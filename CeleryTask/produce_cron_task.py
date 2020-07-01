#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/1/2020  11:53 AM 
# 文件名称   ：produce_cron_task.py
from datetime import datetime
from celery_task import send_mail


exec_datetime = datetime(2020, 7, 1, 12, 00, 00)
print(exec_datetime)
utc_exec_datetime = datetime.utcfromtimestamp(exec_datetime.timestamp())
print(utc_exec_datetime)

result = send_mail.apply_async(args=('email1',), eta=utc_exec_datetime)
print(result.id)
