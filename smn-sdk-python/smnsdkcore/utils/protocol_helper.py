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
SMN Subscribe protocol helper
create at 2017/11/4
"""
__author__ = 'pengzl'

import re

SUBSCRIBE_PROTOCOL = {"sms":"sms", "email":"email", "http":"http", "https":"https", \
                      "functionstage":"functionstage", "functiongraph":"functiongraph", \
                      "dms":"dms"}


match_telephone = re.compile('^\+?[0-9]+$')
match_email = re.compile('^[a-zA-Z0-9]+([._\-]*[a-zA-Z0-9])*@([a-zA-Z0-9]+[-a-zA-Z0-9]*[a-zA-Z0-9]+.){1,63}[a-zA-Z0-9]+$')
match_http = re.compile('^http://.*')
match_https = re.compile('^https://.*')
match_functionstage = re.compile('^urn:fss:[\w:-]+$')
match_functiongraph = re.compile('^urn:fgs:[\w:-]+$')
match_dms = re.compile('\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')

def get_protocol_type(endpoint):
    if match_telephone.match(endpoint):
        return SUBSCRIBE_PROTOCOL['sms']
    if match_email.match(endpoint):
        return SUBSCRIBE_PROTOCOL['email']
    if match_http.match(endpoint):
        return SUBSCRIBE_PROTOCOL['http']
    if match_https.match(endpoint):
        return SUBSCRIBE_PROTOCOL['https']
    if match_functionstage.match(endpoint):
        return SUBSCRIBE_PROTOCOL['functionstage']
    if match_functiongraph.match(endpoint):
        return SUBSCRIBE_PROTOCOL['functiongraph']
    if match_dms.match(endpoint):
        return SUBSCRIBE_PROTOCOL['dms']

def valid_protocol(protocol):
    if SUBSCRIBE_PROTOCOL.__contains__(protocol):
        return True
    return False

if __name__ == "__main__":
    phone = "+86188888"
    print get_protocol_type(phone)
    email = "x_djf@dd.c"
    print get_protocol_type(email)
    http = "http://forum.huaweicloud.com/forum.php?mod=forumdisplay&fid=625&page=1"
    print get_protocol_type(http)
    https = "https://github.com/marketplace1"
    print get_protocol_type(https)
    functionstage = "urn:fss:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:function:default:peng:latest"
    print get_protocol_type(functionstage)
    functiongraph = "urn:fgs:cn-north-1:3bf82e180e3742b8ac3019e9c2ef7095:graph:workflow-peng"
    print get_protocol_type(functiongraph)
    dms = "b8a2f8ef-3a7a-4a9c-bed8-fef8cefcd78c"
    print get_protocol_type(dms)
    
    print valid_protocol('sms')
    print valid_protocol('ddd')
    
    