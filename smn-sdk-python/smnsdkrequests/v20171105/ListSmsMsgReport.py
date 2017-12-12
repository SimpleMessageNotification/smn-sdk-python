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

class ListSmsMsgReport(CommonRequest):
    def __init__(self):
        super(ListSmsMsgReport, self).__init__()
        self.set_uri('/v2/{project_id}/notifications/sms/report')
        self.set_method(httpmethod.GET)
        self.add_query_param('offset', 0)
        self.add_query_param('limit', 100)
    
    def set_offset(self, offset):
        self.add_query_param('offset', offset)
        
    def get_offset(self):
        return self.get_query_param().get('offset')
    
    def set_limit(self, limit):
        self.add_query_param('limit', limit)
        
    def get_limit(self):
        return self.get_query_param().get('limit')
    
    def set_start_time(self, start_time):
        self.add_query_param('start_time', "%.f"%start_time)
    
    def set_end_time(self, end_time):
        self.add_query_param('end_time', "%.f"%end_time)
    
    def set_sign_id(self, sign_id):
        self.add_query_param('sign_id', sign_id)
    
    def set_query_mobile(self, mobile):
        self.add_query_param('mobile', mobile)
    
    def set_query_sms_status(self, status):
        self.add_query_param('status', status)
