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
    bg1 = '#84C1FF'

    global window

    text1 = "logout"
    Cheack_Log(text1)

    window = tk.Tk()

    window.title("Automatic Borrow Equipment System")

    window.configure(background=bg1)

    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    x_cord = 75
    y_cord = 20
    checker = 0

    message = tk.Label(window, text=" Automatic Borrow Equipment System", bg=bg1, fg="black", width=40, height=1,
                       font=('Times New Roman', 35, 'bold underline'))
    message.place(x=200, y=20)
    message.pack()

    lbl = tk.Label(window, text="Enter Your Student ID", width=20, height=2, fg="black", bg=bg1,
                   font=('Times New Roman', 25, ' bold '))
    lbl.place(x=200 - x_cord, y=200 - y_cord)

    global txt, txt2

    txt = tk.Entry(window, width=32, bg="white", fg="blue", font=('Times New Roman', 15, ' bold '))
    txt.place(x=200 - x_cord, y=300 - y_cord)

    lbl2 = tk.Label(window, text="Enter Your Name", width=20, fg="black", bg=bg1, height=2,
                    font=('Times New Roman', 25, ' bold '))
    lbl2.place(x=600 - x_cord, y=200 - y_cord)

    txt2 = tk.Entry(window, width=32, bg="white", fg="blue", font=('Times New Roman', 15, ' bold '))
    txt2.place(x=600 - x_cord, y=300 - y_cord)

    lbl3 = tk.Label(window, text="NOTIFICATION", width=20, fg="black", bg=bg1, height=2,
                    font=('Times New Roman', 25, ' bold '))
    lbl3.place(x=1000 - x_cord, y=200 - y_cord)

    lbl4 = tk.Label(window, text="STEP 1", width=26, fg="red", bg=bg1, height=2,
                    font=('Times New Roman', 20, ' bold '))
    lbl4.place(x=200 - x_cord, y=375 - y_cord)

    lbl5 = tk.Label(window, text="STEP 2", width=26, fg="red", bg=bg1, height=2,
                    font=('Times New Roman', 20, ' bold '))
    lbl5.place(x=600 - x_cord, y=375 - y_cord)

    lbl6 = tk.Label(window, text="STEP 3", width=26, fg="red", bg=bg1, height=2,
                    font=('Times New Roman', 20, ' bold '))
    lbl6.place(x=1000 - x_cord, y=375 - y_cord)

    takeImg = tk.Button(window, text="Student ID", command=Cheack_Login, fg=bg1, bg="blue", width=30,
                        activebackground="pink", font=('Times New Roman', 15, ' bold '))
    takeImg.place(x=200 - x_cord, y=500 - y_cord)

    takeImg = tk.Button(window, text="Image Capture Button", command=TakeImages, fg=bg1, bg="blue", width=30,
                        activebackground="pink", font=('Times New Roman', 15, ' bold '))
    takeImg.place(x=200 - x_cord, y=425 - y_cord)
    trainImg = tk.Button(window, text="Model Training Button", command=TrainImages, fg=bg1, bg="blue", width=30,
                         activebackground="pink", font=('Times New Roman', 15, ' bold '))
    trainImg.place(x=600 - x_cord, y=425 - y_cord)
    trackImg = tk.Button(window, text="Test Face Button", command=TrackImages, fg=bg1, bg="red", width=30,
                         activebackground="pink", font=('Times New Roman', 15, ' bold '))
    trackImg.place(x=1000 - x_cord, y=425 - y_cord)
    quitWindow = tk.Button(window, text="QUIT", command=quit_window, fg=bg1, bg="red", width=10,
                           activebackground="pink", font=('Times New Roman', 15, ' bold '))
    quitWindow.place(x=700, y=735 - y_cord)

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
        msg._show(title='错误！', message=res)
        MsgBox = tk.messagebox.askquestion("Warning", "Please enter roll number properly , press yes if you understood",
                                           icon='warning')
        if MsgBox == 'no':
            tk.messagebox.showinfo('Your need', 'Please go through the readme file properly')
    elif not name:
        res = "Please enter Name"
        # message.configure(text=res)
        msg._show(title='错误！', message=res)
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
        msg.showinfo(title='成功！', message=res)
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
    msg.showinfo(title='成功！', message=res)
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
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if 'Id' in df and (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                # tt = str(Id) + "-" + str(aa)
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown/Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('1')):
            break
    # global StId
    StId = Id
    getid()
    Cheack_Log(text1='login')
    cv2.destroyAllWindows()
    # Cheack_Login()
    # time.sleep(10)
    # Cheack_Login()


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
                         db='library3',
                         charset='utf8'
                         )
    cursor = db.cursor()
    global id1
    id1 = getid()
    sql = "SELECT id FROM user WHERE id='%s'" % (id1)
    cursor.execute(sql)  # sql语句被执行
    result = cursor.fetchone()  # 得到的结果返回给result数组
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
            msg._show(title='错误！', message='您输入的用户不存在！请先注册！')
    else:
        msg._show(title='错误！', message='請重新掃描人面！')
    # if result and log1 == log:
    #     db.close()
    #     print(id1)
    #     text1 = 'login'
    #     Cheack_Log(text1)
    #     Borrow_frame()
    # else:
    #     msg._show(title='错误！', message='您输入的用户不存在！请先注册！')


