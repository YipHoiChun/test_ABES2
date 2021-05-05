import re
import tkinter as tk
import cv2, os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox as msg
import pymysql


def frame():
    bg1 = '#84C1FF'

    global window

    window = tk.Tk()

    window.title("Automatic Borrow Equipment System")

    window.configure(background=bg1)

    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    x_cord = 75
    y_cord = 20
    checker = 0

    # message = tk.Label(window, text="DIT UNIVERSITY", bg="white", fg="black", width=20, height=2,
    #                    font=('Times New Roman', 25, 'bold'))
    # message.place(x=1150, y=760)

    message = tk.Label(window, text=" Automatic Borrow Equipment System", bg=bg1, fg="black", width=40, height=1,
                       font=('Times New Roman', 35, 'bold underline'))
    # message.place(x=200, y=20)
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
    lbl3.place(x=1000- x_cord, y=200 - y_cord)

    # message = tk.Label(window, text="", bg="white", fg="blue", width=32, height=1, activebackground="white",
    #                    font=('Times New Roman', 15, ' bold '))
    # message.place(x=1000 - x_cord, y=300 - y_cord)

    # lbl3 = tk.Label(window, text="ATTENDANCE", width=20, fg="white", bg="lightgreen", height=2,
    #                 font=('Times New Roman', 30, ' bold '))
    # lbl3.place(x=120, y=570 - y_cord)

    # message2 = tk.Label(window, text="", fg="red", bg="yellow", activeforeground="green", width=60, height=4,
    #                     font=('times', 15, ' bold '))
    # message2.place(x=700, y=570 - y_cord)

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
    takeImg.place(x=200 - x_cord, y=200 - y_cord)

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

# bg1 = '#84C1FF'
#
# window = tk.Tk()
#
# window.title("Automatic Borrow Equipment System")
#
# window.configure(background=bg1)
#
# window.grid_rowconfigure(0, weight=1)
# window.grid_columnconfigure(0, weight=1)
#
# x_cord = 75
# y_cord = 20
# checker = 0
#
# # message = tk.Label(window, text="DIT UNIVERSITY", bg="white", fg="black", width=20, height=2,
# #                    font=('Times New Roman', 25, 'bold'))
# # message.place(x=1150, y=760)
#
# message = tk.Label(window, text=" Automatic Borrow Equipment System", bg=bg1, fg="black", width=40, height=1,
#                    font=('Times New Roman', 35, 'bold underline'))
# # message.place(x=200, y=20)
# message.pack()
#
# lbl = tk.Label(window, text="Enter Your Student ID", width=20, height=2, fg="black", bg=bg1,
#                font=('Times New Roman', 25, ' bold '))
# lbl.place(x=200 - x_cord, y=200 - y_cord)
#
# txt = tk.Entry(window, width=32, bg="white", fg="blue", font=('Times New Roman', 15, ' bold '))
# txt.place(x=200 - x_cord, y=300 - y_cord)
#
# lbl2 = tk.Label(window, text="Enter Your Name", width=20, fg="black", bg=bg1, height=2,
#                 font=('Times New Roman', 25, ' bold '))
# lbl2.place(x=600 - x_cord, y=200 - y_cord)
#
# txt2 = tk.Entry(window, width=32, bg="white", fg="blue", font=('Times New Roman', 15, ' bold '))
# txt2.place(x=600 - x_cord, y=300 - y_cord)
#
# lbl3 = tk.Label(window, text="NOTIFICATION", width=20, fg="black", bg=bg1, height=2,
#                 font=('Times New Roman', 25, ' bold '))
# lbl3.place(x=1000- x_cord, y=200 - y_cord)
#
# message = tk.Label(window, text="", bg="white", fg="blue", width=32, height=1, activebackground="white",
#                    font=('Times New Roman', 15, ' bold '))
# message.place(x=1000 - x_cord, y=300 - y_cord)
#
# # lbl3 = tk.Label(window, text="ATTENDANCE", width=20, fg="white", bg="lightgreen", height=2,
# #                 font=('Times New Roman', 30, ' bold '))
# # lbl3.place(x=120, y=570 - y_cord)
#
# # message2 = tk.Label(window, text="", fg="red", bg="yellow", activeforeground="green", width=60, height=4,
# #                     font=('times', 15, ' bold '))
# # message2.place(x=700, y=570 - y_cord)
#
# lbl4 = tk.Label(window, text="STEP 1", width=26, fg="red", bg=bg1, height=2,
#                 font=('Times New Roman', 20, ' bold '))
# lbl4.place(x=200 - x_cord, y=375 - y_cord)
#
# lbl5 = tk.Label(window, text="STEP 2", width=26, fg="red", bg=bg1, height=2,
#                 font=('Times New Roman', 20, ' bold '))
# lbl5.place(x=600 - x_cord, y=375 - y_cord)
#
# lbl6 = tk.Label(window, text="STEP 3", width=26, fg="red", bg=bg1, height=2,
#                 font=('Times New Roman', 20, ' bold '))
# lbl6.place(x=1000 - x_cord, y=375 - y_cord)


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
    global StId
    StId = Id
    # StN = str(aa)
    # insertVariblesIntoTable(StId, StN)
    getid()
    cv2.destroyAllWindows()

