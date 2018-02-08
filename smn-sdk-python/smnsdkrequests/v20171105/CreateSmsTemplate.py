# coding=utf-8

# Copyright (C) 2018. Huawei Technologies Co., LTD. All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of Apache License, Version 2.0.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License, Version 2.0 for more detail
"""
create at 2018/02/08
"""
__author__ = 'zhangyx'

import sys

from smnsdkcore.http import httpmethod
from smnsdkcore.request import CommonRequest

reload(sys)
sys.setdefaultencoding('utf-8')

class CreateSmsTemplate(CommonRequest):
    def __init__(self):
        super(CreateSmsTemplate, self).__init__()
        self.set_uri('/v2/{project_id}/notifications/sms_template')
        self.set_method(httpmethod.POST)

    def set_sms_template_name(self, sms_template_name):
        self.add_request_body_param('sms_template_name', sms_template_name)

    def set_sms_template_content(self, sms_template_content):
        self.add_request_body_param('sms_template_content', sms_template_content)

    def set_remark(self, remark):
        self.add_request_body_param('remark', remark)

    def set_sms_template_type(self, sms_template_type):
        self.add_request_body_param('sms_template_type', sms_template_type)