def getid():
    return StId


# def Borrow_frame():
#     window2 = tk.Tk()
#     window2.title('Borrow')
#     window2.geometry('700x600')
#     lable0 = tk.Label(window2, text=getid(), bg='pink', font=('微软雅黑', 50)).pack()  # 上
#     window2.mainloop()


def quit_window():  # 退出管理员界面，跳转至初始界面
    window.destroy()
    initial.frame()


def Borrow_frame():
    global window2
    window2 = tk.Tk()
    window2.title('Borrow')
    window2.geometry('700x600')
    lable0 = tk.Label(window2, text=getid(), bg='pink', font=('微软雅黑', 50)).pack()  # 上

    lable1 = tk.Label(window2, text='请选择操作:', font=('微软雅黑', 20)).place(x=80, y=400)  # 下
    tk.Button(window2, text=' 借  书', font=('微软雅黑', 15), width=10, height=2, command=borrow).place(x=350, y=250)
    tk.Button(window2, text=' 还  书', font=('微软雅黑', 15), width=10, height=2, command=turnback).place(x=350, y=350)
    tk.Button(window2, text='信息查询', font=('微软雅黑', 15), width=10, height=2, command=search.frame).place(x=350, y=450)

    tk.Button(window2, text='QR code', font=('微软雅黑', 15), width=10, height=2, command=scan).place(x=350, y=550)
    tk.Button(window2, text='QR(Load)', font=('微软雅黑', 15), width=10, height=2, command=qrcode_show).place(x=500, y=550)

    tk.Button(window2, text='out', font=('微软雅黑', 15), width=10, height=2, command=out).place(x=200, y=550)

    window2.mainloop()


def out():
    # sys.exit
    # text1 = 'logout'
    text1 = 'logout'
    Cheack_Log(text1)
    window2.destroy()

def getlog():
    return log

def borrow():
    global win
    win = tk.Tk()
    win.title('读者')
    win.geometry('900x300')
    win.wm_attributes('-topmost', 1)
    lable1 = tk.Label(win, text='请填写所借图书的信息:(书名作者都要填写正确无误！)', bg='pink', font=('微软雅黑', 20)).place(x=30, y=100)

    global b_name
    tk.Label(win, text='书名：', font=('宋体', 12)).place(x=200, y=200)
    b_name = tk.Entry(win, font=('宋体', 12), width=10)
    b_name.place(x=250, y=200)

    global author
    tk.Label(win, text='作者：', font=('宋体', 12)).place(x=350, y=200)
    author = tk.Entry(win, font=('宋体', 12), width=10)
    author.place(x=400, y=200)

    tk.Button(win, text='确认借书', font=('宋体', 12), width=10, command=confirm_borrow).place(x=600, y=195)


def confirm_borrow():
    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='cla051063',
                         db='library3',
                         charset='utf8'
                         )
    cursor = db.cursor()
    sql0 = "SELECT amount FROM book WHERE name='%s' AND author='%s'" % (b_name.get(), author.get())
    cursor.execute(sql0)
    result = cursor.fetchone()
    if result:
        if result != '0':
            time = datetime.datetime.now().strftime('%F')  # 得到的时间不是字符串型，我们要把时间转化成字符串型
            sql = "INSERT INTO borrow VALUES('%s','%s','%s','%s')" % (getid(), b_name.get(), author.get(), time)
            sql1 = "UPDATE book SET amount=amount-1 WHERE name='%s' AND author='%s'" % (b_name.get(), author.get())
            cursor.execute(sql)
            cursor.execute(sql1)
            msg.showinfo(title='成功！', message='借书成功！请一个月之内归还')
            db.commit()
            db.close()
            win.destroy()
        else:
            msg.showinfo(title='失败！', message='您借的书库存不足！')
    else:
        msg.showinfo(title='错误！', message='未找到该书！')


