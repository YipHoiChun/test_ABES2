import tkinter as tk
import initial
# import ID
import cv2, os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time
from tkinter import messagebox
import pymysql
import tkinter.messagebox as msg
from pyzbar import pyzbar
import pymysql
from tkinter import ttk
import search
import sys


def frame():
    bg1 = '#FFC284'

    global window

    text1 = "logout"
    Cheack_Log(text1)

    window = tk.Tk()

    window.title("Face register or login")

    window.configure(background=bg1)

    window.geometry('900x600')

    # Add image file
    bg = tk.PhotoImage(file="device-900_600.png")

    # Create Canvas
    canvas1 = tk.Canvas(window, width=900,
                        height=600)

    canvas1.pack(fill="both", expand=True)

    # Display image
    canvas1.create_image(0, 0, image=bg,
                         anchor="nw")

    x_cord = 75
    y_cord = 20
    checker = 0
    bg2 = '#848DFF'
    lbl0 = tk.Label(window, text="Registered face login", width=20, fg="white", bg=bg2,
                    font=('Times New Roman', 25, 'bold'))
    lbl0.place(x=100 - x_cord, y=150 - y_cord)

    l1 = tk.Label(window, text="Face login", width=25, fg="white", bg=bg2,
                  font=('Times New Roman', 25, 'bold'))
    l1.place(x=400 - x_cord, y=150 - y_cord)

    l2 = tk.Label(window, text="Click 1 to close the camera", width=25, fg="black", bg=bg1,
                  font=('Times New Roman', 25, 'bold'))
    l2.place(x=400 - x_cord, y=190 - y_cord)

    lbl = tk.Label(window, text="(1) Enter Student ID", width=20, height=2, fg="black", bg=bg1,
                   font=('Times New Roman', 25, 'bold'))
    lbl.place(x=100 - x_cord, y=200 - y_cord)

    global txt, txt2

    txt = tk.Entry(window, width=32, bg="white", fg="blue", font=('Times New Roman', 15, ' bold '))
    txt.place(x=100 - x_cord, y=250 - y_cord)

    lbl2 = tk.Label(window, text="(2) Enter Name", width=20, fg="black", bg=bg1, height=2,
                    font=('Times New Roman', 25, ' bold '))
    lbl2.place(x=100 - x_cord, y=300 - y_cord)

    txt2 = tk.Entry(window, width=32, bg="white", fg="blue", font=('Times New Roman', 15, ' bold '))
    txt2.place(x=100 - x_cord, y=350 - y_cord)

    takeImg = tk.Button(window, text="(3) Image Capture Button", command=TakeImages, fg="black", bg="blue", width=30,
                        activebackground="pink", font=('Times New Roman', 15, ' bold '))
    takeImg.place(x=100 - x_cord, y=400 - y_cord)
    trainImg = tk.Button(window, text="(4) Model Training Button", command=TrainImages, fg="black", bg="blue", width=30,
                         activebackground="pink", font=('Times New Roman', 15, ' bold '))
    trainImg.place(x=100 - x_cord, y=450 - y_cord)

    borrow = tk.Button(window, text="(2) Login", command=Cheack_Login, fg="black", bg="blue", width=23,
                       activebackground="pink", font=('Times New Roman', 25, ' bold '))
    borrow.place(x=400 - x_cord, y=300 - y_cord)

    trackImg = tk.Button(window, text="(1) Face Recognition", command=TrackImages, fg="black", width=23,
                         activebackground="pink", font=('Times New Roman', 25, ' bold '))
    trackImg.place(x=400 - x_cord, y=235 - y_cord)
    quitWindow = tk.Button(window, text="Quit", command=quit_window, fg="black", width=10,
                           activebackground="pink", font=('Times New Roman', 25, ' bold '))
    quitWindow.place(x=400, y=500 - y_cord)

    window.mainloop()


