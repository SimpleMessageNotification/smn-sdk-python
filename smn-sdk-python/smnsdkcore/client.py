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

        endpoint = self._resovle_endpoiint()
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

    def _resovle_endpoiint(self):
        return self.SMN_ENDPOINT % (self.__region_id)

    def _resolve_url(self, request):
        project_id = self.__authentication.get_project_id()
        return request.get_uri().format(project_id=project_id)

    def _get_user_agent(self):
        return self.__user_agent
