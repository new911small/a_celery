import pymysql

def connect_sql():
    try:
        connect = pymysql.connect(
            host='192.168.1.118',
            port=3306,
            user='root',
            password='root',
            db='new_database'
        )

        cursor = connect.cursor()
    except Exception as e:
        print(str(e))

    return cursor,connect

