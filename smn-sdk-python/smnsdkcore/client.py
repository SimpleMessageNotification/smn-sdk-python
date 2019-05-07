# coding=utf-8

# Copyright (C) 2017. Huawei Technologies Co., LTD. All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of Apache License, Version 2.0.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License, Version 2.0 for more detail
"""
SMN Client mudule
create at 2017/11/4
"""
__author__ = 'pengzl'

import json
import logging

from __init__ import __version__
from auth.iam import Auth
from http.http_client import HttpClient
from smnsdkcore.exception.exceptions import SMNException
from smnsdkcore.auth.iam import AkskNova
from apig_sdk import signer

logger = logging.getLogger(__name__)


class SMNClient():
    SMN_ENDPOINT = 'smn.%s.myhuaweicloud.com'

    def __init__(
            self,
            domain_name=None,
            password=None,
            username=None,
            region_id='cn-north-1',
            auto_retry=True,
            max_retry_time=3,
            user_agent='smn-sdk-python/' + __version__,
            port=443,
            connect_timeout=10
    ):

        """
        constructor for SMNClient
        :param domain_name: String, domain_name
        :param username: String, username;if use sub user, need to set username
        :param password: String, user password
        :param region_id: String, region id
        :param auto_retry: Boolean
        :param max_retry_time: Number
        :param user_agent: user_agent, proxy for http(s)
        :param port: Number, default is 443 for https
        :param connect_timeout: Number, http connect timeout
        :return:
        """

        self.__domain_name = domain_name

        self.__username = username
        if not username:
            self.__username = domain_name

        self.__password = password
        self.__region_id = region_id
        self.__auto_retry = auto_retry
        self.__max_retry_time = max_retry_time
        self.__user_agent = user_agent
        self._port = port
        self._connect_timeout = connect_timeout

        self.__authentication = Auth(domain_name=self.__domain_name,
                                     username=self.__username,
                                     password=self.__password,
                                     region_id=self.__region_id
                                     )

    def send(self, smn_request):
        if self._get_user_agent():
            smn_request.add_header('User-Agent', self._get_user_agent())
        self._set_authentication(smn_request)

        endpoint = self._resovle_endpoint()
        if smn_request.get_request_body_param():
            req_body = json.dumps(smn_request.get_request_body_param())
        else:
            req_body = ""
        logger.debug('request body is %s', req_body)
        httpclient = HttpClient(host=endpoint,
                                url=self._resolve_url(smn_request),
                                method=smn_request.get_method(),
                                headers=smn_request.get_headers(),
                                body=req_body,
                                timeout=self._connect_timeout
                                )
        return httpclient.get_https_response()

    def _set_authentication(self, request):
        x_auth_token = self.__authentication.get_x_auth_token()
        request.add_header('X-Auth-Token', x_auth_token)

    def _resovle_endpoint(self):
        if self.__region_id.lower().startswith('dec'):
            region = self.__region_id.split('_')[1]
        else:
            region = self.__region_id.split('_')[0]
        return self.SMN_ENDPOINT % (region)

    def _resolve_url(self, request):
        project_id = self.__authentication.get_project_id()
        return request.get_uri().format(project_id=project_id)

    def _get_user_agent(self):
        return self.__user_agent


