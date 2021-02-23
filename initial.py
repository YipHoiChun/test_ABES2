import tkinter as tk
import borrower
import manager
import face
import create_qrcode

def frame():  # 初始界面
    global root
    root = tk.Tk()
    root.geometry('900x700')
    root.title('IVE借用設備系统')
    lable0 = tk.Label(root, text='欢迎来到XDU图书馆', bg='pink', font=('微软雅黑', 50)).pack()  # 上
    lable1 = tk.Label(root, text='请选择用户类型:', font=('微软雅黑', 20)).place(x=80, y=500)  # 下

    tk.Button(root, text='Borrower', font=('微软雅黑', 15), width=20, height=2, command=exit_borrower).place(x=350, y=420)
    tk.Button(root, text='Borrower face', font=('微软雅黑', 15), width=20, height=2, command=exit_borrower_face).place(x=350, y=300)

    tk.Button(root, text='管理员', font=('微软雅黑', 15), width=20, height=2, command=exit_manager).place(x=350, y=550)
    tk.Button(root, text='Qrcode', font=('微软雅黑', 15), width=20, height=2, command=exit_qrcode).place(x=350, y=200)
    root.mainloop()  # 必须要有这句话，你的页面才会动态刷新循环，否则页面不会显示


def exit_borrower():  # 跳转至读者界面
    root.destroy()
    borrower.frame()

def exit_borrower_face():
    root.destroy()
    face.frame()

def exit_manager():  # 跳转至管理员界面
    root.destroy()
    manager.frame()

def exit_qrcode():
    root.destroy()
    create_qrcode.frame()


if __name__ == '__main__':
    frame()
