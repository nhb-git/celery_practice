#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/1/2020  9:30 AM 
# 文件名称   ：task02.py
import time
from celery_tasks.celery import cel


@cel.task
def send_msg(msg):
    print('开始发送短信%s' % msg)
    time.sleep(5)
    print('发送短信完成')
    return 'ok'
