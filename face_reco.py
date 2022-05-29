#import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

import mysql.connector
import cv2

import numpy as np
from tkinter import messagebox

from time import strftime
from datetime import datetime
class Face_Reco:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Pannel")

        # This part is image labels setting start 
        # first header image  
        title_lb1 = Label(self.root,text="Face Recognition",font=("verdana",30,"bold"),bg="darkblue",fg="red")
        title_lb1.place(x=0,y=0,width=1370,height=50)
        
        # This part is image labels setting start 
        # first header image  
        img_top=Image.open(r"Images_GUI\face1.jpeg")
        img_top=img_top.resize((580,660),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=50,width=580,height=660)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\face2.jpeg")
        bg1=bg1.resize((840,660),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=580,y=50,width=840,height=660)


        

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
       

        

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="dark green",fg="white")
        std_b1_1.place(x=315,y=580,width=200,height=40)
    
    
    #=============Attendance=============
    def mark_attendance(self,i,r,n):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)) :
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")


    #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host='localhost',username='root', password='root',database='face_recognition')
                cursor = conn.cursor()

                cursor.execute("select Name from student where Student_id="+str(id))
                n=cursor.fetchone()
                n="+".join(n)

                cursor.execute("select Roll from student where Student_id="+str(id))
                r=cursor.fetchone()
                r="+".join(r)

                cursor.execute("select Dep from student where Student_id="+str(id))
                i=cursor.fetchone()
                i="+".join(i)


                if confidence > 77:
                    cv2.putText(img,f"Dep:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,225),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,225),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,225),3)
                    self.mark_attendance(i,r,n)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face ",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord    

 
         
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_Reco(root)
    root.mainloop()