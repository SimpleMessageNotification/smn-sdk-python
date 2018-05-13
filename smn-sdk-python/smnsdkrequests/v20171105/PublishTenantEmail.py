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
create at 2018/5/13
"""
__author__ = 'zhangyx'

from smnsdkcore.http import httpmethod
from smnsdkcore.request import CommonRequest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class PublishTenantEmail(CommonRequest):
    def __init__(self):
        super(PublishTenantEmail, self).__init__()
        self.set_uri('/v2/{project_id}/notifications/tenant_email')
        self.set_method(httpmethod.POST)

    def set_subject(self, subject):
        self.add_request_body_param("subject", subject)

    def set_display_name(self, display_name):
        self.add_request_body_param("display_name", display_name)

    def set_message(self, message):
        self.add_request_body_param("message", message)

    def set_email_reply_to(self, email_reply_to):
        self.add_request_body_param("email_reply_to", email_reply_to)

    def set_to(self, to):
        self.add_request_body_param("to", to)

    def set_cc(self, cc):
        self.add_request_body_param("cc", cc)

    def set_bcc(self, bcc):
        self.add_request_body_param("bcc", bcc)
