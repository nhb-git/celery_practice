#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/1/2020  5:59 PM 
# 文件名称   ：config.py


BROKER_URL = 'redis://192.168.137.131:6379/11'
CELERY_RESULT_BACKEND = 'redis://192.168.137.131:6379/12'
CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']
