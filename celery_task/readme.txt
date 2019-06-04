https://blog.csdn.net/Shyllin/article/details/80940643

1，celery -A celery_task beat（在celery_task同级目录下执行）
2，celery -A celery_task worker --loglevel=info -P eventlet（ 在celery_task同级目录下执行）
celery -A celery_task worker --loglevel=info -P solo
1,2在不同终端下执行。




