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
from smnsdkcore.utils.protocol_helper import valid_protocol
from smnsdkcore.exception.exceptions import SMNException
from smnsdkcore.request import CommonRequest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class CreateMessageTemplate(CommonRequest):
    def __init__(self):
        super(CreateMessageTemplate, self).__init__()
        self.set_uri('/v2/{project_id}/notifications/message_template')
        self.set_method(httpmethod.POST)
    
    def set_message_template_name(self, message_template_name):
        self.add_request_body_param('message_template_name', message_template_name)
    
    def set_content(self, content):
        self.add_request_body_param('content', content)
    
    def set_protocol(self, protocol):
        if not valid_protocol(protocol):
            raise SMNException("param", "protocol is not support.")
        self.add_request_body_param('protocol', protocol)
    
    def set_protocol_to_default(self):
        self.add_request_body_param('protocol', 'default')
