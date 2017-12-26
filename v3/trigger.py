#! /usr/bin/env python
# coding=utf-8
# --------------------------
# @Time    : 17-12-26 下午2:32
# @Author  : knight
# @File    : trigger.py
# --------------------------
from tasks import add
import time

result = add.delay(4, 4)

while not result.ready():
    time.sleep(1)
print 'task done: {0}'.format(result.get())