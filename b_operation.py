import tkinter as tk
import tkinter.messagebox as msg
from tkinter import ttk
import search
import ID
import datetime as dt  # datetime
import pymysql
import cv2
from pyzbar import pyzbar


def frame():
    global window2
    window2 = tk.Tk()
    window2.title('Borrower')
    window2.geometry('700x600')
    lable0 = tk.Label(window2, text=ID.getid(), bg='pink', font=('Microsoft YaHei', 50)).pack()  # 上

    lable1 = tk.Label(window2, text='Please select the operation:', font=('Microsoft YaHei', 20)).place(x=80,
                                                                                                        y=400)  # 下
    tk.Button(window2, text='Borrow', font=('Microsoft YaHei', 15), width=10, height=2, command=borrow).place(x=350,
                                                                                                              y=250)
    tk.Button(window2, text='Return', font=('Microsoft YaHei', 15), width=10, height=2, command=turnback).place(x=350,
                                                                                                                y=350)
    tk.Button(window2, text='Search', font=('Microsoft YaHei', 15), width=10, height=2, command=search.frame).place(
        x=350, y=450)

    tk.Button(window2, text='QR code', font=('Microsoft YaHei', 15), width=10, height=2, command=scan).place(x=350,
                                                                                                             y=550)
    tk.Button(window2, text='QR(Load)', font=('Microsoft YaHei', 15), width=10, height=2, command=qrcode_show).place(
        x=500, y=550)

    window2.mainloop()


def borrow():
    global win
    win = tk.Tk()
    win.title('Borrower')
    win.geometry('900x300')
    win.wm_attributes('-topmost', 1)
    lable1 = tk.Label(win, text='Please fill in the information of the borrowed equipment:', bg='pink',
                      font=('Microsoft YaHei', 20)).place(x=30, y=100)
    lable2 = tk.Label(win, text='(The equipment name should be filled in correctly!)', bg='pink',
                      font=('Microsoft YaHei', 20)).place(x=30, y=140)

    global e_name
    tk.Label(win, text='Equipment Name：', font=('Microsoft YaHei', 12)).place(x=140, y=200)
    e_name = tk.Entry(win, font=('Microsoft YaHei', 12), width=10)
    e_name.place(x=250, y=200)

    tk.Button(win, text='Confirm Borrow', font=('Microsoft YaHei', 12), width=10, command=confirm_borrow).place(x=600,
                                                                                                                y=195)


def confirm_borrow():
    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='cla051063',
                         db='abes',
                         charset='utf8'
                         )
    cursor = db.cursor()
    sql3 = "SELECT COUNT(*) FROM book WHERE userid='%s' AND name='%s'" % (ID.getid(), e_name.get())
    cursor.execute(sql3)
    result3 = cursor.fetchone()
    print(result3)
    if result3 == 0:
        sql = "SELECT name FROM borrow WHERE userid='%s' AND name='%s'" % (ID.getid(), e_name.get())
        cursor.execute(sql)
        result2 = cursor.fetchone()
        if result2 is None:
            sql0 = "SELECT amount FROM equipment WHERE name='%s'" % (e_name.get())
            cursor.execute(sql0)
            result = cursor.fetchone()
            if result:
                if result != '0':
                    time = dt.datetime.now().strftime('%F')
                    sql = "INSERT INTO borrow VALUES('%s','%s','%s')" % (ID.getid(), e_name.get(), time)
                    sql1 = "UPDATE equipment SET amount=amount-1 WHERE name='%s'" % (e_name.get())
                    cursor.execute(sql)
                    cursor.execute(sql1)
                    msg.showinfo(title='Success！', message='The equipment is successfully borrowed!')
                    db.commit()
                    db.close()
                    win.destroy()
                else:
                    msg.showinfo(title='Error！', message='The equipment is out of stock!')
            else:
                msg.showinfo(title='Error！', message='The equipment was not found！')
        else:
            db.close()
            msg.showinfo(title='Error！', message='You have borrow！')

    else:
        sql4 = "UPDATE equipment SET amount=amount+1 WHERE name='%s'" % (e_name.get())
        cursor.execute(sql4)
        sql5 = "DELETE FROM book WHERE name='%s' AND userid='%s'" % (e_name.get(), ID.getid())
        cursor.execute(sql5)

        sql6 = "SELECT name FROM borrow WHERE userid='%s' AND name='%s'" % (ID.getid(), e_name.get())
        cursor.execute(sql6)
        result2 = cursor.fetchone()
        if result2 is None:
            sql0 = "SELECT amount FROM equipment WHERE name='%s'" % (e_name.get())
            cursor.execute(sql0)
            result = cursor.fetchone()
            if result:
                if result != '0':
                    time = dt.datetime.now().strftime('%F')  # 得到的时间不是字符串型，我们要把时间转化成字符串型
                    sql = "INSERT INTO borrow VALUES('%s','%s','%s')" % (ID.getid(), e_name.get(), time)
                    sql1 = "UPDATE equipment SET amount=amount-1 WHERE name='%s'" % (e_name.get())
                    cursor.execute(sql)
                    cursor.execute(sql1)
                    msg.showinfo(title='Success！', message='The equipment is successfully borrowed!')
                    db.commit()
                    db.close()
                    win.destroy()
                else:
                    msg.showinfo(title='Error！', message='The equipment is out of stock!')
            else:
                msg.showinfo(title='Error！', message='The equipment was not found！')
        else:
            db.close()
            msg.showinfo(title='Error！', message='You have borrow！')