def clear1():
    txt.delete(0, 'end')
    res = ""
    # message.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = ""
    # message.configure(text=res)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def TakeImages():
    Id = (txt.get())
    name = (txt2.get())
    if not Id:
        res = "Please enter Id"
        # message.configure(text=res)
        msg._show(title='error！', message=res)
        MsgBox = tk.messagebox.askquestion("Warning", "Please enter roll number properly , press yes if you understood",
                                           icon='warning')
        if MsgBox == 'no':
            tk.messagebox.showinfo('Your need', 'Please go through the readme file properly')
    elif not name:
        res = "Please enter Name"
        # message.configure(text=res)
        msg._show(title='error！', message=res)
        MsgBox = tk.messagebox.askquestion("Warning", "Please enter your name properly , press yes if you understood",
                                           icon='warning')
        if MsgBox == 'no':
            tk.messagebox.showinfo('Your need', 'Please go through the readme file properly')

    elif (is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage/ " + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                # display the frame
                cv2.imshow('frame', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
        msg.showinfo(title='success！', message=res)
    else:
        if (is_number(Id)):
            res = "Enter Alphabetical Name"
            # message.configure(text=res)
        if (name.isalpha()):
            res = "Enter Numeric Id"
            # message.configure(text=res)


def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    faces, Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel/Trainner.yml")
    res = "Image Trained"
    clear1()
    clear2()
    # message.configure(text=res)
    msg.showinfo(title='success！', message=res)
    tk.messagebox.showinfo('Completed', 'Your model has been trained successfully!!')


def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

    faces = []

    Ids = []

    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids


def TrackImages():
    global StId
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel/Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if 'Id' in df and (conf < 50):

                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown/Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('1')):
            break
    # global StId
    StId = Id
    getid()
    Cheack_Log(text1='login')
    cv2.destroyAllWindows()


def Cheack_Log(text1):
    global log
    log = text1
    login = "login"
    logout = "logout"
    getlog()
    if text1 == login:
        print(text1)
    elif text1 == logout:
        print(text1)
    else:
        print("error")


def Cheack_Login():
    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='cla051063',
                         db='abes',
                         charset='utf8'
                         )
    cursor = db.cursor()
    global id1
    id1 = getid()
    sql = "SELECT id FROM user WHERE id='%s'" % (id1)
    cursor.execute(sql)
    result = cursor.fetchone()
    log = getlog()
    log1 = "login"
    if log1 == log:
        if result and log1 == log:
            db.close()
            print(id1)
            text1 = 'login'
            Cheack_Log(text1)
            Borrow_frame()
        else:
            msg._show(title='error！', message='The user you entered does not exist! Please register first!')
    else:
        msg._show(title='error！', message='Please rescan the human face!')


def getid():
    return StId


def quit_window():
    window.destroy()
    initial.frame()


def Borrow_frame():
    global window2
    window2 = tk.Tk()
    window2.title('Borrower Operation')
    window2.geometry('700x600')
    window2.configure(background='#7DC0F8')
    lable = tk.Label(window2, text="Student ID:  ", font=('Microsoft YaHei', 50)).place(x=20, y=10)
    lable0 = tk.Label(window2, text=getid(), font=('Microsoft YaHei', 50)).place(x=280, y=10)

    lable1 = tk.Label(window2, text='Please select:', font=('Microsoft YaHei', 20)).place(x=80, y=200)
    lable2 = tk.Label(window2, text='General input borrow', font=('Microsoft YaHei', 20)).place(x=80, y=250)
    lable3 = tk.Label(window2, text='QR code borrow', font=('Microsoft YaHei', 20)).place(x=80, y=550)

    tk.Button(window2, text='Borrow', font=('Microsoft YaHei', 15), width=10, height=2, command=borrow).place(x=350,
                                                                                                              y=250)
    tk.Button(window2, text='Return', font=('Microsoft YaHei', 15), width=10, height=2, command=turnback).place(x=350,
                                                                                                                y=350)
    tk.Button(window2, text='Search', font=('Microsoft YaHei', 15), width=10, height=2, command=search.frame).place(
        x=350, y=450)

    tk.Button(window2, text='(1)QR code', font=('Microsoft YaHei', 15), width=10, height=2, command=scan).place(x=350,
                                                                                                             y=550)
    tk.Button(window2, text='(2)Borrow', font=('Microsoft YaHei', 15), width=10, height=2, command=qrcode_show).place(
        x=500, y=550)

    tk.Button(window2, text='Logout', font=('Microsoft YaHei', 15), width=10, height=2, command=out).place(x=550, y=20)

    window2.mainloop()


def out():
    text1 = 'logout'
    Cheack_Log(text1)
    window2.destroy()


def getlog():
    return log


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
    sql3 = "SELECT name FROM book WHERE userid='%s' AND name='%s'" % (getid(), e_name.get())
    cursor.execute(sql3)
    result3 = cursor.fetchone()
    print(result3)
    if result3 is None:
        print('not book')
        sql = "SELECT name FROM borrow WHERE userid='%s' AND name='%s'" % (getid(), e_name.get())
        cursor.execute(sql)
        result2 = cursor.fetchone()
        if result2 is None:
            sql0 = "SELECT amount FROM equipment WHERE name='%s'" % (e_name.get())
            cursor.execute(sql0)
            result = cursor.fetchone()
            if result:
                if result != '0':
                    time = datetime.datetime.now().strftime('%F.%H:%M:%S')
                    sql = "INSERT INTO borrow VALUES('%s','%s','%s')" % (getid(), e_name.get(), time)
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
        print('have book')
        sql4 = "UPDATE equipment SET amount=amount+1 WHERE name='%s'" % (e_name.get())
        cursor.execute(sql4)
        sql5 = "DELETE FROM book WHERE name='%s' AND userid='%s'" % (e_name.get(), getid())
        cursor.execute(sql5)

        sql6 = "SELECT name FROM borrow WHERE userid='%s' AND name='%s'" % (getid(), e_name.get())
        cursor.execute(sql6)
        result2 = cursor.fetchone()
        if result2 is None:
            sql0 = "SELECT amount FROM equipment WHERE name='%s'" % (e_name.get())
            cursor.execute(sql0)
            result = cursor.fetchone()
            if result:
                if result != '0':
                    time = datetime.datetime.now().strftime('%F')
                    sql = "INSERT INTO borrow VALUES('%s','%s','%s')" % (getid(), e_name.get(), time)
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


