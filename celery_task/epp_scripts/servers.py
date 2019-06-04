 # _*_ coding:utf-8 _*_
# from celery_task.celery import app
import random
import requests
# import ssl
import re
import datetime

import time
from celery_task.sql_connect import connect_sql

from xml.etree.ElementTree import fromstring, ElementTree



def get_servers(kkk):

    #
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
    # # print(rep1.status_code)
    #
    # postdata2 = {
    #     'loginName': 'biqing.liu',
    #     'password': 'biqing.liu!@#$%^'
    # }
    # rep2 = res.post(url=url1, headers=headers1, data=postdata2)
    # print(rep2.status_code)


    # 第三次请求拿到数据 服务器管理，服务器信息

    # 数据列表id

    # id 22 4.5.4 alb
    # id 41 4.6 alb
    # id 71 aray-test alb

    cursor, connect = connect_sql()

    count_list = ['22','41','71']
    f = 'servertable'

    for g in count_list:
        postdata3 = {'id': g}
        randoms = str(random.random())
        url3 = 'http://opsys.gensee.com/opsys/site/cmd/svrlist?random=' + randoms
        rep3 = kkk.post(url=url3, headers=headers1, data=postdata3,verify=False)
        content = rep3.content.decode()
        # print(content)
        list1 = content.split('><svr ')
        list2 = list1[1:]
        print(list2)
        for i in list2:
            m = re.findall(r'(?<==\\").+?(?=\\")', i)
            # print(m)
            list3 = m[1].split('://')
            str11 = list3[1]
            list5 = str11.split(':')
            # print(list5)
            del m[1]
            # print(m)
            m.insert(0,list5[0])
            m.insert(2,list5[1])
            del m[9]
            print(m)
            if g == '22':
                sql1 = "insert into server_data30(name,idP,port,status,maxCurrent,current,IDC,site,version)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql1, m)
                connect.commit()
            elif g == '41':
                sql1 = "insert into server_data31(name,idP,port,status,maxCurrent,current,IDC,site,version)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql1, m)
                connect.commit()
            elif g == '71':
                sql1 = "insert into server_data33(name,idP,port,status,maxCurrent,current,IDC,site,version)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql1, m)
                connect.commit()


        # c = ''.join(l1)
        # print(c)
        # nodes = re.findall(r'<svr (.*?) />?', content, re.M)
        # print(nodes)
        # if nodes:
        #     for i in nodes:
        #         # print(i)
        #         list1=[]
        #         name = re.findall(r'url=\\".*?//(.*?):\d*\\" ', i, re.M)
        #         if name:
        #             name = name[0]
        #         else:
        #             name = ''
        #
        #         # typesss = 'Server'
        #         list1.append(name)
        #         # list1.append(typesss)
        #
        #         idP = re.findall(r'id=\\"(.*?)\\"', i, re.M)
        #         if idP:
        #             idP = idP[0]
        #         else:
        #             idP = ''
        #         list1.append(idP)
        #         status = re.findall(r'status=\\"(.*?)\\"', i, re.M)
        #         if status:
        #             status = status[0]
        #         else:
        #             status = ''
        #         list1.append(status)
        #         ip = name
        #         list1.append(ip)
        #         port = re.findall(r'url=\\".*?:.*?:(.*?)\\"', i, re.M)
        #         if port:
        #             port = port[0]
        #         else:
        #             port = ''
        #
        #         list1.append(port)
        #
        #         maxCurrent = re.findall(r'maxcapacity=\\"(.*?)\\"', i, re.M)
        #         if maxCurrent:
        #             maxCurrent = maxCurrent[0]
        #         else:
        #             maxCurrent = ''
        #         list1.append(maxCurrent)
        #
        #         current = re.findall(r'currentcapacity=\\"(.*?)\\"', i, re.M)
        #         if current:
        #             current = current[0]
        #         else:
        #             current = ''
        #         list1.append(current)
        #
        #         IDC = re.findall(r'idcid=\\"(.*?)\\"', i, re.M)
        #         if IDC:
        #             IDC = IDC[0]
        #         else:
        #             IDC = ''
        #         list1.append(IDC)
        #
        #         site = re.findall(r'belongsiteid=\\"(.*?)\\"', i, re.M)
        #         if site:
        #             site = site[0]
        #         else:
        #             site = ''
        #
        #         list1.append(site)
        #
        #         server = re.findall(r'proxy=\\"(.*?)\\"', i, re.M)
        #         if server:
        #             server = server[0]
        #         else:
        #             server = ''
        #         list1.append(server)
        #
        #         version = re.findall(r'ver=\\"(.*?)\\"', i, re.M)
        #         if version:
        #             version = version[0]
        #         else:
        #             version = ''
        #         list1.append(version)
        #         # note 备注 目前没有数据
        #         note = re.findall(r'note=\\"(.*?)\\"', i, re.M)
        #         if note:
        #             note = note[0]
        #         else:
        #             note = ''
        #
        #         list1.append(note)

                # print(name,types,idP,status,ip,port,maxCurrent,current,IDC,site,server,version,note)
                # print(version)
                # print(list1)
                # if g == '22':
                #     sql2 = "insert into training3(name,types,idP,status,ip,port,maxCurrent,current,IDC,site,server,version,note)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                #     sql1 = "insert into training3(name,idP,status,ip,port,maxCurrent,current,IDC,site,server,version,note)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                #     cursor.execute(sql1, list1)
                #     connect.commit()
                # elif g == '41':
                #     sql1 = "insert into training3(name,types,idP,status,ip,port,maxCurrent,current,IDC,site,server,version,note)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                #     cursor.execute(sql1, list1)
                #     connect.commit()
                # elif g == '71':
                #     sql1 = "insert into training3(name,types,idP,status,ip,port,maxCurrent,current,IDC,site,server,version,note)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                #     cursor.execute(sql1, list1)
                #     connect.commit()




    print(111)



if __name__ == '__main__':
    get_servers()