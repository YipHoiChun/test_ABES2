import pymysql


def select_one():
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
        sql = "SELECT * FROM user WHERE id='%s'" % (1234)
        cursor.execute(sql)
        print(cursor.fetchone())
        db.commit()
    finally:
        cursor.close()
        db.close()


if __name__ == '__main__':
    select_one()
