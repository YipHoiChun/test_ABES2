import tkinter as tk
import tkinter.messagebox as msg
from tkinter import ttk
import pymysql


def frame():
    global window
    window = tk.Tk()
    window.title('Equipment查询')
    window.geometry('1200x700')

    tk.Label(window, text='Equipment type：', font=('宋体', 12)).place(x=200, y=30)

    global list
    comvalue = tk.StringVar()
    list = ttk.Combobox(window, textvariable=comvalue, height=10, width=10)
    list.place(x=300, y=30)
    list['values'] = ('All', 'Camera', 'Computer', 'Phone', 'Other')
    list.current(0)

    global e_name
    tk.Label(window, text='Name：', font=('宋体', 12)).place(x=450, y=30)
    e_name = tk.Entry(window, font=('宋体', 12), width=15)
    e_name.place(x=500, y=30)

    tk.Button(window, text='搜索', font=('宋体', 12), width=10, command=search).place(x=900, y=25)
    global tree  # 建立树形图
    yscrollbar = ttk.Scrollbar(window, orient='vertical')  # 右边的滑动按钮
    tree = ttk.Treeview(window, columns=('1', '2', '3'), show="headings", yscrollcommand=yscrollbar.set)
    tree.column('1', width=150, anchor='center')
    tree.column('2', width=150, anchor='center')
    tree.column('3', width=150, anchor='center')
    tree.heading('1', text='Type')
    tree.heading('2', text='Name')
    tree.heading('3', text='Amount')
    tree.place(x=200, y=150)
    yscrollbar.place(x=955, y=150)
    window.mainloop()


def search():
    # 我用了最原始的方法来动态查询
    if list.get() == 'All' and e_name.get() == '':
        sql = "SELECT * FROM equipment "
    elif list.get() == 'All' and e_name.get() == '':
        sql = "SELECT * FROM equipment WHERE name='%s'" % (e_name.get())
    elif list.get() == 'All' and e_name.get() != '':
        sql = "SELECT * FROM equipment WHERE name='%s'" % (e_name.get())
    elif list.get() != 'All' and e_name.get() == '':
        sql = "SELECT * FROM equipment WHERE type='%s'" % (list.get())
    elif list.get() != 'All' and e_name.get() != '':
        sql = "SELECT * FROM equipment WHERE type='%s' AND name='%s'" % (list.get(), e_name.get())
    else:
        sql = "SELECT * FROM book WHERE type='%s' AND name='%s'" % (
        list.get(), e_name.get())

    # db = pymysql.connect("localhost", "root", "qwer", "library")

    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='cla051063',
                         db='abes',
                         charset='utf8'
                         )
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    if results:
        l = len(results)
        for i in range(0, l):  # 查询到的结果依次插入到表格中
            tree.insert('', i, values=(results[i]))
    else:
        tree.insert('', 0, values=('查询不到结果', '查询不到结果', '查询不到结果'))

    db.close()
