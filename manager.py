import tkinter as tk
import tkinter.messagebox as msg
import initial
import pymysql
import ID


def frame():  # Manager frame
    global root
    root = tk.Tk()
    root.geometry('900x600')
    root.title('Borrow Equipment System')
    # Add image file
    bg = tk.PhotoImage(file="device-900_600.png")
    # Create Canvas
    canvas1 = tk.Canvas(root, width=900,
                        height=600)
    canvas1.pack(fill="both", expand=True)
    # Display image
    canvas1.create_image(0, 0, image=bg,
                         anchor="nw")
    lable0 = tk.Label(root, text='Manager Login', font=('Microsoft YaHei', 50)).place(x=300, y=100)

    lable1 = tk.Label(root, text='Please select:', font=('Microsoft YaHei', 20)).place(x=80, y=400)

    tk.Button(root, text='Login', font=('Microsoft YaHei', 15), width=10, height=2, command=login).place(x=150, y=500)
    tk.Button(root, text='Register', font=('Microsoft YaHei', 15), width=10, height=2, command=register).place(x=350, y=500)
    tk.Button(root, text='Quit', font=('Microsoft YaHei', 15), width=10, height=2, command=exit_manager).place(x=550, y=500)
    root.mainloop()


def login():
    global root1
    root1 = tk.Tk()
    root1.wm_attributes('-topmost', 1)
    root1.title('Manager Login')
    root1.geometry('500x300')

    lable1 = tk.Label(root1, text='Account：', font=25).place(x=100, y=50)
    lable2 = tk.Label(root1, text='Password：', font=25).place(x=90, y=100)

    global entry_name, entry_key
    name = tk.StringVar()
    key = tk.StringVar()

    entry_name = tk.Entry(root1, textvariable=name, font=25)
    entry_name.place(x=180, y=50)
    entry_key = tk.Entry(root1, textvariable=key, font=25, show='*')
    entry_key.place(x=180, y=100)
    button1 = tk.Button(root1, text='Confirm', height=2, width=10, command=lambda: ID.id_check('1'))

    button1.place(x=210, y=180)


def register():
    global root2
    root2 = tk.Tk()
    root2.wm_attributes('-topmost', 1)
    root2.title('Manager Register')
    root2.geometry('500x300')

    lable1 = tk.Label(root2, text='Account：', font=25).place(x=90, y=50)
    lable2 = tk.Label(root2, text='Password：', font=25).place(x=80, y=100)
    lable2 = tk.Label(root2, text='Confirm Password：', font=25).place(x=30, y=150)

    global entry_name, entry_key, entry_confirm
    name = tk.StringVar()
    key = tk.StringVar()
    confirm = tk.StringVar()
    entry_name = tk.Entry(root2, textvariable=name, font=25)
    entry_name.place(x=180, y=50)
    entry_key = tk.Entry(root2, textvariable=key, font=25, show='*')
    entry_key.place(x=180, y=100)
    entry_confirm = tk.Entry(root2, textvariable=confirm, font=25, show='*')
    entry_confirm.place(x=180, y=150)
    button1 = tk.Button(root2, text='Confirm', height=2, width=10, command=lambda: ID.id_write('1'))
    button1.place(x=210, y=200)


def exit_manager():
    root.destroy()
    initial.frame()
