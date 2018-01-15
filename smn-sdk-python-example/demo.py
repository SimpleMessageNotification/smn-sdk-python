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
Demo for how to use smn python sdk
"""
from smnsdkrequests.v20171105.ListTopicAttribute import ListTopicAttribute
__author__ = 'pengzl'

from smnsdkcore.client import SMNClient
from smnsdkrequests.v20171105.CreateTopic import CreateTopic
from smnsdkrequests.v20171105.UpdateTopic import UpdateTopic
from smnsdkcore import set_stream_logger
from smnsdkrequests.v20171105.DeleteTopic import DeleteTopic
from smnsdkrequests.v20171105.ListTopics import ListTopics
from smnsdkrequests.v20171105.QueryTopicDetail import QueryTopicDetail
from smnsdkrequests.v20171105.UpdateTopicAttribute import SimpleConfigTopicPolicy
from smnsdkrequests.v20171105.UpdateTopicAttribute import UpdateTopicIntroduction
from smnsdkrequests.v20171105.DeleteTopicAttributeByName import DeleteTopicAttributeByName
from smnsdkrequests.v20171105.DeleteTopicAttribute import DeleteTopicAttribute
from smnsdkrequests.v20171105.ListSubscriptions import ListSubscriptions
from smnsdkrequests.v20171105.ListSubscriptionsByTopic import ListSubscriptionsByTopic
from smnsdkrequests.v20171105.Subscribe import Subscribe
from smnsdkrequests.v20171105.Unsubscribe import Unsubscribe
from smnsdkrequests.v20171105.CreateMessageTemplate import CreateMessageTemplate
from smnsdkrequests.v20171105.UpdateMessageTemplate import UpdateMessageTemplate
from smnsdkrequests.v20171105.DeleteMessageTemplate import DeleteMessageTemplate
from smnsdkrequests.v20171105.ListMessageTemplates import ListMessageTemplates
from smnsdkrequests.v20171105.QueryMessageTemplateDetail import QueryMessageTemplateDetail
from smnsdkrequests.v20171105 import Publish
from smnsdkrequests.v20171105.Publish import PublishMessage, PublishMessageWithStruct,\
    PublishMessageWithTemplate


def demoCreateTopic(topic_name, display_name):
    request = CreateTopic()
    request.set_topic_name(topic_name)
    request.set_display_name(display_name)
    return client.send(request)

def demoUpdateTopic(topic_name,update_name):
    request = UpdateTopic()
    request.set_topic_urn(topic_name)
    request.set_display_name(update_name)
    return client.send(request)

def demoDeleteTopic(topic_urn):
    request = DeleteTopic()
    request.set_topic_urn(topic_urn)
    return client.send(request)
    
def demoListTopics():
    request = ListTopics()
    request.set_offset(0)
    request.set_limit(100)
    return client.send(request)

def demoQueryTopicDetail(topic_urn):
    request = QueryTopicDetail()
    request.set_topic_urn(topic_urn)
    return client.send(request)

def demoListTopicAttributes(topic_urn, atrribute_name):
    request = ListTopicAttribute()
    request.set_topic_urn(topic_urn)
    request.set_attribute_name(atrribute_name)
    return client.send(request)

def demoUpdateTopicAttribute(topic_urn, domain_id_list=[], service_list=[]):
    request = SimpleConfigTopicPolicy()
    request.set_topic_urn(topic_urn)
    if domain_id_list == []:
        requset.authrize_to_all_users()
    else:
        request.authrize_to_users(domain_id_list)
    
    if service_list != []:
        request.authrize_to_services(service_list)
    
    return client.send(request)

def demoUpdateTopicIntroduction(topic_urn, introduction):
    request = UpdateTopicIntroduction()
    request.set_topic_urn(topic_urn)
    request.set_introduction(introduction)
    return client.send(request)

def demoDeleteTopicAttributeByName(topic_urn, atrribute_name):
    request = DeleteTopicAttributeByName()
    request.set_topic_attribute_name(atrribute_name)
    request.set_topic_urn(topic_urn)
    return client.send(request)

def demoDeleteTopicAttribute(topic_urn):
    request = DeleteTopicAttribute()
    request.set_topic_urn(topic_urn)
    return client.send(request)

def demoListSubscriptions(offset, limit):
    request = ListSubscriptions()
    request.set_offset(offset)
    request.set_limit(limit)
    return client.send(request)

def demoListSubscriptionsByTopic(topic_urn, offset, limit):
    request = ListSubscriptionsByTopic()
    request.set_offset(offset)
    request.set_limit(limit)
    request.set_topic_urn(topic_urn)
    return client.send(request)

def demoSubscribe(topic_urn, endpoint, remark):
    request = Subscribe()
    request.set_endpoint(endpoint)
    request.set_remark(remark)
    request.set_topic_urn(topic_urn)
    return client.send(request)

def demoUnsubscribe(subscription_urn):
    request = Unsubscribe()
    request.set_subscription_urn(subscription_urn)
    return client.send(request)

def demoCreateMessageTemplate(template_name, content, template_protocol=None):
    request = CreateMessageTemplate()
    request.set_message_template_name(template_name)
    request.set_content(content)
    if not template_protocol:
        request.set_protocol_to_default()
    else:
        request.set_protocol(template_protocol)
    return client.send(request)

def demoUpdateMessageTemplate(message_template_id, update_content):
    request = UpdateMessageTemplate()
    request.set_message_template_id(message_template_id)
    request.set_content(update_content)
    return client.send(request)

def demoDeleteMessageTemplate(message_template_id):
    request = DeleteMessageTemplate()
    request.set_message_template_id(message_template_id)
    return client.send(request)

def demoListMessageTemplates(offset, limit, message_template_name=None, template_protocol=None):
    request = ListMessageTemplates()
    request.set_offset(offset)
    request.set_limit(limit)
    if message_template_name:
        request.set_message_template_name(message_template_name)
    if template_protocol:
        request.set_protocol(template_protocol)
    return client.send(request)

def demoQueryMessageTemplateDetail(message_template_id):
    request = QueryMessageTemplateDetail()
    request.set_message_template_id(message_template_id)
    return client.send(request)

def demoPublishMessage(topic_urn, message):
    request = PublishMessage()
    request.set_topic_urn(topic_urn)
    request.set_subject("Subject, only display to email subscription")
    request.set_message(message)
    return client.send(request)

def demoPublishMessageWithStruct(topic_urn, message_struct):
    request = PublishMessageWithStruct()
    request.set_topic_urn(topic_urn)
    request.set_subject("From Struct Subject, only display to email subscription")
    request.set_message_structure(message_struct)
    return client.send(request)

def demoPublishMessageWithTemplate(topic_urn, message_template_name, tags = None):
    request = PublishMessageWithTemplate()
    request.set_topic_urn(topic_urn)
    request.set_subject("From Template Subject, only display to email subscription")
    request.set_message_template_name(message_template_name)
    if tags:
        request.set_tags(tags)
    return client.send(request)


if __name__ == "__main__":
    #swith on/off the logger
    # set_stream_logger('')
    client = SMNClient(username='YourAccountUserName', domain_name='YourAccountDomainName', password='YourAccountPassword', region_id='YourRegionName')

    test_urn = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk'
    policy_authrozie_to_domain_id = ['123456180e3742b8ac3019e9c2ef7095']
    policy_authrozie_to_service = ['obs']
    introduction = 'this topic use to publish message to subscribed email.'
    endpoint_email = 'pengzl@huawei.com'
    endpoint_remark = 'this is pengzl email'
    subscription_urn = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk:4da9f1d1355e4c8ba7c83a5db10ba236'
    message_template_name = 'pythonsdkCreateTemplate'
    emmail_template_content = 'hello world ,email protocol template, create by {agent_tag}'
    message_template_protocol = 'email'
    message_template_id = '7eda9de266994835a3201e21e30b9cd8'
    message = 'from smn message.'
    message_struct = '{"default":"smn publish with structrue json message, default","sms":"smn publish with structrue json message, to SMS user","email":"smn publish with structrue json message, to Email user"}'
    

    '''
    #demo for topic operattion.
    '''
    status, headers, response_body = demoCreateTopic('python-sdk', 'FromCloud')
    print status, response_body

    status, headers, response_body = demoUpdateTopic(test_urn, 'UpdateFromCloud')
    print status, response_body
    '''
    status, headers, response_body = demoListTopics()
    print status, response_body
    
    status, headers, response_body = demoQueryTopicDetail(test_urn)
    print status, response_body

    status, headers, response_body = demoListTopicAttributes(test_urn, 'access_policy')
    print status, response_body

    

    status, headers, response_body = demoUpdateTopicAttribute(test_urn, \
                                                              domain_id_list = policy_authrozie_to_domain_id,\
                                                              service_list = policy_authrozie_to_service)
    print status, response_body
    
    status, headers, response_body = demoUpdateTopicIntroduction(test_urn, introduction)
    print status, response_body
    
    status, headers, response_body = demoDeleteTopicAttributeByName(test_urn, 'introduction')
    print status, response_body
    
    status, headers, response_body = demoDeleteTopicAttribute(test_urn)
    print status, response_body

    # demo for subscription operations
    # set_stream_logger('')
    status, headers, response_body = demoListSubscriptions(0, 100)
    print status, response_body

    status, headers, response_body = demoListSubscriptionsByTopic(test_urn, 0, 100)
    print status, response_body
    
    status, headers, response_body = demoSubscribe(test_urn, endpoint_email, endpoint_remark)
    print status, response_body

    status, headers, response_body = demoUnsubscribe('urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:peng116:d2309958b9e04561b1fc49b0c85f269e')
    print status, response_body

    # demo for template operation
    status, headers, response_body = demoCreateMessageTemplate(message_template_name, emmail_template_content, template_protocol = message_template_protocol)
    print status, response_body
    
    status, headers, response_body = demoUpdateMessageTemplate(message_template_id, emmail_template_content)
    print status, response_body
    
    status, headers, response_body = demoDeleteMessageTemplate('24fe9ba978d049478b80cece196b2a1a')
    print status, response_body
    
    status, headers, response_body = demoListMessageTemplates(0, 100, message_template_name = message_template_name, template_protocol = message_template_protocol)
    print status, response_body
    
    status, headers, response_body = demoQueryMessageTemplateDetail(message_template_id)
    print status, response_body


    # demo for publish message to topic
    # endpoint which subscribe to the topic will recieve the message.

    status, headers, response_body = demoPublishMessage(test_urn, message)
    print status, response_body

    status, headers, response_body = demoPublishMessageWithStruct(test_urn, message_struct)
    print status, response_body

    status, headers, response_body = demoPublishMessageWithTemplate(test_urn, message_template_name, tags = {"agent_tag":"python-sdk"})
    print status, response_body
    '''