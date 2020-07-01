#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/1/2020  9:20 AM 
# 文件名称   ：task01.py
import time
from celery_tasks.celery import cel


@cel.task
def send_mail(msg):
    print('开始发送邮件%s' % msg)
    time.sleep(5)
    print('邮件发送完成')
    return 'ok'
