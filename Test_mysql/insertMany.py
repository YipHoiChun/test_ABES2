import pymysql


def insert_Many():
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
        sql = "INSERT INTO book VALUES('%s','%s','%s')" % (333, 'iPhone', '2021-04-01 00:00:00')
        cursor.execute(sql)
        db.commit()
    finally:
        cursor.close()
        db.close()


if __name__ == '__main__':
    insert_Many()
