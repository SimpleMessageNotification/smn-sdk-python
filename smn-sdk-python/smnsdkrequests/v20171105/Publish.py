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
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

MAX_SUBJECT_LENGTH = 512
class PublishMessage(CommonRequest):
    def __init__(self):
        super(PublishMessage, self).__init__()
        self.set_method(httpmethod.POST)
    
    def set_topic_urn(self, topic_urn):
        uri = '/v2/{project_id}/notifications/topics/' + topic_urn + '/publish'
        self.set_uri(uri)
    
    def set_subject(self, subject):
        subject_bytes = subject.encode('utf-8')
        if (len(subject_bytes) > MAX_SUBJECT_LENGTH):
            raise SMNException("param", "subject byte length excced 512 bytes")
        self.add_request_body_param("subject", subject)
    
    def set_message(self, message):
        self.add_request_body_param("message", message)

class PublishMessageWithStruct(CommonRequest):
    def __init__(self):
        super(PublishMessageWithStruct, self).__init__()
        self.set_method(httpmethod.POST)
    
    def set_topic_urn(self, topic_urn):
        uri = '/v2/{project_id}/notifications/topics/' + topic_urn + '/publish'
        self.set_uri(uri)
    
    def set_subject(self, subject):
        subject_bytes = subject.encode('utf-8')
        if (len(subject_bytes) > MAX_SUBJECT_LENGTH):
            raise SMNException("param", "subject byte length excced 512 bytes")
        self.add_request_body_param("subject", subject)
    
    def set_message_structure(self, message_structure):
        self.add_request_body_param("message_structure", message_structure)

class PublishMessageWithTemplate(CommonRequest):
    def __init__(self):
        super(PublishMessageWithTemplate, self).__init__()
        self.set_method(httpmethod.POST)
    
    def set_topic_urn(self, topic_urn):
        uri = '/v2/{project_id}/notifications/topics/' + topic_urn + '/publish'
        self.set_uri(uri)
    
    def set_subject(self, subject):
        subject_bytes = subject.encode('utf-8')
        if (len(subject_bytes) > MAX_SUBJECT_LENGTH):
            raise SMNException("param", "subject byte length excced 512 bytes")
        self.add_request_body_param("subject", subject)
    
    def set_message_template_name(self, message_template_name):
        self.add_request_body_param("message_template_name", message_template_name)
    
    def set_tags(self, tags):
        self.add_request_body_param("tags", tags)