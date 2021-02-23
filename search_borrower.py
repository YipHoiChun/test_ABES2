import tkinter as tk
import tkinter.messagebox as msg
from tkinter import ttk
import pymysql



def frame():
    global window
    window = tk.Tk()
    window.title('借物查询')
    window.geometry('1200x700')

    # tk.Label(window, text='图书类目：', font=('宋体', 12)).place(x=220, y=30)

    # global list
    # comvalue = tk.StringVar()
    # list = ttk.Combobox(window, textvariable=comvalue, height=10, width=10)
    # list.place(x=300, y=30)
    # list['values'] = ('全部', '人文', '艺术', '计算机', '科技', '杂志')
    # list.current(0)

    tk.Label(window, text='ID：', font=('宋体', 12)).place(x=220, y=30)


    global id
    tk.Label(window, text='书名：', font=('宋体', 12)).place(x=450, y=30)
    id = tk.Entry(window, font=('宋体', 12), width=15)
    id.place(x=300, y=30)

    global b_name
    tk.Label(window, text='Book:', font=('宋体', 12)).place(x=450, y=30)
    b_name = tk.Entry(window, font=('宋体', 12), width=15)
    b_name.place(x=500, y=30)

    global author
    tk.Label(window, text='Author：', font=('宋体', 12)).place(x=650, y=30)
    author = tk.Entry(window, font=('宋体', 12), width=15)
    author.place(x=700, y=30)

    # tk.Button(window, text='搜索', font=('宋体', 12), width=10, command=search).place(x=900, y=25)
    tk.Button(window, text='搜索', font=('宋体', 12), width=10, command=search).place(x=900, y=25)

    global tree  # 建立树形图
    yscrollbar = ttk.Scrollbar(window, orient='vertical')  # 右边的滑动按钮
    tree = ttk.Treeview(window, columns=('1', '2', '3', '4'), show="headings", yscrollcommand=yscrollbar.set)
    # tree = ttk.Treeview(window, columns=('1', '2', '3', '4', '5'), show="headings", yscrollcommand=yscrollbar.set)
    tree.column('1', width=150, anchor='center')
    tree.column('2', width=150, anchor='center')
    tree.column('3', width=150, anchor='center')
    tree.column('4', width=150, anchor='center')
    # tree.column('5', width=150, anchor='center')
    tree.heading('1', text='id')
    tree.heading('2', text='book name')
    tree.heading('3', text='author')
    tree.heading('4', text='date')
    # tree.heading('5', text='库存')
    tree.place(x=200, y=150)
    yscrollbar.place(x=955, y=150)
    window.mainloop()

def search():
    # 我用了最原始的方法来动态查询
    if id.get() == '' and b_name.get() == '' and author.get() == '':
        sql = "SELECT * FROM borrow "
    elif id.get() == '' and b_name.get() == '' and author.get() != '':
        sql = "SELECT * FROM borrow WHERE author='%s'" % (author.get())
    elif id.get() == '' and b_name.get() != '' and author.get() == '':
        sql = "SELECT * FROM borrow WHERE bookname='%s'" % (b_name.get())
    elif id.get() != '' and b_name.get() == '' and author.get() == '':
        sql = "SELECT * FROM borrow WHERE id='%s'" % (id.get())
    elif id.get() == '' and b_name.get() != '' and author.get() != '':
        sql = "SELECT * FROM borrow WHERE bookname='%s' AND author='%s'" % (b_name.get(), author.get())
    elif id.get() != '全部' and b_name.get() != '' and author.get() == '':
        sql = "SELECT * FROM borrow WHERE id='%s' AND bookname='%s'" % (id.get(), b_name.get())
    elif id.get() != '全部' and b_name.get() == '' and author.get() != '':
        sql = "SELECT * FROM borrow WHERE id='%s' AND author ='%s'" % (id.get(), author.get())
    else:
        sql = "SELECT * FROM borrow WHERE id='%s' AND bookname='%s' AND author ='%s'" % (
        id.get(), b_name.get(), author.get())

    # db = pymysql.connect("localhost", "root", "qwer", "library")

    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='cla051063',
                         db='library3',
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
        tree.insert('', 0, values=('查询不到结果', '查询不到结果', '查询不到结果', '查询不到结果'))

    db.close()