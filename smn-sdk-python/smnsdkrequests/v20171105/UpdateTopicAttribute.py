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

from smnsdkcore.exception.exceptions import SMNException
from smnsdkcore.request import CommonRequest
from smnsdkcore.http import httpmethod
from copy import deepcopy
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class UpdateTopicAccessPolicy(CommonRequest):
    def __init__(self):
        super(UpdateTopicAccessPolicy, self).__init__()
        self.set_method(httpmethod.PUT)
    
    def set_topic_urn(self, topic_urn):
        uri = '/v2/{project_id}/notifications/topics/' + topic_urn + '/attributes/access_policy'
        self.set_uri(uri)
    
    def set_topic_policy(self,policy):
        self.add_request_body_param("value", policy)
        
    def get_topic_policy(self):
        self.get_request_body_param().get("value")

class SimpleConfigTopicPolicy(UpdateTopicAccessPolicy):
    def __init__(self):
        super(SimpleConfigTopicPolicy, self).__init__()
        self.__policy_map = {"Version": "2016-09-07","Id": "__default_policy_ID"}
        
        self.__user_statement = {"Sid": "__user_pub_0","Effect": "Allow", "Principal": None, \
                          "Action": ["SMN:Publish"], "Resource": None}
        self.__service_statement = {"Sid": "__service_pub_0", "Effect": "Allow", "Principal": None, \
                             "Action": ["SMN:Publish", "SMN:QueryTopicDetail"], \
                             "Resource": None}
        self.__policy_map["Statement"] = []

        self.__csp_to_domainids = []
        self.__csp_to_services = []
        self.__topic_urn = None
        
    
    def set_topic_urn(self, topic_urn):
        super(SimpleConfigTopicPolicy, self).set_topic_urn(topic_urn)
        self.__topic_urn = topic_urn;

    def authrize_to_users(self, domain_id_list):
        if type(domain_id_list) != list:
            raise SMNException("param", "domain_id_list must be list")
        
        if self.__csp_to_domainids is None:
            pass
        else:
            self.__csp_to_domainids = self.__csp_to_domainids + ['urn:csp:iam::' + domain_id + ':root' for domain_id in domain_id_list]
    
    def authrize_to_services(self, services_list):
        if type(services_list) != list:
            raise SMNException("param", "services_list must be list")
        self.__csp_to_services = self.__csp_to_services + [service for service in services_list]
    
    def authrize_to_all_users(self):
        self.__csp_to_domainids = "*"
    
    def get_request_body_param(self):
        request = UpdateTopicAccessPolicy.get_request_body_param(self)
        
        if request:
            return request
        
        return self._get_request_body_param()
    
    def _get_request_body_param(self):
        if not self.__topic_urn:
            raise SMNException("param", "topic_urn is None")
        if not (self.__csp_to_domainids or self.__csp_to_services):
            raise SMNException("param", "both domain_id and servcie is None")
        
        policy_map = deepcopy(self.__policy_map)
        user_statement = deepcopy(self.__user_statement)
        service_statement = deepcopy(self.__service_statement)
        
        if self.__csp_to_domainids == "*":
            user_principal = {"CSP": "*"}
            user_statement["Principal"] = user_principal
            user_statement["Resource"] = self.__topic_urn
            policy_map["Statement"].append(user_statement)
        elif self.__csp_to_domainids:
            user_principal = {"CSP": self.__csp_to_domainids}
            user_statement["Principal"] = user_principal
            user_statement["Resource"] = self.__topic_urn
            policy_map["Statement"].append(user_statement)
        else:
            pass
        
        if self.__csp_to_services:
            service_principal = {"Service": self.__csp_to_services}
            service_statement["Principal"] = service_principal
            service_statement["Resource"] = self.__topic_urn
            policy_map["Statement"].append(service_statement)
        
        return {"value": json.dumps(policy_map)}

class UpdateTopicIntroduction(CommonRequest):
    def __init__(self):
        super(UpdateTopicIntroduction, self).__init__()
        self.set_method(httpmethod.PUT)
    
    def set_topic_urn(self, topic_urn):
        uri = '/v2/{project_id}/notifications/topics/' + topic_urn + '/attributes/introduction'
        self.set_uri(uri)
    
    def set_introduction(self, introduction):
        self.add_request_body_param('value', introduction)
    
    def get_introduction(self):
        return self.get_request_body_param().get('value')
    
class UpdateTopicSmsSignId(CommonRequest):
    def __init__(self):
        super(UpdateTopicSmsSignId, self).__init__()
        self.set_method(httpmethod.PUT)
    
    def set_topic_urn(self, topic_urn):
        uri = '/v2/{project_id}/notifications/topics/' + topic_urn + '/attributes/sms_sign_id'
        self.set_uri(uri)
    
    def set_sms_sign_id(self, sms_sign_id):
        self.add_request_body_param('value', sms_sign_id)
    
    def get_sms_sign_id(self):
        return self.get_request_body_param().get('value')