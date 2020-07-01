#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/30/2020  10:47 PM 
# 文件名称   ：produce_task.py


from celery_task import send_mail, send_msg


result = send_mail.delay('niu')
print(result.id)


result = send_msg.delay('niu')
print(result.id)