# def confirm_borrow():
#     db = pymysql.connect(host='127.0.0.1',
#                          port=3306,
#                          user='root',
#                          passwd='cla051063',
#                          db='abes',
#                          charset='utf8'
#                          )
#     cursor = db.cursor()
#     sql = "SELECT name FROM borrow WHERE name='%s'" % (e_name.get())
#     cursor.execute(sql)
#     result2 = cursor.fetchone()
#     if result2 is None:
#         sql0 = "SELECT amount FROM equipment WHERE name='%s' AND userid='%s" % (e_name.get(),ID.getid())
#         cursor.execute(sql0)
#         result = cursor.fetchone()
#         if result:
#             if result != '0':
#                 time = dt.datetime.now().strftime('%F')  # 得到的时间不是字符串型，我们要把时间转化成字符串型
#                 sql = "INSERT INTO borrow VALUES('%s','%s','%s')" % (ID.getid(), e_name.get(), time)
#                 sql1 = "UPDATE equipment SET amount=amount-1 WHERE name='%s'" % (e_name.get())
#                 cursor.execute(sql)
#                 cursor.execute(sql1)
#                 msg.showinfo(title='Success！', message='The equipment is successfully borrowed!')
#                 db.commit()
#                 db.close()
#                 win.destroy()
#             else:
#                 msg.showinfo(title='Error！', message='The equipment is out of stock!')
#         else:
#             msg.showinfo(title='Error！', message='The equipment was not found！')
#     else:
#         db.close()
#         msg.showinfo(title='Error！', message='You have borrow！')


def turnback():  # 还书
    global win
    win = tk.Tk()
    win.title('Borrower')
    win.geometry('550x600')

    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='cla051063',
                         db='abes',
                         charset='utf8'
                         )
    cursor = db.cursor()
    sql0 = "SELECT COUNT(*) FROM borrow WHERE userid='%s'" % (ID.getid())
    cursor.execute(sql0)
    result = cursor.fetchone()
    if result[0] == 0:
        msg.showinfo(title='Error', message='You have not borrowed an equipment yet!')
    else:
        lable1 = tk.Label(win, text='The following equipment on the unreturned：', bg='pink',
                          font=('Microsoft YaHei', 20)).place(x=80, y=20)
        tree = ttk.Treeview(win, columns=('1', '2'), show="headings")
        tree.column('1', width=150, anchor='center')
        tree.column('2', width=150, anchor='center')
        tree.heading('1', text='Equipment')
        tree.heading('2', text='Date')
        tree.place(x=100, y=100)

        sql1 = "SELECT name,date FROM borrow WHERE userid='%s'" % (ID.getid())
        cursor.execute(sql1)
        result1 = cursor.fetchall()
        for i in range(0, result[0]):
            tree.insert('', i, values=(result1[i]))

        lable2 = tk.Label(win, text='Please enter your equipment return information：', bg='pink',
                          font=('Microsoft YaHei', 20)).place(x=80, y=360)
        lable22 = tk.Label(win, text='The equipment name should be filled in correctly！', bg='pink',
                           font=('Microsoft YaHei', 20)).place(x=80, y=400)
        global e_name
        tk.Label(win, text='Equipment：', font=('Microsoft YaHei', 12)).place(x=80, y=480)
        e_name = tk.Entry(win, font=('Microsoft YaHei', 12), width=10)
        e_name.place(x=180, y=480)

        tk.Button(win, text='Confirm Turn back', font=('Microsoft YaHei', 12), width=10,
                  command=confirm_turnback).place(x=395, y=480)
    db.close()


