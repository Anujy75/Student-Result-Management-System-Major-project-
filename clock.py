from tkinter import *
import time
import math

class clockClass:
    def __init__(self, parent):   # NOTE: parent, not root
        self.parent = parent

        self.canvas = Canvas(self.parent, width=500, height=700, bg='black', highlightthickness=0)
        self.canvas.place(x=0, y=0)

        self.center_x = 250
        self.center_y = 400
        self.clock_radius = 220

        self.update_clock()

    def update_clock(self):
        self.canvas.delete("all")

        # Draw clock border
        self.canvas.create_oval(self.center_x - self.clock_radius, self.center_y - self.clock_radius,
                                 self.center_x + self.clock_radius, self.center_y + self.clock_radius,
                                 outline="#00FFFF", width=5)

        # Draw minute ticks
        for i in range(60):
            angle = math.radians(i * 6 - 90)
            inner = self.clock_radius * 0.92
            outer = self.clock_radius * 0.98
            x1 = self.center_x + inner * math.cos(angle)
            y1 = self.center_y + inner * math.sin(angle)
            x2 = self.center_x + outer * math.cos(angle)
            y2 = self.center_y + outer * math.sin(angle)
            width = 2 if i % 5 == 0 else 1
            color = "white"
            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=width)

        # Draw numbers
        for hour in range(1, 13):
            angle = math.radians((hour - 3) * 30)
            x = self.center_x + self.clock_radius * 0.75 * math.cos(angle)
            y = self.center_y + self.clock_radius * 0.75 * math.sin(angle)
            self.canvas.create_text(x, y, text=str(hour), fill="white", font=("Arial", 16, "bold"))

        # Draw hands
        t = time.localtime()
        self.draw_hand((t.tm_hour % 12 + t.tm_min / 60) * 30, self.clock_radius * 0.5, 6, "white")
        self.draw_hand(t.tm_min * 6, self.clock_radius * 0.7, 5, "white")
        self.draw_hand(t.tm_sec * 6, self.clock_radius * 0.85, 3, "red")

        # Draw center circle
        self.canvas.create_oval(self.center_x+10, self.center_y-7, self.center_x+7, self.center_y+7, fill="cyan")

        # Draw Analog Clock title inside clock
        self.canvas.create_text(self.center_x, self.center_y - 320, text="Analog Clock", fill="cyan", font=("Arial", 35, "bold"))

        self.canvas.after(1000, self.update_clock)

    def draw_hand(self, angle_deg, length, width, color):
        angle_rad = math.radians(angle_deg - 90)
        x = self.center_x + length * math.cos(angle_rad)
        y = self.center_y + length * math.sin(angle_rad)
        self.canvas.create_line(self.center_x, self.center_y, x, y, width=width, fill=color, capstyle=ROUND)


# Test the code separately:
if __name__ == "__main__":
    root = Tk()
    root.geometry("500x600+300+150")
    root.config(bg="white")

    clock_frame = Frame(root, bg="white")
    clock_frame.place(x=0, y=0, width=500, height=600)

    clock = clockClass(clock_frame)

    root.mainloop()
