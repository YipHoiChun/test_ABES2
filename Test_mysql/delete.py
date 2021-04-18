import pymysql


def delete_all():
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
        sql = "TRUNCATE TABLE book"
        cursor.execute(sql)
        db.commit()
        print('Delete all book')
    finally:
        cursor.close()
        db.close()


if __name__ == '__main__':
    delete_all()