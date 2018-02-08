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

reload(sys)
sys.setdefaultencoding('utf-8')

from smnsdkcore.http import httpmethod
from smnsdkcore.request import CommonRequest


class DeleteSmsTemplate(CommonRequest):
    def __init__(self):
        super(DeleteSmsTemplate, self).__init__()
        self.set_method(httpmethod.DELETE)

    def set_sms_template_id(self, sms_template_id):
        uri = '/v2/{project_id}/notifications/sms_template/' + sms_template_id
        self.set_uri(uri)
