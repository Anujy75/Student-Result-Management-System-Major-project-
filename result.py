from tkinter import *
from PIL import Image, ImageTk 
from tkinter import ttk, messagebox
import sqlite3

class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1800x750+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #================================ Title========================= ===========
        title = Label(self.root, text="Add Student Results",font=("Times New Roman", 25, "bold"),bg="orange", fg="#262626").place(x=0, y=10, width=1800, height=60)

        #=======================variables========================================
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_totalmarks= StringVar()
        self.var_select = StringVar()
        self.roll_list = []
        self.fetch_roll()

        #======================   Labels  ==========================================
        lbl_select = Label(self.root, text="Select Student", font=("Times New Roman", 20, "bold"), bg="white", fg="#262626").place(x=50, y=100)
        lbl_sname = Label(self.root, text="Name", font=("Times New Roman", 20, "bold"), bg="white", fg="#262626").place(x=50, y=180)
        lbl_course = Label(self.root, text="Course", font=("Times New Roman", 20, "bold"), bg="white", fg="#262626").place(x=50, y=260)
        lbl_marks = Label(self.root, text="Marks Obtained", font=("Times New Roman", 20, "bold"), bg="white", fg="#262626").place(x=50, y=340)
        lbl_totalmarks = Label(self.root, text="Full Marks", font=("Times New Roman", 20, "bold"), bg="white", fg="#262626").place(x=50, y=420)

        #=========================  Entry section   ===========================
        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, font=("Times New Roman", 15, ),state='readonly', justify=CENTER, values=self.roll_list)
        self.txt_student.place(x=300, y=100, width=250, height=40)
        self.txt_student.set("Select")

        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("Times New Roman", 18, ), bg="lightyellow", fg="black", state='readonly').place(x=300, y=180, width=430, height=40)
        self.txt_course = Entry(self.root, textvariable=self.var_course, font=("Times New Roman", 18, ), bg="lightyellow", fg="black", state='readonly').place(x=300, y=260, width=430, height=40)
        self.txt_marks = Entry(self.root, textvariable=self.var_marks, font=("Times New Roman", 18, ), bg="lightyellow", fg="black").place(x=300, y=340, width=430, height=40)
        self.txt_totalmark = Entry(self.root, textvariable=self.var_totalmarks, font=("Times New Roman", 18, ), bg="lightyellow", fg="black").place(x=300, y=420, width=430, height=40)

        #========================search panel==========================
        self.var_search = StringVar()
        btn_search= Button(self.root, text = "Search", font=("Times New Roman", 15, "bold"), bg="#1349D3", fg="white", cursor="hand2",command=self.search ).place(x=580, y=100, width=150, height=40)

        #========================buttons=========================
        self.btn_add= Button(self.root, text = "Submit", font=("Times New Roman", 20, "bold"), bg="#20EA60", fg="#262626", cursor="hand2",command=self.add)
        self.btn_add.place(x=330, y=500, width=150, height=40)
        self.btn_clear= Button(self.root, text = "Clear", font=("Times New Roman", 20, "bold"), bg="#404445", fg="white", cursor="hand2" , command=self.clear)
        self.btn_clear.place(x=530, y=500, width=150, height=40)

        #=============content window===========
        self.bg_img = Image.open("image/result.jpeg")
        self.bg_img = self.bg_img.resize((1200, 600),)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self_bg = Label(self.root, image = self.bg_img).place(x=750, y=120, width= 1200, height= 600)

    # ========= Yehi main change hai ========== 
    def fetch_roll(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        try:
            cur.execute("select roll from student")
            rows = cur.fetchall()
            if len(rows) > 0:
                self.roll_list.clear()
                for row in rows:
                    self.roll_list.append(row[0])
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
#================================================================================================
    def search(self):
          con = sqlite3.connect(database="rms.db")
          cur = con.cursor()
          
          try:
            cur.execute("Select name, course from student where roll=?", (self.var_roll.get(),) )
            row = cur.fetchone()
            if row !=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No record found")
            

          except Exception as ex:
              messagebox.showerror("Error", f"Error due to {str(ex)}")
    

  #===========================================================================================================
    def add(self):
        con=sqlite3.connect(database ="rms.db")
        cur = con.cursor()
        
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error", "Please first search student record", parent=self.root)
            else:
                cur.execute("Select * from RESULT where roll=? and course=?",(self.var_roll.get(), self.var_course.get()))
                row = cur.fetchone()
                if row !=None:
                    messagebox.showerror("Error", "Result already present", parent = self.root)
                else:
                    pct = (int(self.var_marks.get())*100)/(int(self.var_totalmarks.get()))
                    cur.execute("insert into result(roll, name, course, marks_ob, totalmarks, pct) values(?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_totalmarks.get(),
                        str(pct)
                    ))

                    con.commit()
                    messagebox.showinfo("success", "result added successfully", parent = self.root)
                        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


#===================================================================================
    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_totalmarks.set("")






if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()
