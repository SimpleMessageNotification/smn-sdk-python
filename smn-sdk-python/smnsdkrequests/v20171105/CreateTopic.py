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
from smnsdkcore.request import CommonRequest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class CreateTopic(CommonRequest):
    def __init__(self):
        super(CreateTopic, self).__init__()
        self.set_uri('/v2/{project_id}/notifications/topics')
        self.set_method(httpmethod.POST)
    
    def set_topic_name(self, topic_name):
        self.add_request_body_param('name', topic_name)
        
    def get_topic_name(self):
        return self.get_request_body_param().get('name')
    
    def set_display_name(self, display_name):
        self.add_request_body_param('display_name', display_name)
    
    def get_display_name(self):
        return self.get_request_body_param().get('display_name')