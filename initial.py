import tkinter as tk
import borrower
import manager
import face


def frame():
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
    bg1 = '#FFC284'
    lable1 = tk.Label(root, fg="black", bg=bg1, text='Please select the user type:', font=('Microsoft YaHei', 22)).place(x=80, y=100)  # 下

    tk.Button(root, text='Borrower', font=('Microsoft YaHei', 20), width=20, height=2, command=exit_borrower).place(x=350, y=320)
    tk.Button(root, text='Borrower face', font=('Microsoft YaHei', 20), width=20, height=2, command=exit_borrower_face).place(
        x=350, y=200)
    tk.Button(root, text='Manager', font=('Microsoft YaHei', 20), width=20, height=2, command=exit_manager).place(x=350, y=450)
    lable2 = tk.Label(root, fg="black", bg=bg1, text='Student Borrow Equipment', font=('Microsoft YaHei', 25)).place(x=350, y=150)
    lable3 = tk.Label(root, fg="black", bg=bg1, text='Manager manage Equipment', font=('Microsoft YaHei', 23)).place(x=350, y=400)

    root.mainloop()


def exit_borrower():
    root.destroy()
    borrower.frame()


def exit_borrower_face():
    root.destroy()
    face.frame()


def exit_manager():
    root.destroy()
    manager.frame()


def exit_qrcode():
    root.destroy()
    create_qrcode.frame()


if __name__ == '__main__':
    frame()