def confirm_turnback():
    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='cla051063',
                         db='abes',
                         charset='utf8'
                         )
    cursor = db.cursor()

    sql1 = "UPDATE equipment SET amount=amount+1 WHERE name='%s'" % (e_name.get())
    cursor.execute(sql1)
    # db.commit()

    # time1 = dt.datetime.now()  # 获取现在的时间
    # sql2 = "SELECT date FROM borrow WHERE name='%s'" % (e_name.get())
    # cursor.execute(sql2)
    # result = cursor.fetchone()
    # day = (time1 - result[0]).days  # 得到时间差，检查图书是否超期
    # print(day)
    # if day == 0:
    #     day = 1
    # if day > 30:
    #     msg.showinfo(title='Successful return', message='You are overdue! Please return it on time next time!')
    # else:
    #     msg.showinfo(title='Successful return', message='Return the book successfully, and not more than 30 days')
    sql0 = "DELETE FROM borrow WHERE name='%s' AND userid='%s'" % (e_name.get(), ID.getid())
    sql1 = "UPDATE equipment SET amount=amount+1 WHERE name='%s'" % (e_name.get())
    cursor.execute(sql1)
    cursor.execute(sql0)
    db.commit()
    db.close()
    msg.showinfo(title='Successful return', message='Return the book successfully')
    win.destroy()


def qrcode_show():
    global win
    win = tk.Tk()
    win.title('QR code borrow')
    win.geometry('700x600')
    lable0 = tk.Label(win, text=gettext(), bg='pink', font=('Microsoft YaHei', 50)).pack()  # 上
    tk.Button(win, text='Confirm Turn back', font=('Microsoft YaHei', 12), width=10,
              command=confirm_qrcode_borrow).place(x=600, y=195)
    win.mainloop()


def confirm_qrcode_borrow():
    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='cla051063',
                         db='abes',
                         charset='utf8'
                         )
    cursor = db.cursor()
    # test qrcode
    sql0 = "SELECT amount FROM equipment WHERE name='%s'" % (gettext())
    cursor.execute(sql0)
    result = cursor.fetchone()
    if result:
        if result != '0':
            time = dt.datetime.now().strftime('%F')  # 得到的时间不是字符串型，我们要把时间转化成字符串型
            sql = "INSERT INTO borrow VALUES('%s','%s','%s')" % (ID.getid(), gettext(), time)
            sql1 = "UPDATE equipment SET amount=amount-1 WHERE name='%s'" % (gettext())
            cursor.execute(sql)
            cursor.execute(sql1)
            msg.showinfo(title='Success！', message='Borrowed equipment successfully!')
            db.commit()
            db.close()
            win.destroy()
        else:
            msg.showinfo(title='Error！', message='Your borrowed equipment is out of stock！')
    else:
        msg.showinfo(title='Error！', message='The equipment was not found！')


def scan():
    global text1
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('scan qrcode', frame)
        # global text1
        # 解析二维码
        text1 = None
        try:
            text1 = scan_qrcode(frame)
        except Exception as e:
            pass
        if text1:
            print(text1)
            gettext()
            break

        key = cv2.waitKey(10)
        if key == ord('q'):
            break
    cv2.destroyAllWindows()


def scan_qrcode(qrcode):
    data = pyzbar.decode(qrcode)
    return data[0].data.decode('utf-8')


def gettext():
    return text1