class AkskSMNClient:
    SMN_ENDPOINT = 'smn.%s.myhuaweicloud.com'
    IAM_ENDPOINT = 'iam.%s.myhuaweicloud.com'
    PROJECT_ID_URI = '/v3/projects'

    def __init__(
            self,
            access, secret,
            securitytoken=None,
            region_id='cn-north-1',
            smn_endpoint=None,
            iam_endpoint=None,
            auto_retry=True,
            max_retry_time=3,
            user_agent='smn-sdk-python/' + __version__,
            port=443,
            connect_timeout=10
    ):

        """
        constructor for AkskSMNClient
        :param access: String, access
        :param secret: String, secret
        :param securitytoken: String, when use temporary AKs and SKs is needed.
        :param region_id: String, region id
        :param smn_endpoint: String, smn_endpoint
        :param iam_endpoint: String, iam_endpoint
        :param auto_retry: Boolean
        :param max_retry_time: Number
        :param user_agent: user_agent, proxy for http(s)
        :param port: Number, default is 443 for https
        :param connect_timeout: Number, http connect timeout
        :return:
        """
        self.__access = access
        self.__secret = secret
        self.__securitytoken = securitytoken
        self.__region_id = region_id
        if smn_endpoint is not None:
            self.__smn_endpoint = smn_endpoint
        else:
            self.__smn_endpoint = self._resovle_endpoint(self.SMN_ENDPOINT)

        if iam_endpoint is not None:
            self.__iam_endpoint = iam_endpoint
        else:
            self.__iam_endpoint = self._resovle_endpoint(self.IAM_ENDPOINT)
        self.__auto_retry = auto_retry
        self.__max_retry_time = max_retry_time
        self.__user_agent = user_agent
        self._port = port
        self._connect_timeout = connect_timeout

    def send(self, smn_request):
        project_id = self._get_project_id()
        uri, query = self._resolve_url(smn_request, project_id)
        header = {"content-type": "application/json",
                  "x-project-id": project_id}
        if smn_request.get_request_body_param():
            req_body = json.dumps(smn_request.get_request_body_param())
        else:
            req_body = ""
        return self._get_response(smn_request.get_method(), self.__smn_endpoint, uri, header, query=query,
                                  body=req_body)

    def _get_project_id(self):
        '''get project id by ak/sk or ak/sk/securitytoken'''

        header = {"content-type": "application/json"}
        response = self._get_response('GET', self.__iam_endpoint, self.PROJECT_ID_URI, header,
                                      query={"name": self.__region_id})
        message_map = json.loads(response[2])
        try:
            project_id = message_map['projects'][0]['id']
        except Exception:
            raise SMNException(response[0], response[2])

        if project_id is None or len(project_id) == 0:
            raise SMNException(response[0], 'Failed to get project id by aksk auth. project_id is null.')
        return project_id

    def _get_response(self, methed, host, uri, header, query=None, body=None):

        sig = signer.Signer()
        # Set the AK/SK to sign and authenticate the request.
        sig.Key = self.__access
        sig.Secret = self.__secret
        # The following example shows how to set the request URL and parameters to query a VPC list.
        r = signer.HttpRequest()
        r.scheme = "https"
        # Set request Endpoint.
        r.host = host
        # Specify a request method, such as GET, PUT, POST, DELETE, HEAD, and PATCH.
        r.method = methed
        # Set request URI.
        r.uri = uri
        # Set parameters for the request URL.
        r.query = query
        # Add header parameters, for example, x-domain-id for invoking a global service and x-project-id for invoking a project-level service.
        r.headers = header
        if body is not None:
            r.body = body
        sig.Sign(r)

        if self.__securitytoken is not None:
            r.headers['X-Security-Token'] = self.__securitytoken

        httpclient = HttpClient(host=r.host,
                                url=r.uri,
                                method=r.method,
                                headers=r.headers,
                                body=r.body,
                                timeout=self._connect_timeout
                                )
        return httpclient.get_https_response()

    def _resolve_url(self, request, project_id):
        query = {}
        url = request.get_uri().format(project_id=project_id)
        # split uri and query string
        if '?' not in url:
            return url, query
        url = url.split('?')

        pre_uri = url[0]
        query_str = str(url[1])
        # split query key and value
        if '&' not in query_str:
            return pre_uri, query
        query_list = query_str.split('&')

        for q in query_list:
            if q is None or len(q) == 0:
                continue
            key_val = q.split('=')
            if key_val[1] is None or len(key_val[1]) == 0:
                continue
            query[key_val[0]] = key_val[1]
        return pre_uri, query

        return request.get_uri().format(project_id=project_id)

    def _resovle_endpoint(self, domain_name):
        if self.__region_id.lower().startswith('dec'):
            region = self.__region_id.split('_')[1]
        else:
            region = self.__region_id.split('_')[0]
        return domain_name % (region)
