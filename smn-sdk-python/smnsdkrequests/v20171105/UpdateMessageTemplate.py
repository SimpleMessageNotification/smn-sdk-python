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

from smnsdkcore.request import CommonRequest
from smnsdkcore.http import httpmethod
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class UpdateMessageTemplate(CommonRequest):
    def __init__(self):
        super(UpdateMessageTemplate, self).__init__()
        self.set_method(httpmethod.PUT)
    
    def set_message_template_id(self, message_template_id):
        uri = '/v2/{project_id}/notifications/message_template/' + message_template_id
        self.set_uri(uri)
        
    def set_content(self, content):
        self.add_request_body_param('content', content)
