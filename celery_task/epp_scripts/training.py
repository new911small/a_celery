# _*_ coding:utf-8 _*_
# from celery_task.celery import app
import random
import requests
# import ssl
import re
import datetime
# import pymongo
import time
from xml.etree.ElementTree import fromstring, ElementTree

from celery_task.sql_connect import connect_sql



def get_training(kkk):
    headers1 = {
        'Authorization': 'Basic d2VibWFzdGVyQGdlbnNlZS5jb206cXdlcjEyMzRAZ2Vuc2VlLmNvbQ==',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    }

    count_list = ['22', '41', '71']
    servicetype = '1'
    cursor, connect=connect_sql()
    for g in count_list:

        postdata5 = {'albId': g, 'servicetype': servicetype}

        randoms = str(random.random())
        url5 = 'http://opsys.gensee.com/opsys/site/cmd/conflist?random=' + randoms
        # 直播第一次响应
        rep5 = kkk.post(url=url5, headers=headers1, data=postdata5, verify=False)
        content_5 = rep5.content.decode()

        body = re.findall(r'{"content":"(.*)",', content_5, re.M)
        if body:
            body = body[0]
            body = body.replace('\\', '')

            list888 = body.split('conf ')
        #
            list999 = (list888[1:])

            if len(list999) == 0:
                pass
            for i in list999:

                m = re.findall(r'(?<==").+?(?=")', i)
                m[1] = ""
                num = len(m)
                list2 = m[:10]

                if num==10:
                    pass

                elif num > 14:
                    n = int((num - 10) / 4)
                    nn = 10
                    for i in range(n):
                        str1 = 'list'
                        mk = str(i)
                        q = mk + str1
                        q = list2
                        ff = q + m[nn:nn + 4]
                        nn = nn + 4
                        print(ff)
                        if g == '22':
                            sql1="insert into training3(server_id,name,site,status,web,client,type,ip,total,IDCID,typetwo,iptwo,totaltwo,IDCIDtwo)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            cursor.execute(sql1, ff)
                            connect.commit()
                        elif g == '41':
                            sql1="insert into training4(server_id,name,site,status,web,client,type,ip,total,IDCID,typetwo,iptwo,totaltwo,IDCIDtwo)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            cursor.execute(sql1, ff)
                            connect.commit()
                        elif g == '71':
                            sql1="insert into training5(server_id,name,site,status,web,client,type,ip,total,IDCID,typetwo,iptwo,totaltwo,IDCIDtwo)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            cursor.execute(sql1, ff)
                            connect.commit()
                else:

                    if g == '22':
                        sql1 = "insert into training3(server_id,name,site,status,web,client,type,ip,total,IDCID,typetwo,iptwo,totaltwo,IDCIDtwo)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        cursor.execute(sql1, m)
                        connect.commit()
                    elif g == '41':
                        sql1 = "insert into training4(server_id,name,site,status,web,client,type,ip,total,IDCID,typetwo,iptwo,totaltwo,IDCIDtwo)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        cursor.execute(sql1, m)
                        connect.commit()
                    elif g == '71':
                        sql1 = "insert into training5(server_id,name,site,status,web,client,type,ip,total,IDCID,typetwo,iptwo,totaltwo,IDCIDtwo)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        cursor.execute(sql1, m)
                        connect.commit()





if __name__ == '__main__':
    # celery_run()
    get_training()
