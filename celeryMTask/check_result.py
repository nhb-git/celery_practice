#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/1/2020  9:44 AM 
# 文件名称   ：check_result.py
from celery.result import AsyncResult
from celery_tasks.celery import cel


async_result = AsyncResult(id='9b8612fa-ae61-4776-aadd-2bcbea49b70e', app=cel)

if async_result.successful():
    result = async_result.get()
    print(result)
elif async_result.failed():
    print('执行失败')
elif async_result.status == 'PENDING':
    print('等待任务执行')
elif async_result.status == 'RETRY':
    print('任务异常后正在重试')
elif async_result.status == 'STARTED':
    print('任务已经开始被执行')
