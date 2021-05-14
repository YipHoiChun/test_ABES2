import pymysql


def update():
    try:
        db = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             passwd='cla051063',
                             db='abes',
                             charset='utf8'
                             )
    except:
        print('Failed to connect to mysql database')
    else:
        cursor = db.cursor()
        sql = "UPDATE equipment SET amount=amount-1 WHERE name='%s'" % ('iPhone')
        cursor.execute(sql)
        db.commit()
    finally:
        cursor.close()


if __name__ == '__main__':
    update()
