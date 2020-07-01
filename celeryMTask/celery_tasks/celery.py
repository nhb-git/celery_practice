#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/1/2020  9:20 AM 
# 文件名称   ：celery.py
from datetime import timedelta
from celery import Celery


broker = 'redis://192.168.137.131:6379/1'
backend = 'redis://192.168.137.131:6379/2'

cel = Celery('celery_demo', broker=broker, backend=backend,
             include=[
                 'celery_tasks.task01',
                 'celery_tasks.task02',
             ])

# 时区
cel.conf.timezone = 'Asia/Shanghai'

# 定时任务配置
cel.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'celery_tasks.task01.send_mail',
        # 'schedule': timedelta(seconds=10),
        'schedule': 6,
        'args': ('niu',)
    },
}
