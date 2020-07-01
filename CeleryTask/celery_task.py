#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/30/2020  10:30 PM 
# 文件名称   ：celery_task.py


import time
import celery


backend = 'redis://192.168.137.131:6379/1'
broker = 'redis://192.168.137.131:6379/2'
cel = celery.Celery('test', backend=backend, broker=broker)


@cel.task
def send_mail(name):
    print('向%s发送邮件' % name)
    time.sleep(5)
    print('向%s发送邮件完成' % name)
    return 'ok'


@cel.task
def send_msg(name):
    print('向%s发送短信' % name)
    time.sleep(5)
    print('向%s发送短信完成' % name)
    return 'ok'
