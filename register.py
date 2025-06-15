from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os

class registerClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1500x1000+0+0")
        self.root.config(bg="#22345B")
        self.root.state("zoomed")
        self.root.focus_force()

        title = Label(self.root, font=("goudy old style", 20, "bold"),
                      bg="#355186", fg="white").place(x=0, y=10, relwidth=1, relheight=1)
        title = Label(self.root, text="Registration Window", font=("goudy old style", 20, "bold"),
            bg="#0860EE", fg="white").place(x=0, y=0, relwidth=1, height=50)

        self.bg = ImageTk.PhotoImage(file="image/newbg.png")
        bg = Label(self.root, image=self.bg).place(x=500, y=50, height=800, width=1500)

        self.left = ImageTk.PhotoImage(file="image/reg.png")
        left = Label(self.root, image=self.left).place(x=400, y=150, height=600, width=500)

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=900, y=150, width=750, height=600)

        Label(frame1, text="REGISTER HERE", font=("Times New Roman", 20, "bold"), bg="white", fg="green").place(x=50, y=30)

        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_select = StringVar()
        self.var_answer = StringVar()
        self.var_password = StringVar()
        self.var_cpassword = StringVar()
        self.var_check = IntVar()

        Label(frame1, text="First Name", font=("Times New Roman", 15, "bold"), bg="white").place(x=50, y=90)
        self.txt_fname = Entry(frame1, font=("Times New Roman", 15), bg="lightgray", textvariable=self.var_fname)
        self.txt_fname.place(x=50, y=120, width=250)

        Label(frame1, text="Last Name", font=("Times New Roman", 15, "bold"), bg="white").place(x=350, y=90)
        self.txt_lname = Entry(frame1, font=("Times New Roman", 15), bg="lightgray", textvariable=self.var_lname)
        self.txt_lname.place(x=350, y=120, width=250)

        Label(frame1, text="Contact", font=("Times New Roman", 15, "bold"), bg="white").place(x=50, y=160)
        self.txt_contact = Entry(frame1, font=("Times New Roman", 15), bg="lightgray", textvariable=self.var_contact)
        self.txt_contact.place(x=50, y=190, width=250)

        Label(frame1, text="Email", font=("Times New Roman", 15, "bold"), bg="white").place(x=350, y=160)
        self.txt_email = Entry(frame1, font=("Times New Roman", 15), bg="lightgray", textvariable=self.var_email)
        self.txt_email.place(x=350, y=190, width=250)

        Label(frame1, text="Security Question", font=("Times New Roman", 15, "bold"), bg="white").place(x=50, y=230)
        self.txt_select = ttk.Combobox(frame1, font=("Times New Roman", 15), state='readonly', justify=CENTER, textvariable=self.var_select,
                                       values=("Select", "What was your childhood nickname?",
                                                "What was the name of your first pet?", 
                                                "In which city were you born?", 
                                                "What is your favorite book?", 
                                                "What is your favorite game?"))
        self.txt_select.place(x=50, y=260, width=250, height=30)
        self.txt_select.current(0)

        Label(frame1, text="Security Answer", font=("Times New Roman", 15, "bold"), bg="white").place(x=350, y=230)
        self.txt_answer = Entry(frame1, font=("Times New Roman", 15), bg="lightgray", textvariable=self.var_answer)
        self.txt_answer.place(x=350, y=260, width=250)

        Label(frame1, text="Password", font=("Times New Roman", 15, "bold"), bg="white").place(x=50, y=300)
        self.txt_password = Entry(frame1, font=("Times New Roman", 15), bg="lightgray", textvariable=self.var_password, show="*")
        self.txt_password.place(x=50, y=330, width=250)

        Label(frame1, text="Confirm Password", font=("Times New Roman", 15, "bold"), bg="white").place(x=350, y=300)
        self.txt_cpassword = Entry(frame1, font=("Times New Roman", 15), bg="lightgray", textvariable=self.var_cpassword, show="*")
        self.txt_cpassword.place(x=350, y=330, width=250)

        Checkbutton(frame1, text="I Agree to the Terms & Conditions", variable=self.var_check, bg="white",
                    font=("Times New Roman", 15)).place(x=70, y=400)

        Button(self.root, text="Sign In", font=("goudy old style", 25, "bold"), bg="#2196f3", fg="white", command=self.login_window).place(x=550, y=598, width=250, height=55)
        Button(self.root, text="Register Now →", font=("Segoe UI", 22, "bold"), bg="green", fg="white", command=self.register_data).place(x=1000, y=600, width=320, height=55)

    def login_window(self):
        self.root.destroy()
        os.system("python login.py")

    def register_data(self):
        if (self.var_fname.get() == "" or self.var_contact.get() == "" or self.var_email.get() == ""
                or self.var_select.get() == "Select" or self.var_answer.get() == ""
                or self.var_password.get() == "" or self.var_cpassword.get() == ""):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_password.get() != self.var_cpassword.get():
            messagebox.showerror("Error", "Passwords do not match", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to the Terms & Conditions!", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS employee (f_name TEXT, l_name TEXT, contact TEXT, email TEXT PRIMARY KEY, question TEXT, answer TEXT, password TEXT)")
                cur.execute("SELECT * FROM employee WHERE email=?", (self.var_email.get(),))
                row = cur.fetchone()
                if row:
                    messagebox.showerror("Error", "User already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO employee (f_name, l_name, contact, email, question, answer, password) VALUES (?,?,?,?,?,?,?)", (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_select.get(),
                        self.var_answer.get(),
                        self.var_password.get(),
                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration successful", parent=self.root)
                    self.login_window()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = registerClass(root)
    root.mainloop()
