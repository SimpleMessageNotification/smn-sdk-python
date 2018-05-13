# coding=utf-8

#Copyright (C) 2018. Huawei Technologies Co., LTD. All rights reserved.
#
#This program is free software; you can redistribute it and/or modify
#it under the terms of Apache License, Version 2.0.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#Apache License, Version 2.0 for more detail

"""
Demo for tenant email
"""
from smnsdkcore.client import SMNClient
from smnsdkrequests.v20171105.PublishTenantEmail import PublishTenantEmail

__author__ = 'zhangyx'

if __name__ == "__main__":
    client = SMNClient(username='YourAccountUserName', domain_name='YourAccountDomainName', password='YourAccountPassword', region_id='YourRegionName')
    request = PublishTenantEmail()
    request.set_message("test_email")
    request.set_subject("helloworld")
    request.set_display_name("test123")
    request.set_cc(["375831500@qq.com", "zhangyaxing@huawei.com"])
    status, headers, response_body = client.send(request)
    print status, response_body