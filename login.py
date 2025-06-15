from tkinter import *
import time
import math
import sqlite3
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import os
#from dashboard import Main


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1500x1200+0+0")
        self.root.config(bg="grey")
        self.root.state("zoomed")
        self.root.focus_force()

        # Variables
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_select = StringVar()
        self.var_answer = StringVar()
        self.var_newpass = StringVar()

        # ================== Login Frame ===================
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=600, y=75, width=750, height=550)

        Label(login_frame, text="User Name", font=("Times New Roman", 20, "bold"), bg="white", fg="#262626").place(x=200, y=100)
        Entry(login_frame, textvariable=self.var_email, font=("Times New Roman", 18), bg="lightgray").place(x=200, y=140, width=400)

        Label(login_frame, text="Password", font=("Times New Roman", 20, "bold"), bg="white", fg="#262626").place(x=200, y=210)
        Entry(login_frame, textvariable=self.var_password, font=("Times New Roman", 18), bg="lightgray", show="*").place(x=200, y=250, width=400)

        Label(login_frame, text="Register New Account?", font=("Times New Roman", 15, "bold"), bg="white", fg="#0E20E5", cursor="hand2").place(x=200, y=320)
        Label(login_frame, text="Forget Password?", font=("Times New Roman", 15, "bold"), bg="white", fg="#F10814", cursor="hand2").place(x=420, y=320)

        # Binding for register and forget password
        Label(login_frame, text="Register New Account?", font=("Times New Roman", 15, "bold"), bg="white", fg="#0E20E5", cursor="hand2").place(x=200, y=320)
        reg_label = Label(login_frame, text="Register New Account?", font=("Times New Roman", 15, "bold"), bg="white", fg="#0E20E5", cursor="hand2")
        reg_label.place(x=200, y=320)
        reg_label.bind("<Button-1>", self.register_window)

        forget_label = Label(login_frame, text="Forget Password?", font=("Times New Roman", 15, "bold"), bg="white", fg="#F10814", cursor="hand2")
        forget_label.place(x=420, y=320)
        forget_label.bind("<Button-1>", self.forget_password)

        Button(login_frame, text="Login", font=("goudy old style", 20, "bold"), bg="#00FFFF", fg="#000000", command=self.login).place(x=300, y=400, width=200, height=55)

        # ================= Analog Clock ==================
        self.canvas = Canvas(self.root, width=400, height=500, bg='black', highlightthickness=0)
        self.canvas.place(x=300, y=100)
        self.center_x = 200
        self.center_y = 250
        self.clock_radius = 180
        self.update_clock()

    def update_clock(self):
        self.canvas.delete("all")
        self.canvas.create_text(200, 40, text="Analog Clock", font=("Arial", 30, "bold"), fill="white")
        self.canvas.create_oval(self.center_x - self.clock_radius, self.center_y - self.clock_radius,
                                 self.center_x + self.clock_radius, self.center_y + self.clock_radius,
                                 outline="#00FFFF", width=8)

        for i in range(60):
            angle = math.radians(i * 6 - 90)
            inner = self.clock_radius * 0.92
            outer = self.clock_radius * 0.98
            x1 = self.center_x + inner * math.cos(angle)
            y1 = self.center_y + inner * math.sin(angle)
            x2 = self.center_x + outer * math.cos(angle)
            y2 = self.center_y + outer * math.sin(angle)
            width = 2 if i % 5 == 0 else 1
            self.canvas.create_line(x1, y1, x2, y2, fill="white", width=width)

        for hour in range(1, 13):
            angle = math.radians((hour - 3) * 30)
            x = self.center_x + self.clock_radius * 0.75 * math.cos(angle)
            y = self.center_y + self.clock_radius * 0.75 * math.sin(angle)
            self.canvas.create_text(x, y, text=str(hour), fill="white", font=("Arial", 22, "bold"))

        t = time.localtime()
        self.draw_hand((t.tm_hour % 12 + t.tm_min / 60) * 30, self.clock_radius * 0.5, 10, "white")
        self.draw_hand(t.tm_min * 6, self.clock_radius * 0.7, 8, "white")
        self.draw_hand(t.tm_sec * 6, self.clock_radius * 0.85, 4, "red")

        self.canvas.create_oval(self.center_x-10, self.center_y-10, self.center_x+10, self.center_y+10, fill="cyan")
        self.root.after(1000, self.update_clock)

    def draw_hand(self, angle_deg, length, width, color):
        angle_rad = math.radians(angle_deg - 90)
        x = self.center_x + length * math.cos(angle_rad)
        y = self.center_y + length * math.sin(angle_rad)
        self.canvas.create_line(self.center_x, self.center_y, x, y, width=width, fill=color, capstyle=ROUND)

    def register_window(self, event=None):
        self.root.destroy()
        os.system("python register.py")
