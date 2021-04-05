import tkinter as tk
import borrower
import manager
import face
import create_qrcode


def frame():  # 初始界面
    global root
    root = tk.Tk()
    root.geometry('900x700')
    root.title('Borrow Equipment System')
    # Add image file
    bg = tk.PhotoImage(file="bg.png")

    # Create Canvas
    canvas1 = tk.Canvas(root, width=900,
                        height=700)

    canvas1.pack(fill="both", expand=True)

    # Display image
    canvas1.create_image(0, 0, image=bg,
                         anchor="nw")
    lable1 = tk.Label(root, text='Please select the user type:', font=('Microsoft YaHei', 20)).place(x=80, y=200)  # 下

    tk.Button(root, text='Borrower', font=('Microsoft YaHei', 15), width=20, height=2, command=exit_borrower).place(x=350, y=420)
    tk.Button(root, text='Borrower face', font=('Microsoft YaHei', 15), width=20, height=2, command=exit_borrower_face).place(
        x=350, y=300)

    tk.Button(root, text='Manager', font=('Microsoft YaHei', 15), width=20, height=2, command=exit_manager).place(x=350, y=550)
    # tk.Button(root, text='Qrcode', font=('微软雅黑', 15), width=20, height=2, command=exit_qrcode).place(x=350, y=200)
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
