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
Testcase for request
create at 2017/11/4
"""
import time
import unittest
from smnsdkrequests.v20171105.CreateTopic import CreateTopic
from smnsdkrequests.v20171105.DeleteTopic import DeleteTopic
from smnsdkrequests.v20171105.UpdateTopic import UpdateTopic
from smnsdkrequests.v20171105.ListTopics import ListTopics
from smnsdkrequests.v20171105.QueryTopicDetail import QueryTopicDetail
from smnsdkrequests.v20171105.ListTopicAttribute import ListTopicAttribute
from smnsdkrequests.v20171105.DeleteTopicAttribute import DeleteTopicAttribute
from smnsdkrequests.v20171105.DeleteTopicAttributeByName import DeleteTopicAttributeByName
from smnsdkrequests.v20171105.UpdateTopicAttribute import SimpleConfigTopicPolicy
from smnsdkrequests.v20171105.UpdateTopicAttribute import UpdateTopicIntroduction
from smnsdkrequests.v20171105.UpdateTopicAttribute import UpdateTopicSmsSignId
from smnsdkrequests.v20171105.ListSubscriptions import ListSubscriptions
from smnsdkrequests.v20171105.ListSubscriptionsByTopic import ListSubscriptionsByTopic
from smnsdkrequests.v20171105.Subscribe import Subscribe
from smnsdkrequests.v20171105.Unsubscribe import Unsubscribe
from smnsdkrequests.v20171105.CreateMessageTemplate import CreateMessageTemplate
from smnsdkrequests.v20171105.UpdateMessageTemplate import UpdateMessageTemplate
from smnsdkrequests.v20171105.DeleteMessageTemplate import DeleteMessageTemplate
from smnsdkrequests.v20171105.ListMessageTemplates import ListMessageTemplates
from smnsdkrequests.v20171105.QueryMessageTemplateDetail import QueryMessageTemplateDetail
from smnsdkrequests.v20171105.Publish import PublishMessage, PublishMessageWithStruct
from smnsdkrequests.v20171105.Publish import PublishMessageWithTemplate
from smnsdkrequests.v20171105.SmsPublish import SmsPublish
from smnsdkrequests.v20171105.ListSmsSigns import ListSmsSigns
from smnsdkrequests.v20171105.DeleteSmsSign import DeleteSmsSign
from smnsdkrequests.v20171105.ListSmsMsgReport import ListSmsMsgReport
from smnsdkrequests.v20171105.GetSmsMessage import GetSmsMessage
from smnsdkrequests.v20171105.ListSmsEvent import ListSmsEvent
from smnsdkrequests.v20171105.UpdateSmsEvent import UpdateSmsEvent


__author__ = 'pengzl'

class TestTopic(unittest.TestCase):
    def test_init(self):
        pass
    def test_create_topic(self):
        req = {'name':'topoiname','display_name':'diplay_name_value'}
        createReq = CreateTopic()
        createReq.set_topic_name('topoiname')
        createReq.set_display_name('diplay_name_value')
        self.assertDictEqual(req, createReq.get_request_body_param(), 'not euqal')
        
        uri = createReq.get_uri()
        self.assertEqual('/v2/{project_id}/notifications/topics', uri, 'not equal')
    
    def test_create_topic1(self):
        req = {'name':'topoiname'}
        createReq = CreateTopic()
        createReq.set_topic_name('topoiname')
        self.assertDictEqual(req, createReq.get_request_body_param(), 'error')
    
    def test_delete_topic(self):
        uri = '/v2/{project_id}/notifications/topics/'
        urn = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk'
        deleteTopicReq = DeleteTopic()
        deleteTopicReq.set_topic_urn(urn)
        self.assertEqual(uri + urn, deleteTopicReq.get_uri(), 'not equal')
        
    def test_update_topic(self):
        uri = '/v2/{project_id}/notifications/topics/'
        urn = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk'
        req = {'display_name':'display_name_new'}
        updateTopicReq = UpdateTopic()
        updateTopicReq.set_topic_urn(urn)
        updateTopicReq.set_display_name('display_name_new')
        self.assertDictEqual(req, updateTopicReq.get_request_body_param(), 'not equal')
        self.assertEqual(uri + urn, updateTopicReq.get_uri(), 'not equal')
    
    def test_list_topics(self):
        offset = 1
        limit = 20
        uri = '/v2/{project_id}/notifications/topics?limit=20&offset=1&'
        listTopicReq = ListTopics()
        listTopicReq.set_offset(offset)
        listTopicReq.set_limit(limit)
        self.assertEqual(uri, listTopicReq.get_uri(), listTopicReq.get_uri())

    def test_query_topic_detail(self):
        uri = '/v2/{project_id}/notifications/topics/'
        urn = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk'
        queryTopic = QueryTopicDetail()
        queryTopic.set_topic_urn(urn)
        self.assertEqual(uri + urn, queryTopic.get_uri(), 'not equal')
    
    def test_list_topic_attribute(self):
        urn = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk'
        uri = '/v2/{project_id}/notifications/topics/' + urn + '/attributes?name=access_policy&'
        listTopicAttr = ListTopicAttribute()
        listTopicAttr.set_topic_urn(urn)
        listTopicAttr.set_attribute_name('access_policy')
        self.assertEqual(uri, listTopicAttr.get_uri(), listTopicAttr.get_uri())
        
    def test_delete_topic_attribute(self):
        uri = '/v2/{project_id}/notifications/topics/'
        urn = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk'
        DeleteTopicAttributeReq = DeleteTopicAttribute()
        DeleteTopicAttributeReq.set_topic_urn(urn)
        self.assertEqual(uri + urn + '/attributes', DeleteTopicAttributeReq.get_uri(), 'not equal')
        
    def test_delete_topic_attribute_by_name(self):
        uri = '/v2/{project_id}/notifications/topics/'
        urn = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk'
        DeleteTopicAttributeByNameReq = DeleteTopicAttributeByName()
        DeleteTopicAttributeByNameReq.set_topic_urn(urn)
        DeleteTopicAttributeByNameReq.set_topic_attribute_name('sms_sign_id')
        self.assertEqual(uri + urn + '/attributes/sms_sign_id', DeleteTopicAttributeByNameReq.get_uri(), DeleteTopicAttributeByNameReq.get_uri())
        
    def test_update_topic_policy(self):
        urn = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk'
        uri = '/v2/{project_id}/notifications/topics/' + urn + '/attributes/access_policy'
        domain_id_list = ["5d0448e390ec4645a22465e5d462a815"]
        service_list = ["obs"]
        expect_policy = {'value': '{"Version": "2016-09-07", "Id": "__default_policy_ID", "Statement": [{"Action": ["SMN:Publish"], "Sid": "__user_pub_0", "Resource": "urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk", "Effect": "Allow", "Principal": {"CSP": ["urn:csp:iam::5d0448e390ec4645a22465e5d462a815:root"]}}, {"Action": ["SMN:Publish", "SMN:QueryTopicDetail"], "Sid": "__service_pub_0", "Resource": "urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk", "Effect": "Allow", "Principal": {"Service": ["obs"]}}]}'}
        SimpleConfigTopicPolicyReq = SimpleConfigTopicPolicy()
        SimpleConfigTopicPolicyReq.set_topic_urn(urn)
        SimpleConfigTopicPolicyReq.authrize_to_users(domain_id_list)
        SimpleConfigTopicPolicyReq.authrize_to_services(service_list)
        self.assertEqual(uri, SimpleConfigTopicPolicyReq.get_uri(), "not equal")
        self.assertDictEqual(expect_policy, SimpleConfigTopicPolicyReq.get_request_body_param(), SimpleConfigTopicPolicyReq.get_request_body_param())
    
    def test_update_topic_policy_to_all(self):
        urn = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk'
        uri = '/v2/{project_id}/notifications/topics/' + urn + '/attributes/access_policy'
        expect_policy_to_all = {'value': '{"Version": "2016-09-07", "Id": "__default_policy_ID", "Statement": [{"Action": ["SMN:Publish"], "Sid": "__user_pub_0", "Resource": "urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk", "Effect": "Allow", "Principal": {"CSP": "*"}}]}'}
        SimpleConfigTopicPolicyReq = SimpleConfigTopicPolicy()
        SimpleConfigTopicPolicyReq.set_topic_urn(urn)
        SimpleConfigTopicPolicyReq.authrize_to_all_users()
        self.assertDictEqual(expect_policy_to_all, SimpleConfigTopicPolicyReq.get_request_body_param(), "not equal")
        self.assertEqual(uri, SimpleConfigTopicPolicyReq.get_uri(), "not equal")
    
    def test_update_topic_introduction(self):
        urn = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk'
        uri = '/v2/{project_id}/notifications/topics/' + urn + '/attributes/introduction'
        introduction = "hello this is introduction"
        expect_introduction = {"value": introduction}
        UpdateTopicIntroductionReq = UpdateTopicIntroduction()
        UpdateTopicIntroductionReq.set_topic_urn(urn)
        UpdateTopicIntroductionReq.set_introduction(introduction)
        self.assertDictEqual(expect_introduction, UpdateTopicIntroductionReq.get_request_body_param(), "not equal")
        self.assertEqual(uri, UpdateTopicIntroductionReq.get_uri(), "not equal")
        
    def test_update_topic_sms_sign_id(self):
        urn = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk'
        uri = '/v2/{project_id}/notifications/topics/' + urn + '/attributes/sms_sign_id'
        sign_id = "4bf82e180e3742b8ac3019e9c2ef7000"
        expect_sign_id = {"value": sign_id}
        UpdateTopicSmsSignIdReq = UpdateTopicSmsSignId()
        UpdateTopicSmsSignIdReq.set_topic_urn(urn)
        UpdateTopicSmsSignIdReq.set_sms_sign_id(sign_id)
        self.assertDictEqual(expect_sign_id, UpdateTopicSmsSignIdReq.get_request_body_param(), "not equal")
        self.assertEqual(uri, UpdateTopicSmsSignIdReq.get_uri(), "not equal")
        
class TestSubscription(unittest.TestCase):
    def test_list_subscribtion(self):
        offset = 1
        limit = 20
        uri = '/v2/{project_id}/notifications/subscriptions?limit=20&offset=1&'
        listSubscriptionsReq = ListSubscriptions()
        listSubscriptionsReq.set_offset(offset)
        listSubscriptionsReq.set_limit(limit)
        self.assertEqual(uri, listSubscriptionsReq.get_uri(), listSubscriptionsReq.get_uri())
        
    def test_list_subscription_by_topic(self):
        urn = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk'
        offset = 1
        limit = 20
        uri = '/v2/{project_id}/notifications/topics/' + urn + '/subscriptions?limit=20&offset=1&'
        listSubscriptionsByTopicReq = ListSubscriptionsByTopic()
        listSubscriptionsByTopicReq.set_offset(offset)
        listSubscriptionsByTopicReq.set_limit(limit)
        listSubscriptionsByTopicReq.set_topic_urn(urn)
        self.assertEqual(uri, listSubscriptionsByTopicReq.get_uri(), listSubscriptionsByTopicReq.get_uri())
        
    def test_subscribe_topic(self):
        urn = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk'
        endpoint_sms = "18888888"
        endpoint_email = "pengzl@test.com"
        endpoint_http = "http://test.com/processdata"
        endpoint_https = "https://test.com/processdata"
        endpoint_functionstage = "urn:fss:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:function:default:peng:latest"
        endpoint_functiongraph = "urn:fgs:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:graph:workflow-peng"
        endpoint_dms = "b8a2f8ef-3a7a-4a9c-bed8-fef8cefcd78c"
        remark = "这是个test"

        smsReq = {"endpoint": endpoint_sms, "protocol":"sms", "remark":remark}
        emailReq = {"endpoint": endpoint_email, "protocol":"email", "remark":remark}
        httpReq = {"endpoint": endpoint_http, "protocol":"http", "remark":remark}
        httpsReq = {"endpoint": endpoint_https, "protocol":"https", "remark":remark}
        functionstageReq = {"endpoint": endpoint_functionstage, "protocol":"functionstage", "remark":remark}
        functiongraphReq = {"endpoint": endpoint_functiongraph, "protocol":"functiongraph", "remark":remark}
        dmsReq = {"endpoint": endpoint_dms, "protocol":"dms", "remark":remark}
        subscribeReq = Subscribe()
        subscribeReq.set_remark(remark)

        subscribeReq.set_endpoint(endpoint_sms)
        self.assertEqual(smsReq, subscribeReq.get_request_body_param(), subscribeReq.get_request_body_param())

        subscribeReq.set_endpoint(endpoint_email)
        self.assertEqual(emailReq, subscribeReq.get_request_body_param(), subscribeReq.get_request_body_param())

        subscribeReq.set_endpoint(endpoint_http)
        self.assertEqual(httpReq, subscribeReq.get_request_body_param(), subscribeReq.get_request_body_param())

        subscribeReq.set_endpoint(endpoint_https)
        self.assertEqual(httpsReq, subscribeReq.get_request_body_param(), subscribeReq.get_request_body_param())

        subscribeReq.set_endpoint(endpoint_functionstage)
        self.assertEqual(functionstageReq, subscribeReq.get_request_body_param(), subscribeReq.get_request_body_param())

        subscribeReq.set_endpoint(endpoint_functiongraph)
        self.assertEqual(functiongraphReq, subscribeReq.get_request_body_param(), subscribeReq.get_request_body_param())

        subscribeReq.set_endpoint(endpoint_dms)
        self.assertEqual(dmsReq, subscribeReq.get_request_body_param(), subscribeReq.get_request_body_param())
        
    def test_Unsubscribe(self):
        subscription_urn = "urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:peng116:cdde6bb728024e6dbd721705aa3efaae"
        uri = '/v2/{project_id}/notifications/subscriptions/' + subscription_urn
        unsubscribeReq = Unsubscribe()
        unsubscribeReq.set_subscription_urn(subscription_urn)
        self.assertEqual(uri, unsubscribeReq.get_uri(), unsubscribeReq.get_uri())
        

class TestTemplate(unittest.TestCase):
    def test_create_template(self):
        uri = '/v2/{project_id}/notifications/message_template'
        message_template_name = "smn_message_template"
        content = "This is mesage template"
        defaultTpl = {"message_template_name":message_template_name, "protocol":"default", "content":content}
        smsTpl = {"message_template_name":message_template_name, "protocol":"sms", "content":content}
        createTemplateReq = CreateMessageTemplate()
        createTemplateReq.set_message_template_name(message_template_name)
        createTemplateReq.set_content(content)
        createTemplateReq.set_protocol_to_default()
        self.assertEqual(uri, createTemplateReq.get_uri(), "uri not equal")
        self.assertEqual(defaultTpl, createTemplateReq.get_request_body_param(), "not equal")
        
        createTemplateReq.set_protocol('sms')
        self.assertEqual(smsTpl, createTemplateReq.get_request_body_param(), "not equal")
        
    def test_update_template(self):
        message_template_id = '445b9fe05bf3401b8b353bc755be4c46'
        content = "The game will start at {time_tag}"
        uri = '/v2/{project_id}/notifications/message_template/' + message_template_id
        reqdict = {"content":content}
        updateTplReq = UpdateMessageTemplate()
        updateTplReq.set_message_template_id(message_template_id)
        updateTplReq.set_content(content)
        
        self.assertEqual(uri, updateTplReq.get_uri(), "not equal")
        self.assertEqual(reqdict, updateTplReq.get_request_body_param(), "not equal")
        
    def test_delete__template(self):
        message_template_id = '445b9fe05bf3401b8b353bc755be4c46'
        uri = '/v2/{project_id}/notifications/message_template/' + message_template_id
        deleteTemplateReq = DeleteMessageTemplate()
        deleteTemplateReq.set_message_template_id(message_template_id)
        self.assertEqual(uri, deleteTemplateReq.get_uri(), "not equal")
        
    def test_list_message_template(self):
        offset = 1
        limit = 20
        message_template_name = 'smn_message_template'
        protocol = 'sms'
        uri = '/v2/{project_id}/notifications/message_template?message_template_name=smn_message_template&limit=20&protocol=sms&offset=1&'
        
        listMessageTpl = ListMessageTemplates()
        listMessageTpl.set_offset(offset)
        listMessageTpl.set_limit(limit)
        listMessageTpl.set_message_template_name(message_template_name)
        listMessageTpl.set_protocol(protocol)
        self.assertEqual(uri, listMessageTpl.get_uri(), "not equal")
    
    def test_query_message_template_detail(self):
        message_template_id = '445b9fe05bf3401b8b353bc755be4c46'
        uri = '/v2/{project_id}/notifications/message_template/' + message_template_id
        queryMessageTplReq = QueryMessageTemplateDetail()
        queryMessageTplReq.set_message_template_id(message_template_id)
        self.assertEqual(uri, queryMessageTplReq.get_uri(), "not equal")

class TestPublish(unittest.TestCase):
    def test_publishMessage(self):
        topic_urn = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk'
        subject = "from SMN service"
        message = "hello world"
        uri = '/v2/{project_id}/notifications/topics/' + topic_urn + '/publish'
        reqDict = {'subject':subject, 'message':message}
        publishMsgReq = PublishMessage()
        publishMsgReq.set_subject(subject)
        publishMsgReq.set_message(message)
        publishMsgReq.set_topic_urn(topic_urn)
        
        self.assertEqual(uri, publishMsgReq.get_uri(), "not equal")
        self.assertEqual(reqDict, publishMsgReq.get_request_body_param(), 'not equal')
    
    def test_publishMessageWithStruct(self):
        topic_urn = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk'
        subject = "from SMN service"
        messageStruct = '{"default":"test v2 default", "sms":"verify code is 123456"}'
        uri = '/v2/{project_id}/notifications/topics/' + topic_urn + '/publish'
        reqDict = {'subject':subject, 'message_structure':messageStruct}
        publishMsgWithStructReq = PublishMessageWithStruct()
        publishMsgWithStructReq.set_subject(subject)
        publishMsgWithStructReq.set_message_structure(messageStruct)
        publishMsgWithStructReq.set_topic_urn(topic_urn)
        
        self.assertEqual(uri, publishMsgWithStructReq.get_uri(), "not equal")
        self.assertEqual(reqDict, publishMsgWithStructReq.get_request_body_param(), 'not equal')
        
    def test_publishMessageWithMessage(self):
        topic_urn = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk'
        subject = "from SMN service"
        message_template_name = 'smn_message_template'
        tags = dict()
        tags['time_tag'] = "2017-11-4 15:00"
        uri = '/v2/{project_id}/notifications/topics/' + topic_urn + '/publish'
        reqDict = {'subject':subject, 'message_template_name':message_template_name, 'tags':tags}
        
        publishMsgWithTemplateReq = PublishMessageWithTemplate()
        publishMsgWithTemplateReq.set_message_template_name(message_template_name)
        publishMsgWithTemplateReq.set_tags(tags)
        publishMsgWithTemplateReq.set_topic_urn(topic_urn)
        publishMsgWithTemplateReq.set_subject(subject)
        self.assertEqual(uri, publishMsgWithTemplateReq.get_uri(), "not equal")
        self.assertEqual(reqDict, publishMsgWithTemplateReq.get_request_body_param(), 'not equal')
        

class TestSms(unittest.TestCase):
    def test_publish_sms(self):
        uri = '/v2/{project_id}/notifications/sms'
        endpoint = '1868888'
        sign_id = '94d3b63a5dfb475994d3ac34664e2346'
        message = '您的验证码是：123456'
        reqMap = {'endpoint':endpoint, 'message':message, 'sign_id':sign_id}
        
        publishSmsReq = SmsPublish()
        publishSmsReq.set_endpoint(endpoint)
        publishSmsReq.set_message(message)
        publishSmsReq.set_sign_id(sign_id)
        
        self.assertEqual(uri, publishSmsReq.get_uri(), "not equal")
        self.assertEqual(reqMap, publishSmsReq.get_request_body_param(), "not equal")
    
    def test_list_sms_sign(self):
        uri = '/v2/{project_id}/notifications/sms_sign'
        listSmsSignReq = ListSmsSigns()
        self.assertEqual(uri, listSmsSignReq.get_uri(), "not equal")
        
    def test_delete_sms_sign(self):
        sms_sign_id = 'f4ff88c7ccaf4ffba0c9aa149ab2aa14'
        uri = '/v2/{project_id}/notifications/sms_sign/' + sms_sign_id
        deleteSignReq = DeleteSmsSign()
        deleteSignReq.set_sms_sign_id(sms_sign_id)
        self.assertEqual(uri, deleteSignReq.get_uri(), "not equal")
        
    def test_ListSmsMsgReport(self):
        sms_sign_id = 'f4ff88c7ccaf4ffba0c9aa149ab2aa14'        
        end_time = time.time() * 1000
        start_time = end_time - 24 * 3600 * 1000
        mobile = 12888888888
        status_success = 1
        offset = 0
        limit = 33
        uri = '/v2/{project_id}/notifications/sms/report?status=' + str(status_success) + '&mobile=' + str(mobile) + \
        '&start_time=' + str("%.f"%start_time) + '&limit=' + str(limit) +\
        '&end_time=' + str("%.f"%end_time) + '&offset=' + str(offset) + \
        '&sign_id=' + str(sms_sign_id) + '&'

        listReportReq = ListSmsMsgReport()
        listReportReq.set_start_time(start_time)
        listReportReq.set_end_time(end_time)
        listReportReq.set_sign_id(sms_sign_id)
        listReportReq.set_query_mobile(mobile)
        listReportReq.set_query_sms_status(status_success)
        listReportReq.set_offset(offset)
        listReportReq.set_limit(limit)
        self.assertEqual(uri, listReportReq.get_uri(), "not equal")
        
    def test_GetSmsMessage(self):
        message_id = 'f4ff88c7ccaf4ffba0c9aa149ab2aa15'
        uri = '/v2/{project_id}/notifications/sms/message/' + message_id
        getSmsMessageReq = GetSmsMessage()
        getSmsMessageReq.set_message_id(message_id)
        self.assertEqual(uri, getSmsMessageReq.get_uri(), "not equal")
        
    def test_ListSmsEvent(self):
        uri = '/v2/{project_id}/notifications/sms/callback'
        listSmsEventReq = ListSmsEvent()
        self.assertEqual(uri, listSmsEventReq.get_uri(), "not equal")
        listSmsEventReq

    def test_UpdateSmsEvent(self):
        uri = '/v2/{project_id}/notifications/sms/callback'
        urn_fail = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk1'
        urn_success = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk2'
        urn_repy = 'urn:smn:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:python-sdk3'
        event_fail = {}
        event_success = {}
        event_reply = {}
        event_fail['event_type'] = "sms_fail_event"
        event_fail['topic_urn'] = urn_fail
        event_success['event_type'] = "sms_success_event"
        event_success['topic_urn'] = urn_success
        event_reply['event_type'] = "sms_reply_event"
        event_reply['topic_urn'] = urn_repy
        
        callback1 = {"callback": [event_fail]}
        callback2 = {"callback": [event_reply, event_fail, event_success]}

        updateSmsEventReq = UpdateSmsEvent()
        updateSmsEventReq.set_sms_fail_event(urn_fail)
        self.assertDictEqual(callback1, updateSmsEventReq.get_request_body_param(), "not equal")
        
        updateSmsEventReq.set_sms_reply_event(urn_repy)
        updateSmsEventReq.set_sms_success_event(urn_success)
        self.assertDictEqual(callback2, updateSmsEventReq.get_request_body_param(), "not equal")


        
        
        