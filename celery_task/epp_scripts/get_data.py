# _*_ coding:utf-8 _*_
from celery_task.celery import app
# import sys
# sys.path.append(r'D:\a_celery')
from celery_task.epp_scripts.webcast import get_webcast
from celery_task.epp_scripts.meeting import get_meeting
from celery_task.epp_scripts.servers import get_servers
from celery_task.epp_scripts.training import get_training

import requests
# import ssl
# import pymongo


# ssl._create_default_https_context = ssl._create_unverified_context
# def get_db():
#     try:
#         #  连接数据库
#         client = pymongo.MongoClient('127.0.0.1', 27017)
#         db = client.copyright  # 连接要查询的数据库
#     except Exception as e:
#         print(str(e))
#
#     data = db.data
#
#     return data


def get_data():


    res = requests.session()

    # 登录 发起两次post请求（连续两次账号密码登录）
    url1 = 'http://opsys.gensee.com/opsys/site/check'
    headers1 = {
        'Authorization': 'Basic d2VibWFzdGVyQGdlbnNlZS5jb206cXdlcjEyMzRAZ2Vuc2VlLmNvbQ==',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    }
    postdata1 = {
        'loginName': 'webmaster@gensee.com',
        'password': 'qwer1234@gensee.com'
    }

    rep1 = res.post(url=url1, headers=headers1, data=postdata1)
    # print(rep1.status_code)

    postdata2 = {
        'loginName': 'biqing.liu',
        'password': 'biqing.liu!@#$%^'
    }
    rep2 = res.post(url=url1, headers=headers1, data=postdata2)

    get_webcast(res)
    get_meeting(res)
    get_servers(res)
    # get_training(res)


@app.task
def celery_run():
    get_data()

if __name__ == '__main__':

    get_data()
