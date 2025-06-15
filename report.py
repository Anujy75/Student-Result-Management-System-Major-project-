from tkinter import *
from PIL import Image, ImageTk 
from tkinter import ttk, messagebox
import sqlite3

class reportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1800x750+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #==================================================variables===========================================
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_totalmarks= StringVar()
        self.var_select = StringVar()
        self.var_search = StringVar()
        self.var_id =""
        #================================ Title========================= ===========
        title = Label(self.root, text="View Student Result",font=("Times New Roman", 25, "bold"),bg="orange", fg="#262626").place(x=0, y=10, width=1800, height=60)

        #========================search==========================

        lbl_search = Label(self.root, text="Search By | Roll No. ", font=("Times New Roman", 20, "bold"), bg="white", fg="#262626").place(x=500, y=150)
        self.txt_search = Entry(self.root, textvariable=self.var_search, font=("Times New Roman", 18, ), bg="lightyellow", fg="black",).place(x=750, y=150, width=180, height=40)
        btn_search= Button(self.root, text = "Search", font=("Times New Roman", 15, "bold"), bg="#1349D3", fg="white", cursor="hand2", command=self.search).place(x=940, y=150, width=120, height=40)
        btn_clear= Button(self.root, text = "Clear", font=("Times New Roman", 15, "bold"), bg="#393B3D", fg="white", cursor="hand2", command=self.clear).place(x=1070, y=150, width=120, height=40)


        #===========================================Result Labels =======================================
        lbl_roll = Label(self.root, text="Roll No.", font=("Times New Roman", 18, "bold"), bg="white", fg="black", bd=2, relief=GROOVE).place(x=400, y=250, width=150, height=50)
        lbl_name = Label(self.root, text="Name", font=("Times New Roman", 18, "bold"), bg="white", fg="black", bd=2, relief=GROOVE).place(x=540, y=250, width=150, height=50)
        lbl_course = Label(self.root, text="Course", font=("Times New Roman", 18, "bold"), bg="white", fg="black", bd=2, relief=GROOVE).place(x=680, y=250, width=150, height=50)
        lbl_marks = Label(self.root, text="Marks Obtained", font=("Times New Roman", 18, "bold"), bg="white", fg="black", bd=2, relief=GROOVE).place(x=820, y=250, width=250, height=50)
        lbl_totalmarks = Label(self.root, text="Total Marks", font=("Times New Roman", 18, "bold"), bg="white", fg="black", bd=2, relief=GROOVE).place(x=1060, y=250, width=150, height=50)
        lbl_pct = Label(self.root, text="Percentage", font=("Times New Roman", 18, "bold"), bg="white", fg="black", bd=2, relief=GROOVE).place(x=1205, y=250, width=150, height=50)
        
        self.roll = Label(self.root, font=("Times New Roman", 18, "bold"), bg="white", fg="black", bd=2, relief=GROOVE)
        self.roll.place(x=400, y=295, width=150, height=50)
        self.name = Label(self.root, font=("Times New Roman", 18, "bold"), bg="white", fg="black", bd=2, relief=GROOVE)
        self.name.place(x=540, y=295, width=150, height=50)
        self.course = Label(self.root,  font=("Times New Roman", 18, "bold"), bg="white", fg="black", bd=2, relief=GROOVE)
        self.course.place(x=680, y=295, width=150, height=50)
        self.marks = Label(self.root,  font=("Times New Roman", 18, "bold"), bg="white", fg="black", bd=2, relief=GROOVE)
        self.marks.place(x=820, y=295, width=250, height=50)
        self.totalmarks = Label(self.root, font=("Times New Roman", 18, "bold"), bg="white", fg="black", bd=2, relief=GROOVE)
        self.totalmarks.place(x=1060, y=295, width=150, height=50)
        self.pct = Label(self.root,  font=("Times New Roman", 18, "bold"), bg="white", fg="black", bd=2, relief=GROOVE)
        self.pct.place(x=1205, y=295, width=150, height=50)

        #========================delete button==============================

        lbl_delete = Button(self.root, text="Delete", font=("Times New Roman", 20, "bold"), bg="red", fg="white", cursor="hand2", command=self.delete).place(x=800, y=400, width=150, height=50)
        
       #=====================seach function========================================

    def search(self):
          con = sqlite3.connect(database="rms.db")
          cur = con.cursor()
          
          try:
            if self.var_search.get()=="":
                messagebox.showerror("Error", "Roll Number is required", parent = self.root)
            else:
                cur.execute("Select * from result where roll=?", (self.var_search.get(),) )
                row = cur.fetchone()
                if row !=None:
                    self.var_id =row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.totalmarks.config(text=row[5])
                    self.pct.config(text=row[6])
                    
                else:
                    messagebox.showerror("Error","No record found")
            

          except Exception as ex:
              messagebox.showerror("Error", f"Error due to {str(ex)}")
  

  #===========================clear========================================================
    def clear(self):
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.totalmarks.config(text="")
        self.pct.config(text="")
        self.var_search.set("")
        self.var_id =""

 #=========================== Delete ========================================================

    def delete(self):
        con=sqlite3.connect(database ="rms.db")
        cur = con.cursor()
        
        try:
            if self.var_id=="":
                messagebox.showerror("Error", "Search student result first", parent=self.root)
            else:
                cur.execute("Select * from result where rid=?",(self.var_id,))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showerror("Error", "Invalid Student Result", parent = self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete ?", parent = self.root)
                    if op == True:
                        cur.execute("delete from result where rid=?",( self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete", "Result deleted successfully", parent = self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")







if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()
