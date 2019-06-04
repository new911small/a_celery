# _*_ coding:utf-8 _*_
import random
import requests
# import ssl
import re
from celery_task.sql_connect import connect_sql
import datetime
# import pymongo

def get_meeting(kkk):

    cursor, connect=connect_sql()

    # res = requests.session()
    #
    # # 登录 发起两次post请求（连续两次账号密码登录）
    # url1 = 'http://opsys.gensee.com/opsys/site/check'
    headers1 = {
        'Authorization': 'Basic d2VibWFzdGVyQGdlbnNlZS5jb206cXdlcjEyMzRAZ2Vuc2VlLmNvbQ==',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    }
    # postdata1 = {
    #     'loginName': 'webmaster@gensee.com',
    #     'password': 'qwer1234@gensee.com'
    # }
    #
    # rep1 = res.post(url=url1, headers=headers1, data=postdata1)
    #
    #
    # postdata2 = {
    #     'loginName': 'biqing.liu',
    #     'password': 'biqing.liu!@#$%^'
    # }
    # rep2 = res.post(url=url1, headers=headers1, data=postdata2)

    count_list = ['22', '41', '71']
    servicetype = '3'
    #
    for g in count_list:
        # formdata
        postdata55 = {'albId': g, 'servicetype': servicetype}

        randoms = str(random.random())
        url6 = 'http://opsys.gensee.com/opsys/site/cmd/conflist?random=' + randoms
        # 直播第一次响应
        rep55 = kkk.post(url=url6, headers=headers1, data=postdata55, verify=False)
        content_55 = rep55.content.decode()

        body = re.findall(r'{"content":"(.*)",', content_55, re.M)
        if body:
            body = body[0]
            body = body.replace('\\', '')

            list888 = body.split('conf ')

            list999 = (list888[1:])
            print(list999)
            if len(list999) == 0:
                pass
            for i in list999:
                # print('========================================')
                # print(i)
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
                        if g=='22':
                            sql1="insert into meeting_data1(server_id,name,site,status,web,client,type,ip,total,IDCID,typetwo,iptwo,totaltwo,IDCIDtwo)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            cursor.execute(sql1, ff)
                            connect.commit()
                        elif g=='41':
                            sql1="insert into meeting_data2(server_id,name,site,status,web,client,type,ip,total,IDCID,typetwo,iptwo,totaltwo,IDCIDtwo)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            cursor.execute(sql1, ff)
                            connect.commit()
                        elif g=='71':
                            sql1="insert into meeting_data3(server_id,name,site,status,web,client,type,ip,total,IDCID,typetwo,iptwo,totaltwo,IDCIDtwo)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            cursor.execute(sql1, ff)
                            connect.commit()
                else:

                    if g == '22':
                        sql1 = "insert into meeting_data1(server_id,name,site,status,web,client,type,ip,total,IDCID,typetwo,iptwo,totaltwo,IDCIDtwo)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        cursor.execute(sql1, m)
                        connect.commit()
                    elif g == '41':
                        sql1 = "insert into meeting_data2(server_id,name,site,status,web,client,type,ip,total,IDCID,typetwo,iptwo,totaltwo,IDCIDtwo)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        cursor.execute(sql1, m)
                        connect.commit()
                    elif g == '71':
                        sql1 = "insert into meeting_data3(server_id,name,site,status,web,client,type,ip,total,IDCID,typetwo,iptwo,totaltwo,IDCIDtwo)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        cursor.execute(sql1, m)
                        connect.commit()

if __name__ == '__main__':
    get_meeting()