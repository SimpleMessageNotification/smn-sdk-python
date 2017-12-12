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
"""
__author__ = 'pengzl'

from smnsdkcore.http import httpmethod
from smnsdkcore.utils import protocol_helper
from smnsdkcore.exception.exceptions import SMNException
from smnsdkcore.request import CommonRequest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

REMARK_LENGTH = 128
class Subscribe(CommonRequest):
    def __init__(self):
        super(Subscribe, self).__init__()
        self.set_method(httpmethod.POST)

    def set_topic_urn(self, topic_urn):
        uri = '/v2/{project_id}/notifications/topics/' + topic_urn + '/subscriptions'
        self.set_uri(uri)
    
    def set_endpoint(self, endpoint):
        protocol = protocol_helper.get_protocol_type(endpoint)
        if protocol is None:
            raise SMNException("param", "endpoint is invalid.")
        self._set_protocol(protocol)
        self.add_request_body_param("endpoint", endpoint)

    def _set_protocol(self, protocol):
        self.add_request_body_param('protocol', protocol)
    
    def set_remark(self, remark):
        remark_len = len(remark.encode('utf-8'))
        if (remark_len > REMARK_LENGTH):
            raise SMNException("param", "remark is exceed 128 byte.")
        self.add_request_body_param("remark", remark)
    