#=======================================================Login fnc=========================================================================
    def login(self):
        if self.var_email.get() == "" or self.var_password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        try:
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM employee WHERE email=? AND password=?", (self.var_email.get(), self.var_password.get()))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
            else:
                messagebox.showinfo("Success", f"Welcome {self.var_email.get()}", parent=self.root)
                self.root.destroy()

                import dashboard
                root = Tk()
                obj = dashboard.Main(root)
                root.mainloop()

            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)


#=======================================================forget password fnc=========================================================================

    def forget_password(self, event=None):
        if self.var_email.get() == "":
            messagebox.showerror("Error", "Please enter the email first", parent=self.root)
            return
        try:
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM employee WHERE email=?", (self.var_email.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Email not registered", parent=self.root)
            else:
                self.reset_password_window()
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

#=======================================================forget password window fnc=========================================================================
    def reset_password_window(self):
        self.root2 = Toplevel(self.root)
        self.root2.title("Reset Password")
        self.root2.geometry("600x460+780+300")
        self.root2.config(bg="white")
        self.root2.grab_set()

        Label(self.root2, text="Forget Password", font=("Times new roman", 20, "bold"), bg="white", fg="red").place(x=0, y=10, relwidth=1)
        Label(self.root2, text="Security Question", font=("Times New Roman", 15, "bold"), bg="white").place(x=170, y=80)
        self.combo_quest = ttk.Combobox(self.root2, font=("Times New Roman", 15), state='readonly', justify=CENTER,
                                        values=("Select", "What was your childhood nickname?",
                                                "What was the name of your first pet?", 
                                                "In which city were you born?", 
                                                "What is your favorite book?", 
                                                "What is your favorite game?"))
        self.combo_quest.place(x=170, y=110, width=250)
        self.combo_quest.current(0)

        Label(self.root2, text="Answer", font=("Times New Roman", 15, "bold"), bg="white").place(x=170, y=160)
        self.txt_answer = Entry(self.root2, font=("Times New Roman", 15), bg="lightgray")
        self.txt_answer.place(x=170, y=190, width=250)

        Label(self.root2, text="New Password", font=("Times New Roman", 15, "bold"), bg="white").place(x=170, y=240)
        self.txt_newpass = Entry(self.root2, font=("Times New Roman", 15), bg="lightgray", show="*")
        self.txt_newpass.place(x=170, y=270, width=250)

        Button(self.root2, text="Reset", command=self.reset_password, font=("goudy old style", 15, "bold"), bg="green", fg="white").place(x=250, y=330, width=100)


#=======================================================Reset password fnc=========================================================================
    def reset_password(self):
        if self.combo_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_newpass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
            return
        try:
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM employee WHERE email=? AND question=? AND answer=?", (
                self.var_email.get(), self.combo_quest.get(), self.txt_answer.get()
            ))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Answer or Question", parent=self.root2)
            else:
                cur.execute("UPDATE employee SET password=? WHERE email=?", (
                    self.txt_newpass.get(), self.var_email.get()
                ))
                con.commit()
                messagebox.showinfo("Success", "Password reset successful", parent=self.root2)
                self.root2.destroy()
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root2)

if __name__ == "__main__":
    root = Tk()
    obj = Login_window(root)
    root.mainloop()
