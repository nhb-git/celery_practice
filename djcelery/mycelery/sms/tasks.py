#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/1/2020  5:58 PM 
# 文件名称   ：tasks.py
import time
from mycelery.main import app


@app.task
def send_sms(msg):
    print('开始向 %s 发送短信...' % msg)
    time.sleep(5)
    print('向 %s 发送短信成功' % msg)

    return 'send_sms ok'
