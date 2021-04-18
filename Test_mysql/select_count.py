import pymysql


def select_count():
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
        sql = "SELECT COUNT(*) FROM book WHERE name='%s' AND userid='%s'" % ('iPhone', '111')
        cursor.execute(sql)
        print(cursor.fetchone())
        db.commit()
    finally:
        cursor.close()
        db.close()

    # sql3 = "SELECT COUNT(*) FROM book WHERE name='%s' AND userid='%s'" % (e_name.get(), ID.getid())
    # cursor.execute(sql3)
    # result3 = cursor.fetchone()
    # if result3 >= '1':
    #     sql4 = "UPDATE equipment SET amount=amount+1 WHERE name='%s'" % (e_name.get())
    #     cursor.execute(sql4)
    #     sql5 = "DELETE FROM book WHERE name='%s' AND userid='%s'" % (e_name.get(), ID.getid())
    #     cursor.execute(sql5)
    #     print("delete book")


if __name__ == '__main__':
    select_count()
