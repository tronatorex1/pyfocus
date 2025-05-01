import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk
import time

class TimerApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Focus!")
        self.root.geometry("500x500")

        # background image
        self.bg_image = Image.open(r"D:\TMP\___Focus\Untitled-1.jpg")  # Replace with your JPEG image path
        self.bg_image = self.bg_image.resize((500,500))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # label for background
        self.bg_label = tk.Label(root,image=self.bg_photo)
        self.bg_label.place(relwidth=1,relheight=1)

        # Initialize timer variables
        self.start_time = None
        self.running = False
        self.time_elapsed = 0

        # Label to display time
        self.time_label = tk.Label(root,font=("Consolas",20),bg="black",fg="white")
        self.time_label.place(x=0,y=500-40)

        # Start button
        self.start_button = tk.Button(root,text="Start/Next",font=("Candara",14),command=self.start_timer)
        self.start_button.place(x=150+150,y=500-40)

        # Stop button
        self.stop_button = tk.Button(root,text="       Stop       ",font=("Candara",14),command=self.stop_timer)
        self.stop_button.place(x=250+150,y=500-40)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.start_time = self.start_over_time()
            self.start_time = time.time() - self.time_elapsed  # Continue from the last time
            self.update_time()

    def stop_timer(self):
        if self.running:
            self.running = False
            self.time_elapsed = time.time() - self.start_time
            self.update_time()
            with open(r"C:\Users\w10\Desktop\Apps\focus_log.csv","a+") as f:
                f.write(f"{time.asctime()},Seconds focusing=,{self.time_elapsed} {chr(10)}")

    def update_time(self):
        if self.running:
            self.time_elapsed = time.time() - self.start_time
            self.time_label.config(text=f"Time: {int(self.time_elapsed)}")
            self.root.after(1000,self.update_time)  # Update every second

    def start_over_time(self):
        if self.running:
            self.time_elapsed = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
