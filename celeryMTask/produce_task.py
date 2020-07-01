#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/1/2020  9:40 AM 
# 文件名称   ：produce_task.py
from celery_tasks.task01 import send_mail
from celery_tasks.task02 import send_msg


result = send_mail.delay('邮件1')
print(result.id)

result = send_msg.delay('短信1')
print(result.id)
