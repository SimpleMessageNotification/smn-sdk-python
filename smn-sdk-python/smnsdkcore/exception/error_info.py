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


__error_dict = dict(
    SDK_AUTH_USER_PASSWORD_INVALID=['SDK_AUTH_USER_PASSWORD_INVALID', 'Domain_name or username or password is empty.'],
    )

def get_error_info(key):
    return __error_dict.get(key)


if __name__ == "__main__":
    print __error_dict