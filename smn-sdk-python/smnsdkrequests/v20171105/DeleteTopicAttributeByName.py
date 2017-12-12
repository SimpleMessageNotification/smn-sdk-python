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

from smnsdkcore.exception.exceptions import SMNException
from smnsdkcore.request import CommonRequest
from smnsdkcore.http import httpmethod

class DeleteTopicAttributeByName(CommonRequest):
    def __init__(self):
        super(DeleteTopicAttributeByName, self).__init__()
        self.set_method(httpmethod.DELETE)
        self.attribute_name = ''
    
    def set_topic_urn(self, topic_urn):
        uri = '/v2/{project_id}/notifications/topics/' + topic_urn + '/attributes/'
        self.set_uri(uri)
        
    def set_topic_attribute_name(self, name):
        self.attribute_name = name;
    
    def get_uri(self):
        uri = CommonRequest.get_uri(self)
        if not uri:
            raise SMNException("param", "topic_urn need to set.")
        if not self.attribute_name:
            raise SMNException("param", "attribute_name need to set.")
        return uri + self.attribute_name
    