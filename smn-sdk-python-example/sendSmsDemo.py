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
Demo for use smn python sdk to send SMS
"""
__author__ = 'pengzl'

import time
from smnsdkcore.client import SMNClient
from smnsdkrequests.v20171105.SmsPublish import SmsPublish
from smnsdkrequests.v20171105.PromotionSmsPublish import PromotionSmsPublish
from smnsdkrequests.v20171105.CreateSmsTemplate import CreateSmsTemplate
from smnsdkrequests.v20171105.ListSmsTemplates import ListSmsTemplates
from smnsdkrequests.v20171105.GetSmsTemplateDetail import GetSmsTemplateDetail
from smnsdkrequests.v20171105.DeleteSmsTemplate import DeleteSmsTemplate

from smnsdkcore import set_stream_logger
from smnsdkrequests.v20171105.ListSmsSigns import ListSmsSigns
from smnsdkrequests.v20171105.DeleteSmsSign import DeleteSmsSign
from smnsdkrequests.v20171105.ListSmsMsgReport import ListSmsMsgReport
from smnsdkrequests.v20171105.GetSmsMessage import GetSmsMessage
from smnsdkrequests.v20171105.ListSmsEvent import ListSmsEvent
from smnsdkrequests.v20171105.UpdateSmsEvent import UpdateSmsEvent


def demoSendNotifySms(sms_sign_id, endpoint, message):
    request = SmsPublish()
    request.set_endpoint(endpoint)
    request.set_message(message)
    request.set_sign_id(sms_sign_id)
    return client.send(request)

def demoSendPromotionSms():
    request = PromotionSmsPublish()
    request.set_endpoints(['8613688807587', '8618682160029'])
    request.set_sign_id('47f86cf7c9a7449d98ee61cf193a1060')
    request.set_sms_template_id('bfda25c6406e42ddabad74b4a20f6d05')
    return client.send(request)

def demoCreateSmsTemplate():
    request = CreateSmsTemplate()
    request.set_sms_template_content('买买买')
    request.set_sms_template_name('python-SDK-测试模板')
    # 设置模板，0表示通知验证码类，1表示推广营销类
    request.set_sms_template_type(1)
    request.set_remark('python SDK 测试')
    return client.send(request)

def demoListSmsTemplates():
    request = ListSmsTemplates()
    request.set_offset(0)
    request.set_limit(20)
    request.set_sms_template_name('模板')
    #0：审批中 1：审批通过 2：审批不通过 3：已失效
    # request.set_status(1)
    request.set_sms_template_type(1)
    return client.send(request)

def demoGetSmsTemplateDetail():
    request = GetSmsTemplateDetail()
    request.set_sms_template_id('bfda25c6406e42ddabad74b4a20f6d05')
    return client.send(request)

def demoDeleteSmsTemplate():
    request = DeleteSmsTemplate()
    request.set_sms_template_id('21dda6d7443b4fdc9f07d4313d7747ed')
    return client.send(request)

def demoListSmsSigns():
    request = ListSmsSigns()
    return client.send(request)
    
def demoDeleteSmsSign(sms_sign_id):
    request = DeleteSmsSign()
    request.set_sms_sign_id(sms_sign_id)
    return client.send(request)

def demoListSmsMsgReport(start_time, end_time, sms_sign_id, mobile=None, status=None, offset=0, limit=100):
    request = ListSmsMsgReport()
    request.set_start_time(start_time)
    request.set_end_time(end_time)
    request.set_sign_id(sms_sign_id)
    if mobile:
        request.set_query_mobile(mobile)
    if status:
        request.set_query_sms_status(status)
    request.set_offset(offset)
    request.set_limit(limit)
    return client.send(request)

def demoGetSmsMessage(message_id):
    request = GetSmsMessage()
    request.set_message_id(message_id)
    return client.send(request)
    
def demoListSmsEvent():
    request = ListSmsEvent()
    return client.send(request)

def demoUpdateSmsEvent(topic_urn_for_fail=None, topic_urn_for_reply=None, topic_urn_for_success=None):
    request = UpdateSmsEvent()
    if topic_urn_for_fail is not None:
        request.set_sms_fail_event(topic_urn_for_fail)
    if topic_urn_for_reply is not None:
        request.set_sms_reply_event(topic_urn_for_reply)
    if topic_urn_for_success is not None:
        request.set_sms_success_event(topic_urn_for_success)
    return client.send(request)
    

if __name__ == "__main__":
    #swith on/off the logger
    #set_stream_logger('')
    client = SMNClient(username='YourAccountUserName', domain_name='YourAccountDomainName', password='YourAccountPassword', region_id='YourRegionName')
    sms_sign_id = '3fe9fae14729495990cf1a3218fe2aca'
    phoneNumber = '+8618682160029'
    message = '您的验证码是:1234，请查收'

    end_time = time.time() * 1000 + 10 * 60 * 1000
    start_time = end_time - 24 * 3600 * 1000
    sms_success_status = 1

    topic_urn_for_envent = 'urn:smn:cn-north-1:cffe4fc4c9a54219b60dbaf7b586e132:sms_event_urn'
    delete_sms_envent = ''

    # 发送通知验证码类短信
    status, headers, response_body = demoSendNotifySms(sms_sign_id, phoneNumber, message)
    print status, response_body

    # 发送推广类短信
    status, headers, response_body = demoSendPromotionSms()
    print status, response_body

    # 创建短信模板
    status, headers, response_body = demoCreateSmsTemplate()
    print status, response_body

    # 查询短信模板列表
    status, headers, response_body = demoListSmsTemplates()
    print status, response_body

    # 查询短信模板详情
    status, headers, response_body = demoGetSmsTemplateDetail()
    print status, response_body

    # 删除短信模板
    status, headers, response_body = demoDeleteSmsTemplate()
    print status, response_body

    '''
    status, headers, response_body = demoListSmsSigns()
    print status, response_body
    
    # 谨慎删除签名ID
    status, headers, response_body = demoDeleteSmsSign('12345678905241e4b5d85837e6709104')
    print status, response_body
    
    status, headers, response_body = demoListSmsMsgReport(start_time, end_time, sms_sign_id, mobile = phoneNumber, status = sms_success_status)
    print status, response_body

    status, headers, response_body = demoGetSmsMessage('d3e56c2e21c34d67b4eede6cc5a11b61')
    print status, response_body

    status, headers, response_body = demoListSmsEvent()
    print status, response_body

    status, headers, response_body = demoUpdateSmsEvent(topic_urn_for_fail=topic_urn_for_envent,\
                                                        topic_urn_for_reply=topic_urn_for_envent,\
                                                        topic_urn_for_success=delete_sms_envent)
    print status, response_body
    '''
    