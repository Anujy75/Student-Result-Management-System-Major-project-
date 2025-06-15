from tkinter import *
from PIL import Image, ImageTk 
from tkinter import ttk, messagebox
import sqlite3

class StudentClass:
      def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1800x750+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #=========== Title ===========
        title = Label(self.root, text="Manage Student Details",
                      font=("goudy old style", 20, "bold"),
                      bg="#1253c9", fg="white").place(x=0, y=10, width=1800, height=40)  

        #=========== Variables ====================

        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar() 
        self.var_gender = StringVar()
        self.var_address = StringVar()
        self.var_dob = StringVar() 
        self.var_contact = StringVar() 
        self.var_course = StringVar() 
        self.var_a_date = StringVar() 
        self.var_city = StringVar()
        self.var_state = StringVar()
        self.var_pin = StringVar()
        self.var_category = StringVar()
        self.var_search = StringVar()      

        #=========== Labels/widgets ===========
        #=============column- 1=======================================================================================================
        lbl_roll= Label(self.root, text="Roll No.", font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=30, y=60)
        lbl_Name= Label(self.root, text="Name", font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=30, y=110)
        lbl_Email= Label(self.root, text="Email", font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=30, y=160)
        lbl_gender= Label(self.root, text="Gender", font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=30, y=210)
        lbl_course= Label(self.root, text="Course", font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=30, y=260)
        lbl_city= Label(self.root, text="City", font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=30, y=310)       
        lbl_address= Label(self.root, text="Address", font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=30, y=360)

        #================column-2====================================================================================================
        lbl_dob= Label(self.root, text="D.O.B", font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=420, y=60)
        lbl_contact= Label(self.root, text="Contact", font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=420, y=110)
        lbl_admission= Label(self.root, text="Enroll Date", font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=420, y=160)
        lbl_cotegory= Label(self.root, text="Cotegory", font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=420, y=210)
        lbl_state= Label(self.root, text="State", font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=420, y=260)
        lbl_pin= Label(self.root, text="Pin", font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=420, y=310)



        #=========== Input Fields ===========
        #=====================================col-1=================
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15, ), bg="lightyellow", fg="black")
        self.txt_roll.place(x=150, y=60, width=250, height=30)

        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15, ), bg="lightyellow", fg="black")
        self.txt_name.place(x=150, y=110, width=250, height=30)

        self.txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15, ), bg="lightyellow", fg="black")
        self.txt_email.place(x=150, y=160, width=250, height=30)
       

        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender, font=("goudy old style", 15, ),state='readonly', justify=CENTER, values=("Select", "Male", "Female", "Other"))
        self.txt_gender.place(x=150, y=210, width=250, height=30)
        self.txt_gender.current(0)

        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course, font=("goudy old style", 15, ),state='readonly', justify=CENTER, 
                                       values=("Select", "B.Tech (Computer Science)", "B.Tech (IT)", 
           "B.Tech (Electronics and Communication)", "B.Tech (EE)", "B.Tech (ME)", "B.Tech (CE)", 
           "B.Tech (CSE)", "B.Tech (Biotech)", "B.Tech (AIDS)", "B.Tech (CS)", "B.Tech (AE)", "B.Tech (AE)",
             "B.Sc (CS)", "B.Sc (Information Technology)","BCA (BCA)", "B.Sc (AIML)", "M.Tech (CS)", "M.Tech (IT)", 
           "M.Tech (E & C)", "M.Tech (ME)", "M.Tech (CE)", "M.Tech (EE)", "M.Tech (DS)", "M.Tech (AI)", 
           "M.Tech (Cyber Security)", "MCA ", "M.Sc (CS)", "M.Sc (IT)", "M.Sc (DSAI)", "MBA ", "MBA (IT & Systems)"))
        self.txt_course.place(x=150, y=260, width=250, height=30)
        self.txt_course.current(0)



        self.txt_city = Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15, ), bg="lightyellow", fg="black")
        self.txt_city.place(x=150, y=310, width=250, height=30)


        self.txt_address = Text(self.root,font=("goudy old style", 15, ), bg="lightyellow", fg="black")
        self.txt_address.place(x=150, y=360, width=650, height=100)




        #=====================================col-2============================================================================================
        self.txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, ), bg="lightyellow", fg="black")
        self.txt_dob.place(x=550, y=60, width=250, height=30)

        self.txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15, ), bg="lightyellow", fg="black")
        self.txt_contact.place(x=550, y=110, width=250, height=30)

        self.txt_admission = Entry(self.root, textvariable=self.var_a_date, font=("goudy old style", 15, ), bg="lightyellow", fg="black")
        self.txt_admission.place(x=550, y=160, width=250, height=30)

        self.txt_category = ttk.Combobox(self.root, textvariable=self.var_category, font=("goudy old style", 15, ),state='readonly', justify=CENTER,
                           values=("Select", "General", "OBC", "SC", "ST", "EWS", "Minority", "PWD", "Ex-Servicemen", 
                                    "NRI", "Foreign National", "Management Quota"))
        self.txt_category.place(x=550, y=210, width=250, height=30)
        self.txt_category.current(0)

        self.txt_state = ttk.Combobox(self.root, textvariable=self.var_state, font=("goudy old style", 15, ),state='readonly', justify=CENTER,
                                      values = ("Select", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
          "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", 
          "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", 
          "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", 
          "Uttar Pradesh", "Uttarakhand", "West Bengal"))
        self.txt_state.place(x=550, y=260, width=250, height=30)
        self.txt_state.current(0)

        self.txt_pin = Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15, ), bg="lightyellow", fg="black")
        self.txt_pin.place(x=550, y=310, width=250, height=30)

        #============================================buttons===================================================
        self.btn_add= Button(self.root, text = "Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2" , command=self.add)
        self.btn_add.place(x=180, y=500, width=150, height=50)
        self.btn_add= Button(self.root, text = "Update", font=("goudy old style", 15, "bold"), bg="#13ed3b", fg="white", cursor="hand2" , command=self.update)
        self.btn_add.place(x=360, y=500, width=150, height=50)
        self.btn_add= Button(self.root, text = "Delete", font=("goudy old style", 15, "bold"), bg="#e32323", fg="white", cursor="hand2", command=self.delete )
        self.btn_add.place(x=540, y=500, width=150, height=50)
        self.btn_add= Button(self.root, text = "Clear", font=("goudy old style", 15, "bold"), bg="#484F52", fg="white", cursor="hand2",command=self.clear)
        self.btn_add.place(x=720, y=500, width=150, height=50)

        #================================================search pannel=======================
        self.var_search = StringVar()
        lbl_search_roll =Label(self.root, text="Roll No.", font=("goudy old style", 16, "bold"),bg="white", fg="black").place(x=1000, y=60)
        txt_search_roll = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15,), bg="lightyellow", fg="black").place(x=1150, y=60, width=300, height=30)
        
        #==============================================search button========================================
        btn_search= Button(self.root, text = "Search", font=("goudy old style", 15, "bold"), bg="#1349D3", fg="white", cursor="hand2", command=self.search ).place(x=1470, y=60, width=180, height=30)
        
        #=======================================content===========================================
        self.C_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_frame.place(x= 1020, y= 120, width=650, height=350)

        #=============================scroll bar==================================================
        scrolly = Scrollbar(self.C_frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_frame, orient=HORIZONTAL)

        self.CourseTable =ttk.Treeview(self.C_frame,
                             columns=("roll", "name", "email", "gender", "category", "dob", "contact", "admission", "course", "state", "city", "pin", "address"), 
                            xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)


        self.CourseTable.heading("roll", text="Roll No.")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("email", text="Email")
        self.CourseTable.heading("gender", text="Gender")
        self.CourseTable.heading("category", text="Category")
        self.CourseTable.heading("dob", text="D.O.B")
        self.CourseTable.heading("dob", text="D.O.B")
        self.CourseTable.heading("contact", text="Contact")
        self.CourseTable.heading("admission", text="Admission")
        self.CourseTable.heading("course", text="Course")
        self.CourseTable.heading("state", text="State")
        self.CourseTable.heading("city", text="City")
        self.CourseTable.heading("pin", text="Pin")
        self.CourseTable.heading("address", text="Address")
       
       
        self.CourseTable["show"] = 'headings'
                
        self.CourseTable.column("roll", width=150)
        self.CourseTable.column("name", width=150)
        self.CourseTable.column("email", width=150)
        self.CourseTable.column("gender", width=150)
        self.CourseTable.column("category", width=150)
        self.CourseTable.column("dob", width=150)
        self.CourseTable.column("contact", width=150)
        self.CourseTable.column("admission", width=150)
        self.CourseTable.column("course", width=150)
        self.CourseTable.column("state", width=150)
        self.CourseTable.column("city", width=150)
        self.CourseTable.column("pin", width=150)
        self.CourseTable.column("address", width=150)
                               
        self.CourseTable.pack(fill = BOTH, expand=1)

        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

