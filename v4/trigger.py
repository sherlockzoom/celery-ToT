#! /usr/bin/env python
# coding=utf-8
# --------------------------
# @Time    : 17-12-26 下午2:41
# @Author  : knight
# @File    : trigger.py
# --------------------------

from tasks import add, test_mes
import sys


def pm(body):
    res = body.get('result')
    if body.get('status') == 'PROGRESS':
        sys.stdout.write('\r任务进度: {0}%'.format(res.get('p')))  # 进度条
        sys.stdout.flush()
    else:
        print '\r'
        print res


r = test_mes.delay()
print r.get(on_message=pm, propagate=False)