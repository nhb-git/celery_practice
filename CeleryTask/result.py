#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/30/2020  11:25 PM 
# 文件名称   ：result.py
from celery.result import AsyncResult
from celery_task import cel


async_result = AsyncResult(id='8628904d-e02a-473f-966e-9eca4286ba4d', app=cel)

if async_result.successful():
    result = async_result.get()
    print(result)
elif async_result.failed():
    print('failed')
elif async_result.status == 'PENDING':
    print('PENDING')
else:
    print('other')
