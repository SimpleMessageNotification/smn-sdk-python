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

class UpdateSmsEvent(CommonRequest):
    def __init__(self):
        super(UpdateSmsEvent, self).__init__()
        self.set_uri('/v2/{project_id}/notifications/sms/callback')
        self.set_method(httpmethod.PUT)
        self.sms_reply_event = {}
        self.sms_fail_event = {}
        self.sms_success_event = {}
    
    def set_sms_reply_event(self, topic_urn):
        self.sms_reply_event['event_type'] = 'sms_reply_event'
        self.sms_reply_event['topic_urn'] = topic_urn

    def set_sms_fail_event(self, topic_urn):
        self.sms_fail_event['event_type'] = 'sms_fail_event'
        self.sms_fail_event['topic_urn'] = topic_urn

    def set_sms_success_event(self, topic_urn):
        self.sms_success_event['event_type'] = 'sms_success_event'
        self.sms_success_event['topic_urn'] = topic_urn
        
    def get_request_body_param(self):
        callback = CommonRequest.get_request_body_param(self)
        if callback:
            return callback
        event_list = list()
        if self.sms_reply_event:
            event_list.append(self.sms_reply_event)
        if self.sms_fail_event:
            event_list.append(self.sms_fail_event)
        if self.sms_success_event:
            event_list.append(self.sms_success_event)
        return {"callback": event_list}



