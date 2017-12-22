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
from smnsdkcore.exception.exceptions import SMNException
from smnsdkcore.request import CommonRequest
from smnsdkcore.utils.protocol_helper import get_protocol_type
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class SmsPublish(CommonRequest):
    def __init__(self):
        super(SmsPublish, self).__init__()
        self.set_uri('/v2/{project_id}/notifications/sms')
        self.set_method(httpmethod.POST)
    
    def set_endpoint(self, endpoint):
        is_sms = get_protocol_type(endpoint)
        if is_sms != 'sms':
            raise SMNException("param", "telephone endpoint is invalid")
        self.add_request_body_param('endpoint', endpoint)
        
    def set_message(self, message):
        self.add_request_body_param("message", message)
        
    def set_sign_id(self, sign_id):
        self.add_request_body_param('sign_id', sign_id)
    
    def get_request_body_param(self):
        body_param = CommonRequest.get_request_body_param(self)
        if body_param.__contains__('sign_id'):
            return body_param
        else:
            raise SMNException("param", "sign_id must be set.")
