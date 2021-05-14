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
    global win
    win = tk.Tk()
    win.title('Manager')
    win.geometry('700x600')
    win.configure(background='#7DC0F8')
    lable = tk.Label(win, text="Manager ID:", font=('Microsoft YaHei', 50)).place(x=20, y=10)
    lable0 = tk.Label(win, text=ID.getid(), font=('Microsoft YaHei', 50)).place(x=280, y=10)

    lable1 = tk.Label(win, text='Please select:', font=('Microsoft YaHei', 20)).place(x=80, y=200)

    tk.Button(win, text='Add equipment', font=('Microsoft YaHei', 15), width=10, height=2, command=purchase).place(
        x=350, y=250)
    tk.Button(win, text='Delete equipment', font=('Microsoft YaHei', 15), width=10, height=2, command=cancel).place(
        x=350, y=350)
    tk.Button(win, text='Equipment Search', font=('Microsoft YaHei', 15), width=10, height=2,
              command=search.frame).place(x=350, y=450)
    tk.Button(win, text='Borrow Search', font=('Microsoft YaHei', 15), width=10, height=2,
              command=search_borrower.frame).place(x=350, y=550)

    win.mainloop()


def purchase():
    global win2
    win2 = tk.Tk()
    win2.title('Manager')
    win2.geometry('900x300')
    win2.wm_attributes('-topmost', 1)
    lable1 = tk.Label(win2, text='Please fill in the information of the purchased equipments:',
                      font=('Microsoft YaHei', 20)).place(x=30, y=100)

    tk.Label(win2, text='Type：', font=('Microsoft YaHei', 12)).place(x=30, y=200)
    global list
    comvalue = tk.StringVar()
    list = ttk.Combobox(win2, textvariable=comvalue, height=10, width=10)
    list.place(x=100, y=200)
    list['values'] = ('Camera', 'Computer', 'Phone', 'Other')
    list.current(0)

    global e_name
    tk.Label(win2, text='Name：', font=('Microsoft YaHei', 12)).place(x=230, y=200)
    e_name = tk.Entry(win2, font=('Microsoft YaHei', 12), width=10)
    e_name.place(x=280, y=200)

    global amount
    tk.Label(win2, text='Amount：', font=('Microsoft YaHei', 12)).place(x=560, y=200)
    amount = tk.Entry(win2, font=('Microsoft YaHei', 12), width=5)
    amount.place(x=610, y=200)

    tk.Button(win2, text='Confirm Add', font=('Microsoft YaHei', 12), width=10, command=add).place(x=700, y=195)


def add():
    sql = "INSERT INTO equipment VALUES('%s','%s','%s','%s')" % (
        list.get(), e_name.get(), amount.get(), 'images.jpeg')

    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='cla051063',
                         db='abes',
                         charset='utf8'
                         )
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()
    msg.showinfo(title='Success！', message='Equipment add to database！')


def cancel():
    global win3
    win3 = tk.Tk()
    win3.title('Manager')
    win3.geometry('900x300')
    win3.wm_attributes('-topmost', 1)

    lable1 = tk.Label(win3, text='Please fill in the information of the delete equipment :',
                      font=('Microsoft YaHei', 20)).place(
        x=30, y=100)

    tk.Label(win3, text='Equipment Type：', font=('Microsoft YaHei', 12)).place(x=30, y=200)
    global list
    comvalue = tk.StringVar()
    list = ttk.Combobox(win3, textvariable=comvalue, height=10, width=10)
    list.place(x=100, y=200)
    list['values'] = ('Camera', 'Computer', 'Phone', 'Other')
    list.current(0)

    global e_name
    tk.Label(win3, text='Name：', font=('Microsoft YaHei', 12)).place(x=230, y=200)
    e_name = tk.Entry(win3, font=('Microsoft YaHei', 12), width=10)
    e_name.place(x=280, y=200)
    tk.Button(win3, text='Confirm Delete', font=('Microsoft YaHei', 12), width=10, command=delete).place(x=600, y=195)


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
    db.commit()
    db.close()
    msg.showinfo(title='Success！', message='equipment has been deleted！')