#==============================clear data=============================================  
     
      def clear(self):
          self.show()
          self.var_roll.set("")
          self.var_name.set("")
          self.var_email.set("")
          self.var_gender.set("Select")
          self.var_category.set("Select")
          self.var_dob.set("")
          self.var_contact.set("")
          self.var_a_date.set("")
          self.var_course.set("Select")
          self.var_state.set("Select")
          self.var_city.set("")
          self.var_pin.set("")
          self.txt_address.delete("1.0", END)
          self.var_search.set("")
          self.txt_roll.config(state = NORMAL)
#==========================delete function===================================================
      def delete(self):
        con=sqlite3.connect(database ="rms.db")
        cur = con.cursor()
        
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Roll number is required", parent=self.root)
            else:
                cur.execute("Select * from student where roll=?",(self.var_roll.get(),))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showerror("Error", "Please select the student from the list first", parent = self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete ?", parent = self.root)
                    if op == True:
                        cur.execute("delete from student where roll=?",( self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Student record deleted successfully", parent = self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

#=============================================================================

      def get_data(self, ev):
          self.txt_roll.config(state='readonly')
          r= self.CourseTable.focus()
          content=self.CourseTable.item(r)
          row = content["values"]
          self.var_roll.set(row[0])
          self.var_name.set(row[1])
          self.var_email.set(row[2])
          self.var_gender.set(row[3])
          self.var_category.set(row[4])
          self.var_dob.set(row[5])
          self.var_contact.set(row[6])
          self.var_a_date.set(row[7])
          self.var_course.set(row[8])
          self.var_state.set(row[9])
          self.var_city.set(row[10])
          self.var_pin.set(row[11])
          #self.var_address.set(row[0])
          self.txt_address.delete("1.0", END)
          self.txt_address.insert(END, row[12])

#==================================================================================
      def add(self):
        con=sqlite3.connect(database ="rms.db")
        cur = con.cursor()
        
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Roll number is required", parent=self.root)
            else:
                cur.execute("Select * from student where roll=?",(self.var_roll.get(),))
                row = cur.fetchone()
                if row !=None:
                    messagebox.showerror("Error", "student roll number already present", parent = self.root)
                else:
                    cur.execute("insert into student(roll, name, email, gender, category, dob, contact,admission, course, state, city, pin, address) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_category.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        #self.var_address.get()
                        self.txt_address.get("1.0", END).strip()

                    ))
                    con.commit()
                    messagebox.showinfo("success", "Student details added successfully", parent = self.root)
                    self.show()
                        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

#===============================================================================================================================

      def update(self):
        con=sqlite3.connect(database ="rms.db")
        cur = con.cursor()
        
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Roll number is required", parent=self.root)
            else:
                cur.execute("Select * from student where roll=?",(self.var_roll.get(),))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showerror("Error", "Select student from list", parent = self.root)
                else:
                    cur.execute("""update student set name=?, email=?, gender=?, category=?, 
                                dob=?, contact=?, admission=?, course=?, state=?, city=?, pin=?, 
                                address=? where roll=?""", (
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_category.get(),
                    self.var_dob.get(),
                    self.var_contact.get(),
                    self.var_a_date.get(),
                    self.var_course.get(),
                    self.var_state.get(),
                    self.var_city.get(),
                    self.var_pin.get(),
                    self.txt_address.get("1.0", END).strip(),
                    self.var_roll.get(),))

                    con.commit()
                    messagebox.showinfo("success", "Student details Update Successfully", parent = self.root)
                    self.show()
                        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
#========================================================================================================================           
      
      def show(self):
          con = sqlite3.connect(database="rms.db")
          cur = con.cursor()
          
          try:
              cur.execute("Select * from student")
              rows = cur.fetchall()
              self.CourseTable.delete(*self.CourseTable.get_children())
              for row in rows:
                  self.CourseTable.insert('', END, values=row)

          except Exception as ex:
              messagebox.showerror("Error", f"Error due to {str(ex)}")

#========================================================================================================================              
      def search(self):
          con = sqlite3.connect(database="rms.db")
          cur = con.cursor()
          
          try:
            cur.execute("Select * from student where roll=?", (self.var_search.get(),) )
            row = cur.fetchone()
            if row !=None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error","No record found")
            

          except Exception as ex:
              messagebox.showerror("Error", f"Error due to {str(ex)}")
             


if __name__ == "__main__":
    root = Tk()
    obj = StudentClass(root)
    root.mainloop()
