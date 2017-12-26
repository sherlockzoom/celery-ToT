#! /usr/bin/env python
# coding=utf-8
# --------------------------
# @Time    : 17-12-26 下午2:18
# @Author  : knight
# @File    : tasks.py
# --------------------------
from celery import Task

from celery import Celery

app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')  # 配置好celery的backend和broker


class MyTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('task done: {0}'.format(retval))  # 简单打印信息，这里可以按照需求进行修改
        return super(MyTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('task fail, reason: {0}'.format(exc))
        return super(MyTask, self).on_failure(exc, task_id, args, kwargs, einfo)


@app.task(base=MyTask)  # 利用装饰器 使用执行自定义task
def add(x, y):
    raise ValueError
    return x+y
