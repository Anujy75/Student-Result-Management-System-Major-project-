from tkinter import *
from PIL import Image, ImageTk 
from tkinter import ttk, messagebox
import sqlite3

class CourseClass:
      def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1800x750+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #=========== Title ===========
        title = Label(self.root, text="Manage Course Details",
                      font=("goudy old style", 20, "bold"),
                      bg="#1253c9", fg="white").place(x=0, y=10, width=1800, height=40)  

        #=========== Variables ===========
        self.var_course = StringVar()
        self.var_duration = StringVar() 
        self.var_charges = StringVar()  

        #=========== Labels ===========
        Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"),
              bg="white", fg="black").place(x=30, y=60)
        Label(self.root, text="Duration", font=("goudy old style", 15, "bold"),
              bg="white", fg="black").place(x=30, y=110)
        Label(self.root, text="Charge", font=("goudy old style", 15, "bold"),
              bg="white", fg="black").place(x=30, y=160)
        Label(self.root, text="Description", font=("goudy old style", 15, "bold"),
              bg="white", fg="black").place(x=30, y=210)

        #=========== Input Fields ===========
        self.txt_courseName = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15, ), bg="lightyellow", fg="black")
        self.txt_courseName.place(x=180, y=60, width=250, height=40)

        self.txt_duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, ), bg="lightyellow", fg="black")
        self.txt_duration.place(x=180, y=110, width=250, height=40)

        self.txt_charges = Entry(self.root, textvariable=self.var_charges, font=("goudy old style", 15, ), bg="lightyellow", fg="black")
        self.txt_charges.place(x=180, y=160, width=250, height=40)

        self.txt_description = Text(self.root, font=("goudy old style", 15, ), bg="lightyellow", fg="black")
        self.txt_description.place(x=180, y=210, width=600, height=150)


        #===========buttons=========================
        self.btn_add= Button(self.root, text = "Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2" , command=self.add)
        self.btn_add.place(x=180, y=400, width=150, height=50)
        self.btn_add= Button(self.root, text = "Update", font=("goudy old style", 15, "bold"), bg="#13ed3b", fg="white", cursor="hand2" , command=self.update)
        self.btn_add.place(x=360, y=400, width=150, height=50)
        self.btn_add= Button(self.root, text = "Delete", font=("goudy old style", 15, "bold"), bg="#e32323", fg="white", cursor="hand2", command=self.delete )
        self.btn_add.place(x=540, y=400, width=150, height=50)
        self.btn_add= Button(self.root, text = "Clear", font=("goudy old style", 15, "bold"), bg="#484F52", fg="white", cursor="hand2",command=self.clear)
        self.btn_add.place(x=720, y=400, width=150, height=50)

        #==========search pannel=======================
        self.var_search = StringVar()
        lbl_search_courseName =Label(self.root, text="Course Name: ", font=("goudy old style", 16, "bold"),bg="white", fg="black").place(x=1000, y=60)
        txt_search_courseName = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15,), bg="lightyellow", fg="black").place(x=1150, y=60, width=300, height=40)
        
        #==========search button========================
        btn_search= Button(self.root, text = "Search", font=("goudy old style", 15, "bold"), bg="#1349D3", fg="white", cursor="hand2", command=self.search ).place(x=1470, y=60, width=180, height=40)
        
        #================content=========================
        self.C_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_frame.place(x= 1020, y= 120, width=650, height=350)

        #========scroll bar==================
        scrolly = Scrollbar(self.C_frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_frame, orient=HORIZONTAL)

        self.CourseTable =ttk.Treeview(self.C_frame, columns=("cid", "name", "duration", "charges", "description"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)


        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("name", text="name")
        self.CourseTable.heading("duration", text="duration")
        self.CourseTable.heading("charges", text="charges")
        self.CourseTable.heading("description", text="description")
        self.CourseTable["show"] = 'headings'

        self.CourseTable.column("cid", width= 50)
        self.CourseTable.column("name", width= 100)
        self.CourseTable.column("duration", width= 100)
        self.CourseTable.column("charges", width= 100)
        self.CourseTable.column("description", width= 150 )                               
        self.CourseTable.pack(fill = BOTH, expand=1)

        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

#===========================================================================  
# #===========================================================================     
      def clear(self):
          self.show()
          self.var_course.set("")
          self.var_charges.set("")
          self.var_duration.set("")
          self.var_search.set("")
          self.txt_description.delete("1.0", END)
          self.txt_courseName.config(state=NORMAL)
#=============================================================================
      def delete(self):
        con=sqlite3.connect(database ="rms.db")
        cur = con.cursor()
        
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error", "Course name should be required", parent=self.root)
            else:
                cur.execute("Select * from course where name=?",(self.var_course.get(),))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showerror("Error", "Please select the course from the list first", parent = self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete ?", parent = self.root)
                    if op == True:
                        cur.execute("delete from course where name=?",( self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Course delete successfully", parent = self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

#=============================================================================

      def get_data(self, ev):
          self.txt_courseName.config(state='readonly')
          self.txt_courseName
          r= self.CourseTable.focus()
          content=self.CourseTable.item(r)
          row = content["values"]
          #print(row)
          self.var_course.set(row[1])
          self.var_duration.set(row[2])
          self.var_charges.set(row[3])
          self.txt_description.delete("1.0", END)
          self.txt_description.insert(END, row[4])
#==================================================================================
      def add(self):
        con=sqlite3.connect(database ="rms.db")
        cur = con.cursor()
        
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error", "Course name should be required", parent=self.root)
            else:
                cur.execute("Select * from course where name=?",(self.var_course.get(),))
                row = cur.fetchone()
                if row !=None:
                    messagebox.showerror("Error", "Course name already present", parent = self.root)
                else:
                    cur.execute("insert into course(name, duration, charges, description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END)

                    ))
                    con.commit()
                    messagebox.showinfo("success", "course added successfully", parent = self.root)
                    self.show()
                        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

#===============================================================================================================================

      def update(self):
        con=sqlite3.connect(database ="rms.db")
        cur = con.cursor()
        
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error", "Course name should be required", parent=self.root)
            else:
                cur.execute("Select * from course where name=?",(self.var_course.get(),))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showerror("Error", "Select Course from list", parent = self.root)
                else:
                    cur.execute("update course set duration=?, charges=?, description=? where name=?",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END),
                        self.var_course.get()))
                    
                    con.commit()
                    messagebox.showinfo("success", "Course Update Successfully", parent = self.root)
                    self.show()
                        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
#========================================================================================================================           
      
      def show(self):
          con = sqlite3.connect(database="rms.db")
          cur = con.cursor()
          
          try:
              cur.execute("Select * from course")
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
              cur.execute(f"Select * from course where name LIKE '%{self.var_search.get()}%'")
              rows = cur.fetchall()
              self.CourseTable.delete(*self.CourseTable.get_children())
              for row in rows:
                  self.CourseTable.insert('', END, values=row)

          except Exception as ex:
              messagebox.showerror("Error", f"Error due to {str(ex)}")
             



if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()


