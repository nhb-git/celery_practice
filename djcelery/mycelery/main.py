#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/1/2020  6:03 PM 
# 文件名称   ：main.py
import os
from celery import Celery


# 创建celery实例
app = Celery('djcelery')

# celery和django结合，识别和加载django的配置文件
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djcelery.settings')

# 加载celery本身的配置文件
app.config_from_object('mycelery.config')

# 自动扫描任务
app.autodiscover_tasks(['mycelery.sms',])