def turnback():
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
    sql0 = "SELECT COUNT(*) FROM borrow WHERE userid='%s'" % (getid())
    cursor.execute(sql0)
    result = cursor.fetchone()
    if result[0] == 0:
        msg.showinfo(title='Error', message='You have not borrowed an equipment yet！')
    else:
        lable1 = tk.Label(win, text='The following equipment on the unreturned：', bg='pink',
                          font=('Microsoft YaHei', 20)).place(
            x=80, y=20)
        tree = ttk.Treeview(win, columns=('1', '2'), show="headings")
        tree.column('1', width=150, anchor='center')
        tree.column('2', width=150, anchor='center')
        tree.heading('1', text='Equipment')
        tree.heading('2', text='Date')
        tree.place(x=100, y=100)

        sql1 = "SELECT name,date FROM borrow WHERE userid='%s'" % (getid())
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
                  command=confirm_turnback).place(x=395,
                                                  y=480)
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

    # time1 = datetime.datetime.now()
    sql2 = "SELECT date FROM borrow WHERE name='%s'" % (e_name.get())
    cursor.execute(sql2)

    sql0 = "DELETE FROM borrow WHERE name='%s' AND userid='%s'" % (e_name.get(), getid())
    msg.showinfo(title='Successful return', message='Return the equipment successfully')
    cursor.execute(sql0)

    db.commit()
    db.close()
    win.destroy()


def qrcode_show():
    global win
    win = tk.Tk()
    win.title('QR code borrow')
    win.geometry('700x600')
    text = get_text()
    text2 = "Name: " + text
    lable0 = tk.Label(win, text=text2, bg='pink', font=('Microsoft YaHei', 50)).pack()
    tk.Button(win, text='Confirm Turn back', font=('Microsoft YaHei', 12), width=10,
              command=confirm_qrcode_borrow).place(x=300, y=195)
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
    sql3 = "SELECT name FROM book WHERE userid='%s' AND name='%s'" % (getid(), get_text())
    cursor.execute(sql3)
    result3 = cursor.fetchone()
    print(result3)
    if result3 is None:
        sql = "SELECT name FROM borrow WHERE userid='%s' AND name='%s'" % (getid(), get_text())
        cursor.execute(sql)
        result2 = cursor.fetchone()
        if result2 is None:
            print('not book')
            sql0 = "SELECT amount FROM equipment WHERE name='%s'" % (get_text())
            cursor.execute(sql0)
            result = cursor.fetchone()
            if result:
                if result != '0':
                    time = datetime.datetime.now().strftime('%F.%H:%M:%S')
                    sql = "INSERT INTO borrow VALUES('%s','%s','%s')" % (getid(), get_text(), time)
                    sql1 = "UPDATE equipment SET amount=amount-1 WHERE name='%s'" % (get_text())
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
        print('have book')
        sql4 = "UPDATE equipment SET amount=amount+1 WHERE name='%s'" % (get_text())
        cursor.execute(sql4)
        sql5 = "DELETE FROM book WHERE name='%s' AND userid='%s'" % (get_text(), getid())
        cursor.execute(sql5)

        sql6 = "SELECT name FROM borrow WHERE userid='%s' AND name='%s'" % (getid(), get_text())
        cursor.execute(sql6)
        result2 = cursor.fetchone()
        if result2 is None:
            sql0 = "SELECT amount FROM equipment WHERE name='%s'" % (get_text())
            cursor.execute(sql0)
            result = cursor.fetchone()
            if result:
                if result != '0':
                    time = datetime.datetime.now().strftime('%F.%H:%M:%S')
                    sql = "INSERT INTO borrow VALUES('%s','%s','%s')" % (getid(), get_text(), time)
                    sql1 = "UPDATE equipment SET amount=amount-1 WHERE name='%s'" % (get_text())
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


def scan():
    global text1
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('scan qrcode', frame)
        # global text1
        # Analyze the QR code
        text1 = None
        try:
            text1 = scan_qrcode(frame)
        except Exception as e:
            pass
        if text1:
            print(text1)
            get_text()
            break

        key = cv2.waitKey(10)
        if key == ord('q'):
            break
    cv2.destroyAllWindows()


def scan_qrcode(qrcode):
    data = pyzbar.decode(qrcode)
    return data[0].data.decode('utf-8')


def get_text():
    return text1