def Cheack_Login():
    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='cla051063',
                         db='abes_db',
                         charset='utf8'
                         )
    cursor = db.cursor()
    sql = "SELECT student_id FROM Student WHERE student_id='%s'" % (StId)
    cursor.execute(sql) #sql语句被执行
    result = cursor.fetchone()#得到的结果返回给result数组
    if result:
        Borrow_frame()
    else:
        msg._show(title='错误！', message='您输入的用户不存在！请先注册！')
    print(StId)

def getid():
    return StId

def Borrow_frame():
    window2 = tk.Tk()
    window2.title('Borrow')
    window2.geometry('700x600')
    lable0 = tk.Label(window2, text=getid(), bg='pink', font=('微软雅黑', 50)).pack()  # 上
    window2.mainloop()

# def insertVariblesIntoTable(id, name):
#     try:
#         connection = mysql.connector.connect(host='localhost',
#                                              database='abes_db',
#                                              user='root',
#                                              password='cla051063')
#         cursor = connection.cursor()
#         mySql_insert_query = "insert into Student(student_id, student_name) values (%s, %s)"
#
#         recordTuple = (id, name)
#         cursor.execute(mySql_insert_query, recordTuple)
#         connection.commit()
#         print("Record inserted successfully into Student table")
#
#     except mysql.connector.Error as error:
#         print("Failed to insert into MySQL table {}".format(error))
#
#     finally:
#         if (connection.is_connected()):
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed")



def quit_window():
    MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        tk.messagebox.showinfo("Greetings", "Thank You very much for using our software. Have a nice day ahead!!")
        window.destroy()
# takeImg = tk.Button(window, text="Image Capture Button", command=TakeImages, fg=bg1, bg="blue", width=30,
#                     activebackground="pink", font=('Times New Roman', 15, ' bold '))
# takeImg.place(x=200 - x_cord, y=425 - y_cord)
# trainImg = tk.Button(window, text="Model Training Button", command=TrainImages, fg=bg1, bg="blue", width=30,
#                      activebackground="pink", font=('Times New Roman', 15, ' bold '))
# trainImg.place(x=600 - x_cord, y=425 - y_cord)
# trackImg = tk.Button(window, text="Test Face Button", command=TrackImages, fg=bg1, bg="red", width=30,
#                      activebackground="pink", font=('Times New Roman', 15, ' bold '))
# trackImg.place(x=1000 - x_cord, y=425 - y_cord)
# quitWindow = tk.Button(window, text="QUIT", command=quit_window, fg=bg1, bg="red", width=10,
#                        activebackground="pink", font=('Times New Roman', 15, ' bold '))
# quitWindow.place(x=700, y=735 - y_cord)
#
# window.mainloop()

if __name__ == '__main__':
    frame()