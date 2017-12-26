#! /usr/bin/env python
# coding=utf-8
# --------------------------
# @Time    : 17-12-26 下午2:28
# @Author  : knight
# @File    : tasks.py
# --------------------------

from celery.utils.log import get_task_logger
from celery import Celery

logger = get_task_logger(__name__)

app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')  # 配置好celery的backend和broker


@app.task(bind=True)
def add(self, x, y):
    logger.info(self.request.__dict__)
    return x + y