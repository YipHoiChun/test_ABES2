import tkinter as tk
import tkinter.messagebox as msg
import pymysql
import initial
import manager
import borrower
import m_operation
import b_operation


def id_check(a):
    global id
    if a == '1':
        id = manager.entry_name.get()
        password = manager.entry_key.get()
    else:
        id = borrower.entry_name.get()
        password = borrower.entry_key.get()
    getid()
    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='cla051063',
                         db='abes',
                         charset='utf8'
                         )
    cursor = db.cursor()
    sql = "SELECT password FROM user WHERE id='%s' AND job='%s'" % (id, a)
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        if password == result[0]:
            success_login(a)
        else:
            msg._show(title='error！', message='Wrong account or password input!')
    else:
        msg._show(title='error！', message='The user you entered does not exist! Please register first!')
        if a == '1':
            manager.root1.destroy()
        elif a == '0':
            borrower.root1.destroy()
    db.close()  #


def success_login(a):
    if a == '1':
        manager.root1.destroy()
        m_operation.frame()
    elif a == '0':
        borrower.root1.destroy()
        b_operation.frame()


def id_write(a):
    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='cla051063',
                         db='abes',
                         charset='utf8'
                         )
    cursor = db.cursor()
    if a == '1':
        id = manager.entry_name.get()
        password = manager.entry_key.get()
        confirm = manager.entry_confirm.get()
    elif a == '0':
        id = borrower.entry_name.get()
        password = borrower.entry_key.get()
        confirm = borrower.entry_confirm.get()

    sql0 = "SELECT id FROM user WHERE id='%s' AND job='%s'" % (id, a)
    sql1 = "INSERT INTO user VALUES(%s,%s,%s) " % (id, password, a)
    if password == confirm:
        cursor.execute(sql0)
        result = cursor.fetchone()
        if result:
            msg.showerror(title='error！', message='This account has been registered, please re-enter!')
        else:
            cursor.execute(sql1)
            db.commit()
            db.close()
            msg.showinfo(title='Success！', message='Register successfully, please login!')

    else:
        msg.showerror(title='error！', message='Two times the password does not match, please re-enter!')


def getid():
    return id
