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

import httplib
import logging

logger = logging.getLogger(__name__)

from http_request import HttpRequest

class HttpClient(HttpRequest):
    def __init__(
            self,
            host="",
            url="/",
            method="GET",
            headers={},
            protocol="https",
            body=None,
            port=443,
            key_file=None,
            cert_file=None,
            timeout=None):
        HttpRequest.__init__(
            self,
            host=host,
            url=url,
            method=method,
            body=body,
            headers=headers)
        self.__ssl_enable = False
        if protocol is "https":
            self.__ssl_enable = True
        self.__key_file = key_file
        self.__cert_file = cert_file
        self.__port = port
        self.__connection = None
        self._timeout = timeout

    def set_ssl_enable(self, enable):
        self.__ssl_enable = enable

    def get_ssl_enabled(self):
        return self.__ssl_enable

    def get_response(self):
        if self.get_ssl_enabled():
            return self.get_https_response()
        else:
            return self.get_http_response()

    def get_response_object(self):
        if self.get_ssl_enabled():
            return self.get_https_response_object()
        else:
            return self.get_http_response_object()

    def get_http_response(self):
        if self.__port is None or self.__port == "":
            self.__port = 80
        logger.debug('Excute http request, port is %s \
                    host is : %s, url is %s', self.__port, self.get_host(), self.get_url())
        try:
            self.__connection = httplib.HTTPConnection(
                self.get_host(), self.__port, timeout=self._timeout)
            self.__connection.connect()
            self.__connection.request(
                method=self.get_method(),
                url=self.get_url(),
                body=self.get_body(),
                headers=self.get_headers())
            response = self.__connection.getresponse()
            return response.status, response.getheaders(), response.read()
        finally:
            self.__close_connection()

    def get_https_response(self):
        if self.__port is None or self.__port == "":
            self.__port = 443
        logger.debug('Excute https request, method is %s, port is %s, host is : %s, url is %s',\
                    self.get_method(), self.__port, self.get_host(), self.get_url())
        try:
            self.__connection = httplib.HTTPSConnection(
                self.get_host(),
                self.__port,
                cert_file=self.__cert_file,
                key_file=self.__key_file,
                timeout=self._timeout)
            self.__connection.connect()
            self.__connection.request(
                method=self.get_method(),
                url=self.get_url(),
                body=self.get_body(),
                headers=self.get_headers())
            response = self.__connection.getresponse()
            return response.status, response.getheaders(), response.read()
        finally:
            self.__close_connection()

    def __close_connection(self):
        if self.__connection is not None:
            self.__connection.close()
            self.__connection = None
