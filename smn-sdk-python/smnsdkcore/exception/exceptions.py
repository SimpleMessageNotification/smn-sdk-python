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
__author__ = 'pengzl'


class SMNException(Exception):
    def __init__(self, error_code, error_msg):
        super(SMNException, self).__init__()
        self.error_code = error_code
        self.error_msg = error_msg
        
    def __str__(self):
        return "error_code is %s ; error_msg is %s" % (self.error_code, self.error_msg)

    def set_error_code(self, code):
        self.error_code = code

    def set_error_msg(self, msg):
        self.error_msg = msg

    def get_error_code(self):
        return self.error_code

    def get_error_msg(self):
        return self.error_msg
    