#!/usr/bin/python
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

from setuptools import setup, find_packages
import os

PACKAGE = "smnsdkcore"
NAME = "smn-sdk-python"
DESCRIPTION = "This is HuaweiCloud SMN(Simple Message Notification) Service Python SDK."
AUTHOR = "HuaweiCloud"
AUTHOR_EMAIL = "smndeveloper@huawei.com"
URL = "http://developer.huaweicloud.com/dev/sdk"

TOPDIR = os.path.dirname(__file__) or "."
VERSION = __import__(PACKAGE).__version__

desc_file = open("README.md")
try:
    LONG_DESCRIPTION = desc_file.read()
finally:
    desc_file.close()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache",
    url=URL,
    keywords=["smn", "sdk", "HuaweiCloud"],
    packages=find_packages(),
    include_package_data=True,
    python_requires='<3',
    platforms='any',
    install_requires=[
        'pycrypto>=2.6.1'
    ],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
    )
)