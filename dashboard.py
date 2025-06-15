from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os
from clock import clockClass

from course import CourseClass
from student import StudentClass
from result import resultClass
from report import reportClass
from login import Login_window
class Main:
  def __init__(self, root):
    self.root = root
    self.root.title("Student Result Management System")
    self.root.geometry("1500x1000+0+0")
    self.root.state('zoomed')
    self.root.config(bg ="white")


    #=================icons================
    self.logo_dash = ImageTk.PhotoImage(file = "image/logo1_dash.png") 
    #================title=================
    title  = Label(self.root, text = "Student Result Management System",
                    font= ("goudy old style", 30, "bold"), image = self.logo_dash, compound = LEFT, padx = 12,
                    bg ="#1253c9", fg="white").place(x=0, y =0, relwidth=1, height=70)
    
    #====================menu===================
    M_frame = LabelFrame(self.root, text = "Menu", font=("times new roman", 15), bg = "white")
    M_frame.place(x=10, y=70, width = 1900, height = 80)

    btn_course = Button(M_frame, text="Course", font=("goudy old style", 15, "bold"),
                          bg = "#0b5377", fg="white", cursor="hand2", command=self.add_course).place(x= 20, y =5, width = 220, height = 40)
    btn_student = Button(M_frame, text="Student", font=("goudy old style", 15, "bold"),
                      bg = "#0b5377", fg="white", cursor="hand2", command=self.add_student).place(x= 320, y =5, width = 220, height = 40) 
    btn_result = Button(M_frame, text="Result", font=("goudy old style", 15, "bold"),
                      bg = "#0b5377", fg="white", cursor="hand2", command=self.add_result).place(x= 640, y =5, width = 220, height = 40) 
    btn_view = Button(M_frame, text="View Student Result", font=("goudy old style", 15, "bold"),
                      bg = "#0b5377", fg="white", cursor="hand2", command=self.add_report).place(x= 960, y =5, width = 220, height = 40) 
    btn_logout = Button(M_frame, text="Logout", font=("goudy old style", 15, "bold"),
                      bg = "#0b5377", fg="white", cursor="hand2",  command=self.logout).place(x= 1280, y =5, width = 220, height = 40) 
    btn_exit = Button(M_frame, text="Exit", font=("goudy old style", 15, "bold"),
                      bg = "#0b5377", fg="white", cursor="hand2",command=self.exit_).place(x= 1600, y =5, width = 220, height = 40) 
  
    #=============content window===========
    self.bg_img = Image.open("image/bg1.jpeg") 
    self.bg_img = self.bg_img.resize((1500, 600),)
    self.bg_img = ImageTk.PhotoImage(self.bg_img)

    self_bg = Label(self.root, image = self.bg_img).place(x=500, y=200, width= 1500, height= 600)

    #=========update details==========
    self.lbl_course = Label(self.root, text = "Total Course\n[0]", font=("goudy old style", 20),bd =10, bg = "#67726E",fg ="white", relief=RIDGE)
    self.lbl_course.place(x= 520, y = 800, width = 400, height = 100)

    self.lbl_student = Label(self.root, text = "Total Students\n[0]", font=("goudy old style", 20), bd =10, bg = "#13A2E4",fg ="white", relief=RIDGE)
    self.lbl_student.place(x= 1000, y = 800, width = 400, height = 100)

    self.lbl_result = Label(self.root, text = "Total Result\n[0]", font=("goudy old style", 20), bd =10, bg = "#1FF045",fg ="white", relief=RIDGE)
    self.lbl_result.place(x= 1500, y = 800, width = 400, height = 100)
    
    #================footer=================
    footer  = Label(self.root, text = "SRMS-Student Result Management System\nContact us for any Technical Issue: 9721xxxx67",
                    font= ("goudy old style", 10,), padx = 12,
                    bg ="#262626", fg="white").pack(side= BOTTOM, fill = X)
    self.update_details()

#====================update real time details==================================
  
  def update_details(self):
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()
    
    try:
        cur.execute("Select * from course")
        cr = cur.fetchall()
        self.lbl_course.config(text=f"Total Courses[{str(len(cr))}]")

        cur.execute("SELECT * FROM student")
        st = cur.fetchall()
        self.lbl_student.config(text=f"Total Student\n[{str(len(st))}]")

        cur.execute("SELECT * FROM result")
        rs = cur.fetchall()
        self.lbl_result.config(text=f"Total Result\n[{str(len(rs))}]")


        self.lbl_course.after(200, self.update_details)
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to {str(ex)}")


#======================clock positioning====================================================================    
    clock_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
    clock_frame.place(x=20, y=200, width=500, height=700)
    self.clock = clockClass(clock_frame)
#==================================================================================
  def add_course(self):
    self.new_win = Toplevel(self.root)
    self.new_obj = CourseClass(self.new_win)

  def add_student(self):
    self.new_win = Toplevel(self.root)
    self.new_obj = StudentClass(self.new_win)


  def add_result(self):
    self.new_win = Toplevel(self.root)
    self.new_obj = resultClass(self.new_win)   

  def add_report(self):
    self.new_win = Toplevel(self.root)
    self.new_obj = reportClass(self.new_win)

  def add_login(self):
    self.new_win = Toplevel(self.root)
    self.new_obj = Login_window(self.new_win)     

  def logout(self):
    op = messagebox.askyesno("Confirm", "Do you really want to logout?", parent= self.root)
    if op == True:
      self.root.destroy()
      os.system("python login.py")

  def exit_(self):
    op = messagebox.askyesno("Confirm", "Do you really want to Exit?", parent= self.root)
    if op == True:
      self.root.destroy()


if __name__=="__main__":
  root = Tk()
  obj = Main(root)
  root.mainloop()