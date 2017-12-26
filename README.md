celery
---
# install

`$ pip install Celery`

# run

+  定义task，然后使用下面命令启动

`celery -A tasks worker --loglevel=info`

+ 定义trigger 