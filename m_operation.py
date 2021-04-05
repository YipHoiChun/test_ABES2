import tkinter as tk
import tkinter.messagebox as msg
import search
from tkinter import ttk
import pymysql
import search_borrower
import create_qrcode
import cv2
from pyzbar import pyzbar
import ID


def frame():
    global window
    window = tk.Tk()
    window.title('Manager')
    window.geometry('900x700')

    lable1 = tk.Label(window, text='Please select:', font=('Microsoft YaHei', 20)).place(x=80, y=400)

    # tk.Button(window, text='QRcode', font=('微软雅黑', 15), width=10, height=2, command=exit_m_operation).place(x=350, y=150)

    tk.Button(window, text='Add equipment', font=('Microsoft YaHei', 15), width=10, height=2, command=purchase).place(
        x=350, y=250)
    tk.Button(window, text='Delete equipment', font=('Microsoft YaHei', 15), width=10, height=2, command=cancel).place(
        x=350, y=350)
    tk.Button(window, text='Equipment Search', font=('Microsoft YaHei', 15), width=10, height=2,
              command=search.frame).place(x=350, y=450)
    tk.Button(window, text='Borrow Search', font=('Microsoft YaHei', 15), width=10, height=2,
              command=search_borrower.frame).place(x=350, y=550)

    window.mainloop()


def purchase():  # 进购图书
    global win
    win = tk.Tk()
    win.title('Manager')
    win.geometry('900x300')
    win.wm_attributes('-topmost', 1)
    lable1 = tk.Label(win, text='Please fill in the information of the purchased equipments:',
                      font=('Microsoft YaHei', 20)).place(x=30, y=100)

    tk.Label(win, text='Type：', font=('宋体', 12)).place(x=30, y=200)
    global list  # 这个是一个下拉页表项，只能从下面的list['values']里边选
    comvalue = tk.StringVar()
    list = ttk.Combobox(win, textvariable=comvalue, height=10, width=10)
    list.place(x=100, y=200)
    list['values'] = ('Camera', 'Computer', 'Phone', 'Other')
    list.current(0)  # 默认显示'全部'

    global e_name
    tk.Label(win, text='Name：', font=('Microsoft YaHei', 12)).place(x=230, y=200)
    e_name = tk.Entry(win, font=('Microsoft YaHei', 12), width=10)
    e_name.place(x=280, y=200)

    global amount
    tk.Label(win, text='Amount：', font=('Microsoft YaHei', 12)).place(x=560, y=200)
    amount = tk.Entry(win, font=('Microsoft YaHei', 12), width=5)
    amount.place(x=610, y=200)

    tk.Button(win, text='Confirm Add', font=('Microsoft YaHei', 12), width=10, command=add).place(x=700, y=195)


def add():  # 添加图书信息到数据库中
    sql = "INSERT INTO equipment VALUES('%s','%s','%s')" % (
        list.get(), e_name.get(), amount.get())

    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='cla051063',
                         db='abes',
                         charset='utf8'
                         )
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()  # 这句不可或缺，当我们修改数据完成后必须要确认才能真正作用到数据库里
    db.close()
    msg.showinfo(title='Success！', message='Equipment add to database！')


def cancel():  # 撤销图书
    global win
    win = tk.Tk()
    win.title('Manager')
    win.geometry('900x300')
    win.wm_attributes('-topmost', 1)

    lable1 = tk.Label(win, text='Please fill in the information of the delete equipment :', font=('Microsoft YaHei', 20)).place(
        x=30, y=100)

    tk.Label(win, text='Equipment Type：', font=('Microsoft YaHei', 12)).place(x=30, y=200)
    global list
    comvalue = tk.StringVar()
    list = ttk.Combobox(win, textvariable=comvalue, height=10, width=10)
    list.place(x=100, y=200)
    list['values'] = ('Camera', 'Computer', 'Phone', 'Other')
    list.current(0)

    global e_name
    tk.Label(win, text='Name：', font=('Microsoft YaHei', 12)).place(x=230, y=200)
    e_name = tk.Entry(win, font=('Microsoft YaHei', 12), width=10)
    e_name.place(x=280, y=200)
    tk.Button(win, text='Confirm Delete', font=('Microsoft YaHei', 12), width=10, command=delete).place(x=600, y=195)


# 删除图书
def delete():
    sql = "DELETE FROM equipment WHERE type='%s' AND name='%s'" % (list.get(), e_name.get())
    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='cla051063',
                         db='abes',
                         charset='utf8'
                         )
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()  # 这句不可或缺，当我们修改数据完成后必须要确认才能真正作用到数据库里
    msg.showinfo(title='Success！', message='equipment has been deleted！')
