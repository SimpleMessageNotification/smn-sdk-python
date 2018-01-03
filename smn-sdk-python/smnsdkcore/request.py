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
Common Request mudule
create at 2017/11/4
"""
__author__ = 'pengzl'

from http import httpmethod

class CommonRequest(object):
    def __init__(self):
        self._endpoint = None
        self._project_id = None
        self._uri = None
        self._header = {}
        self._query_param = {}
        self._request_body_param = {}
        self._method = httpmethod.GET
        self._header['Content-type'] = 'application/json'
    
    def set_endpoint(self, endpoint):
        self._endpoint = endpoint
    
    def get_endpoint(self):
        return self._endpoint
    
    def set_project_id(self, project_id):
        self._project_id = project_id
        
    def get_project_id(self):
        return self._project_id
    
    def set_uri(self, uri):
        self._uri = uri
        
    def get_uri(self):
        uri = self._uri
        if self._query_param:
            uri = uri + '?'
            for key in self._query_param:
                uri = uri + key + '=' + str(self._query_param[key]) + '&'
        return uri
    
    def add_header(self, key, value):
        self._header[key] = value
    
    def get_headers(self):
        return self._header
    
    def add_query_param(self, key, value):
        self._query_param[key] = value
    
    def get_query_param(self):
        return self._query_param
    
    def add_request_body_param(self, key, value):
        self._request_body_param[key] = value
    
    def get_request_body_param(self):
        return self._request_body_param
    
    def set_method(self, method):
        self._method = method
    
    def get_method(self):
        return self._method
    
        