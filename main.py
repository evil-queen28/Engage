from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime
from chatbot import ChatBot
from face_reco import Face_Reco
from student import Student
from train import Train
from chatbot import ChatBot
from attendance import Attendance

#from student import Student
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1566x860+0+0")
        self.root.title("Face_Recogonition_System")
        
# This part is image labels setting start 
        # first header image  
        img=Image.open(r"Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)
        
 # background image 
        bg1=Image.open(r"Images_GUI\bg3.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)
        #title section
        title_lb1 = Label(bg_img,text="Attendance Management System Using Facial Recognition",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)
# Create buttons below the section 
        
        
            
        # student button 1
        std_img_btn=Image.open(r"Images_GUI\std1.jpg")
        std_img_btn=std_img_btn.resize((200,200),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        #time
        
        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=330,y=100,width=200,height=180)

        std_b1_1 = Button(bg_img,command=self.student_pannels, text="Student Pannel",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=330,y=280,width=200,height=45)
        
        # Detect Face  button 2
        det_img_btn=Image.open(r"Images_GUI\det1.jpg")
        det_img_btn=det_img_btn.resize((200,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_recog,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=570,y=100,width=200,height=180)

        det_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=570,y=280,width=200,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"Images_GUI\att.jpg")
        att_img_btn=att_img_btn.resize((200,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=810,y=100,width=200,height=180)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=810,y=280,width=200,height=45)

        
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
         # Train   button 5
        tra_img_btn=Image.open(r"Images_GUI\tra1.jpg")
        tra_img_btn=tra_img_btn.resize((200,180),Image.ANTIALIAS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=330,y=330,width=200,height=180)

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Train Data",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        tra_b1_1.place(x=330,y=510,width=200,height=45)

        # Photo   button 6
        photo_img_btn=Image.open(r"Images_GUI\chatbot1.jpg")
        photo_img_btn=photo_img_btn.resize((200,180),Image.ANTIALIAS)
        self.photos_img1=ImageTk.PhotoImage(photo_img_btn)


        pho_b1 = Button(bg_img,command=self.ChatBot,image=self.photos_img1,cursor="hand2")
        pho_b1.place(x=570,y=330,width=200,height=180)

        pho_b1_1 = Button(bg_img,command=self.ChatBot,text="Chat Bot",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        pho_b1_1.place(x=570,y=510,width=200,height=45)

        # exit   button 8
        exi_img_btn=Image.open(r"Images_GUI\exi.jpg")
        exi_img_btn=exi_img_btn.resize((200,180),Image.ANTIALIAS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.iExit,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=810,y=330,width=200,height=180)

        exi_b1_1 = Button(bg_img,command=self.iExit,text="Exit",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=810,y=510,width=200,height=45)

# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("Data")
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure want to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return    
        # ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_recog(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Reco(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def ChatBot(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)
    
    def Close(self):
        root.destroy()
   
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()