from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import mysql.connector
import cv2
import numpy as np

class Train:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Pannel")
 #title section
        title_lb1 = Label(self.root,text="Welcome to Training Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1356,height=50)
        
        # This part is image labels setting start 
        # first header image  
        img_top=Image.open(r"Images_GUI\train_top.jpeg")
        img_top=img_top.resize((1400,280),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=1400,height=280)
        
        
        std_b1_1 = Button(self.root,command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("tahoma",30,"bold"),bg="blue",fg="red")
        std_b1_1.place(x=0,y=345,width=1530,height=65)
        
        # backgorund image 
        
        img_bottom=Image.open(r"Images_GUI\Train_bottom.jpeg")
        img_bottom=img_top.resize((1400,280),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg_bottom)
        f_lb1.place(x=0,y=420,width=1400,height=280)

       

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        

       
        

    # ==================Create Function of Traing===================
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Train Classifier=============

        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed!")




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()