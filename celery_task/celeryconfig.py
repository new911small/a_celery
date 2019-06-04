from __future__ import absolute_import # 拒绝隐式引入，因为celery.py的名字和celery的包名冲突，需要使用这条语句让程序正确地运行
from celery.schedules import crontab


broker_url = "redis://@localhost:6379/5"   # 使用redis存储任务队列
# result_backend = "redis://:crawler@localhost:6379/6"  # 使用redis存储结果

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = "Asia/Shanghai"  # 时区设置
worker_hijack_root_logger = False  # celery默认开启自己的日志，可关闭自定义日志，不关闭自定义日志输出为空
result_expires = 60 * 60 * 24  # 存储结果过期时间（默认1天）

# 导入任务所在文件
imports = [
    "celery_task.epp_scripts.get_data",  # 导入py文件
]


# 需要执行任务的配置
beat_schedule = {
    "test1": {
        "task": "celery_task.epp_scripts.get_data.celery_run",  #执行的函数
        "schedule": crontab(minute="*/5"),   # every minute 每分钟执行
        "args": ()  # # 任务函数参数
    },

}