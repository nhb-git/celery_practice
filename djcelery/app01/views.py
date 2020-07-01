from datetime import datetime, timedelta
from django.shortcuts import render, HttpResponse
from mycelery.sms.tasks import send_sms


def test(request):
    # 定时任务
    # now_time = datetime.now()
    # utc_now_time = datetime.utcfromtimestamp(now_time.timestamp())
    # time_delay = timedelta(seconds=10)
    # task_time = utc_now_time + time_delay
    # result = send_sms.apply_async(['niu',], eta=task_time)

    # 异步任务
    send_sms.delay('niu')
    send_sms.delay('haibao')
    send_sms.delay('niu')
    send_sms.delay('haibao')
    send_sms.delay('niu')
    send_sms.delay('haibao')
    send_sms.delay('niu')
    send_sms.delay('haibao')
    return HttpResponse(400)