def turnback():  # 还书
    global win
    win = tk.Tk()
    win.title('读者')
    win.geometry('550x600')

    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='cla051063',
                         db='library3',
                         charset='utf8'
                         )
    cursor = db.cursor()
    sql0 = "SELECT COUNT(*) FROM borrow WHERE id='%s'" % (getid())
    cursor.execute(sql0)
    result = cursor.fetchone()
    if result[0] == 0:
        msg.showinfo(title='错误', message='您还没借过书呢！')
    else:
        lable1 = tk.Label(win, text='查询到您有以下书目未还：', bg='pink', font=('微软雅黑', 20)).place(x=80, y=20)
        tree = ttk.Treeview(win, columns=('1', '2'), show="headings")
        tree.column('1', width=150, anchor='center')
        tree.column('2', width=150, anchor='center')
        tree.heading('1', text='书名')
        tree.heading('2', text='作者')
        tree.place(x=100, y=100)

        sql1 = "SELECT bookname,author FROM borrow WHERE id='%s'" % (getid())
        cursor.execute(sql1)
        result1 = cursor.fetchall()
        for i in range(0, result[0]):
            tree.insert('', i, values=(result1[i]))

        lable2 = tk.Label(win, text='请输入还书信息：', bg='pink', font=('微软雅黑', 20)).place(x=80, y=360)
        lable22 = tk.Label(win, text='书名作者都要填写正确无误！', bg='pink', font=('微软雅黑', 20)).place(x=80, y=400)
        global b_name
        tk.Label(win, text='书名：', font=('宋体', 12)).place(x=80, y=480)
        b_name = tk.Entry(win, font=('宋体', 12), width=10)
        b_name.place(x=130, y=480)

        global author
        tk.Label(win, text='作者：', font=('宋体', 12)).place(x=230, y=480)
        author = tk.Entry(win, font=('宋体', 12), width=10)
        author.place(x=280, y=480)

        tk.Button(win, text='确认还书', font=('宋体', 12), width=10, command=confirm_turnback).place(x=395, y=480)
    db.close()


def confirm_turnback():
    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='cla051063',
                         db='library3',
                         charset='utf8'
                         )
    cursor = db.cursor()

    sql1 = "UPDATE book SET amount=amount+1 WHERE name='%s' AND author='%s'" % (b_name.get(), author.get())
    cursor.execute(sql1)
    db.commit()

    time1 = datetime.datetime.now()  # 获取现在的时间
    sql2 = "SELECT date FROM borrow WHERE bookname='%s' AND author='%s'" % (b_name.get(), author.get())
    cursor.execute(sql2)
    result = cursor.fetchone()
    day = (time1 - result[0]).days  # 得到时间差，检查图书是否超期
    print(day)
    if day > 30:
        msg.showinfo(title='还书成功', message='还书成功，但您已经超期！请下次按时归还')
    else:
        msg.showinfo(title='还书成功', message='还书成功，且未超过30天')
    sql0 = "DELETE FROM borrow WHERE bookname='%s' AND author='%s'" % (b_name.get(), author.get())
    cursor.execute(sql0)
    db.commit()
    db.close()
    win.destroy()


def qrcode_show():
    global win
    win = tk.Tk()
    win.title('QR code borrow')
    win.geometry('700x600')
    lable0 = tk.Label(win, text=gettext(), bg='pink', font=('微软雅黑', 50)).pack()  # 上
    tk.Button(win, text='确认借书', font=('宋体', 12), width=10, command=confirm_qrcode_borrow).place(x=600, y=195)
    win.mainloop()


def confirm_qrcode_borrow():
    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='cla051063',
                         db='library3',
                         charset='utf8'
                         )
    cursor = db.cursor()
    # test qrcode
    author = "abc"
    sql0 = "SELECT amount FROM book WHERE name='%s' AND author='%s'" % (gettext(), author)
    cursor.execute(sql0)
    result = cursor.fetchone()
    if result:
        if result != '0':
            time = datetime.datetime.now().strftime('%F')  # 得到的时间不是字符串型，我们要把时间转化成字符串型
            sql = "INSERT INTO borrow VALUES('%s','%s','%s','%s')" % (getid(), gettext(), author, time)
            sql1 = "UPDATE book SET amount=amount-1 WHERE name='%s' AND author='%s'" % (gettext(), author)
            cursor.execute(sql)
            cursor.execute(sql1)
            msg.showinfo(title='成功！', message='借书成功！请一个月之内归还')
            db.commit()
            db.close()
            win.destroy()
        else:
            msg.showinfo(title='失败！', message='您借的书库存不足！')
    else:
        msg.showinfo(title='错误！', message='未找到该书！')


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
