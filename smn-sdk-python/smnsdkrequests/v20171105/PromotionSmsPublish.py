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

from smnsdkcore.exception.exceptions import SMNException
from smnsdkcore.http import httpmethod
from smnsdkcore.request import CommonRequest

reload(sys)
sys.setdefaultencoding('utf-8')


class PromotionSmsPublish(CommonRequest):
    def __init__(self):
        super(PromotionSmsPublish, self).__init__()
        self.set_uri('/v2/{project_id}/notifications/sms/promotion')
        self.set_method(httpmethod.POST)

    def set_endpoints(self, endpoints):
        self.add_request_body_param('endpoints', endpoints)

    def set_sms_template_id(self, sms_template_id):
        self.add_request_body_param("sms_template_id", sms_template_id)

    def set_sign_id(self, sign_id):
        self.add_request_body_param('sign_id', sign_id)

    def get_request_body_param(self):
        body_param = CommonRequest.get_request_body_param(self)
        if not body_param.__contains__('sign_id'):
            raise SMNException("param", "sign_id must be set.")

        if not body_param.__contains__('sms_template_id'):
            raise SMNException("param", "sms_template_id must be set.")

        if not body_param.__contains__('endpoints'):
            raise SMNException("param", "endpoints must be set.")
        return body_param
