# coding=utf-8

#Copyright (C) 2017. Huawei Technologies Co., LTD. All rights reserved.
#
#This program is free software; you can redistribute it and/or modify
#it under the terms of Apache License, Version 2.0.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#Apache License, Version 2.0 for more detail

"""
create at 2017/11/4

IAM mudule, generate authentication to access SMN API

There are two authentication methods to call APIs
1). Token authentication: Requests are authenticated using Tokens.
{
  "auth": {
    "identity": {
      "methods": [
        "password"
      ],
      "password": {
        "user": {
          "name": "username",
          "password": "password",
          "domain": {
            "name": "domainname"
          }
        }
      }
    },
    "scope": {
      "project": {
        "name": "cn-north-1" //The region name "cn-north-1" is used as an example.

      }
    }
  }
}

2). AK/SK authentication: Requests are encrypted using the access key (AK) and secret key (SK) to provide higher security.

"""

__author__ = 'pengzl'

import json
import httplib
import datetime
import logging
from ..http import httpmethod
from ..http.http_client import HttpClient
from ..exception import error_info
from ..exception.exceptions import SMNException 

logger = logging.getLogger(__name__)

class Auth():
    X_AUTH_TOKEN_REQUEST_BODY = {
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": "username",
                    "password": "password",
                    "domain": {
                        "name": "domainname"
                    }
                }
            }
        },
        "scope": {
            "project": {
                "name": "cn-north-1"
            }
        }
    }
    }
    
    IAM_ENDPOINT = 'iam.%s.myhuaweicloud.com'
    API_PATH = '/v3/auth/tokens'
    
    def __init__(self,
                 domain_name=None,
                 username=None,
                 password=None,
                 access_key=None,
                 secret_key=None,
                 region_id='cn-north-1'):
        
        """
        @param domain_name: String, Tenant domain_name
        @param username: String, sub username
        @param password: String, password
        @param access_key: String, access key
        @param secret_key: String, secret_key
        @param region_id: String, region_id
        """
        
        self._domain_name = domain_name
        self._username = username
        if username is None:
            self._username = domain_name
        self._password = password
        self._ak = access_key
        self._sk = secret_key
        self._region_id = region_id
        
        self._x_auth_token = None
        self._project_id = None
        self._token_expire_time = None
        
    def get_x_auth_token(self):
        if self._get_x_auth_token() and self._token_is_valid() and self.get_project_id():
            logger.debug('x-auth-token is in cache, get it from cache.')
            return self._get_x_auth_token()
        if not (self._domain_name and self._username and self._password):
            sdk_error = error_info.get_error_info('SDK_AUTH_USER_PASSWORD_INVALID')
            raise SMNException(sdk_error[0], sdk_error[1])
        logger.debug("Start to get x-auth-token, iam host is %s, url is %s",\
                     self._get_endpoint(),self.API_PATH)
        httpclient = HttpClient(host=self._get_endpoint(),
                                url=self.API_PATH,
                                method=httpmethod.POST,
                                body=self._get_x_auth_token_request(),
                                headers={'Content-Type':'application/json'}
                                )
        status, headers, body = httpclient.get_https_response()
        
        if status < httplib.OK or status >= httplib.MULTIPLE_CHOICES:
            raise SMNException(status, body)
        
        self._parse_iam_resp_body(body)
        for header in headers:
            if header[0].lower() == 'x-subject-token':
                self._set_x_auth_token(header[1])
                logger.debug('Success to get x-auth-token from iam server.')
                return header[1]
        
    def _get_x_auth_token_request(self):
        body = self.X_AUTH_TOKEN_REQUEST_BODY
        body.get('auth').get('identity').get('password').get('user')['name'] = self._get_username()
        body.get('auth').get('identity').get('password').get('user')['password'] = self._get_password()
        body.get('auth').get('identity').get('password').get('user').get('domain')['name'] = self._get_domain_name()
        body.get('auth').get('scope').get('project')['name'] = self._get_region_id()
        return json.dumps(body)
    
    def _parse_iam_resp_body(self, iam_body):
        body_dict = json.loads(iam_body)
        project_id = body_dict.get('token').get('project').get('id')
        expire_time = body_dict.get('token').get('expires_at')
        self.set_project_id(project_id)
        self._set_token_expire_time(expire_time)

    def _token_is_valid(self):
        now_utc = datetime.datetime.utcnow()
        expect_token_expire_time = (now_utc + datetime.timedelta(hours=0.5)).strftime("%Y-%m-%dT%H%M%SZ")
        token_expire_time = self._get_token_expire_time()
        logger.debug("(now_utc + 30 minutes) is %s, token expire time is %s.", expect_token_expire_time, token_expire_time)
        if token_expire_time:
            return token_expire_time > expect_token_expire_time
        
        return False
    
    def _set_x_auth_token(self, token):
        self._x_auth_token = token
    
    def _get_x_auth_token(self):
        return self._x_auth_token
    
    def _get_username(self):
        return self._username
    
    def _get_domain_name(self):
        return self._domain_name
    
    def _get_password(self):
        return self._password
    
    def _get_region_id(self):
        return self._region_id
    
    def _get_ak(self):
        return self._ak
    
    def _get_sk(self):
        return self._sk
    
    def _set_token_expire_time(self, expire_time):
        self._token_expire_time = expire_time
    
    def _get_token_expire_time(self):
        return self._token_expire_time
    
    def get_project_id(self):
        if self._project_id:
            return self._project_id
        self.get_x_auth_token()
        return self._project_id
    
    def set_project_id(self, project_id):
        self._project_id = project_id
    
    def _get_endpoint(self):
        return self.IAM_ENDPOINT %(self.get_region_id())
        
    def get_region_id(self):
        return self._region_id

if __name__ == '__main__':

    format_string = "%(asctime)s %(name)s [%(levelname)s] %(message)s"

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(format_string)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    auth = Auth(domain_name='XXXXXX',
                password='XXXXXX')
    print auth.get_x_auth_token()
    print auth.get_project_id()
    print auth._get_token_expire_time()
    print auth.get_x_auth_token()