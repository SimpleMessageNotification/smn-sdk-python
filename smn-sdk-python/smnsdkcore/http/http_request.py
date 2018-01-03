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
__author__ = 'pengzl'

class HttpRequest:

    def __init__(self, host="", url="/", method=None, body=None, headers={}):
        self.__host = host
        self.__url = url
        self.__method = method
        self.__headers = headers
        self.__body = body

    def get_host(self):
        return self.__host

    def set_host(self, host):
        self.__host = host

    def get_body(self):
        return self.__body

    def set_body(self, body):
        self.__body = body

    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url

    def get_method(self):
        return self.__method

    def set_method(self, method):
        self.__method = method

    def get_header_value(self, name):
        return self.__headers[name]

    def put_header_parameter(self, key, value):
        if key is not None and value is not None:
            self.__headers[key] = value

    def get_headers(self):
        return self.__headers
