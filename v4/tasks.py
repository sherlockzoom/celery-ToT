#! /usr/bin/env python
# coding=utf-8
# --------------------------
# @Time    : 17-12-26 下午2:39
# @Author  : knight
# @File    : tasks.py
# --------------------------
from celery import Celery
import time

app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')  # 配置好celery的backend和broker


@app.task(bind=True)
def test_mes(self):
    for i in xrange(1, 11):
        time.sleep(0.1)
        self.update_state(state="PROGRESS", meta={'p': i*10})
    return 'finish'


@app.task(bind=True)
def add(self, x, y):
    return x + y