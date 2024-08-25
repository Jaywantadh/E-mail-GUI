#################################################################################################################################################################################################
# ###############################################################################################################################################################################################
# Code Created and Edited by: Jaywant Sandeep Adhau                                               
# 
# Functions:
# -EmailSchedulerApp Class: Contains the main functionality and GUI components.
# -attach_file(): Opens a file dialog to select a file for attachment.
# -send_email(): Sends the email using SMTP with the provided details.
# -schedule_email(): Handles the scheduling of the email.
# -get_scheduled_time(): Retrieves the scheduled time from the calendar and time entry.
# -start_sending(): Starts the email sending process based on the interval or scheduled time.
# -cancel_sending(): Cancels any ongoing scheduled email sending.
# -switch_theme(): Switches between light and dark themes.
# -configure_theme(): Applies the selected theme to the application.
# 
# Dependencies:
# -tkinter: For creating the GUI.
# -tkcalendar: For the calendar widget.
# -schedule: For scheduling tasks.
# -smtplib, email: For sending emails.
#
#################################################################################################################################################################################################
#################################################################################################################################################################################################

import tkinter as tk
from tkinter import filedialog, messagebox
from tkcalendar import Calendar
from datetime import datetime
import schedule
import time
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import os

class EmailSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Scheduler")
        self.root.geometry("500x750")
        self.is_dark_mode = False

        self.light_theme = {"bg": "#f0f0f0", "fg": "black", "button_bg": "#007BFF", "button_fg": "white"}
        self.dark_theme = {"bg": "#2c2c2c", "fg": "white", "button_bg": "#1c1c1c", "button_fg": "#007BFF"}
        self.theme = self.light_theme

        self.configure_theme()

        self.filename = ""
        
        tk.Label(root, text="Sender's Email:", bg=self.theme["bg"], fg=self.theme["fg"]).place(x=20, y=20)
        self.sender_email = tk.Entry(root, width=40)
        self.sender_email.place(x=150, y=20)

        tk.Label(root, text="App Password:", bg=self.theme["bg"], fg=self.theme["fg"]).place(x=20, y=60)
        self.app_password = tk.Entry(root, width=40, show='*')
        self.app_password.place(x=150, y=60)


        tk.Label(root, text="Recipient's Email(s):", bg=self.theme["bg"], fg=self.theme["fg"]).place(x=20, y=100)
        self.recipient_emails = tk.Entry(root, width=40)
        self.recipient_emails.place(x=150, y=100)

        tk.Label(root, text="Body Message:", bg=self.theme["bg"], fg=self.theme["fg"]).place(x=20, y=140)
        self.body_message = tk.Text(root, height=10, width=40, bg=self.theme["bg"], fg=self.theme["fg"])
        self.body_message.place(x=150, y=140)

        tk.Button(root, text="Attach File", command=self.attach_file, bg=self.theme["button_bg"], fg=self.theme["button_fg"]).place(x=20, y=320)
        self.file_label = tk.Label(root, text="No file selected", bg=self.theme["bg"], fg=self.theme["fg"])
        self.file_label.place(x=150, y=320)

        # Interval (in seconds and can be changed to minutes or hours as specified)
        tk.Label(root, text="Interval (seconds):", bg=self.theme["bg"], fg=self.theme["fg"]).place(x=20, y=360)
        self.interval = tk.Entry(root, width=40)
        self.interval.place(x=150, y=360)

        
        tk.Label(root, text="Select Date:", bg=self.theme["bg"], fg=self.theme["fg"]).place(x=20, y=400)
        self.calendar = Calendar(root, selectmode="day", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, background=self.theme["bg"], foreground=self.theme["fg"])
        self.calendar.place(x=150, y=400)

        
        tk.Label(root, text="Select Time (HH:MM:SS):", bg=self.theme["bg"], fg=self.theme["fg"]).place(x=20, y=580)
        self.time_entry = tk.Entry(root, width=40)
        self.time_entry.place(x=150, y=580)
        self.time_entry.insert(0, "00:00:00")

        
        tk.Button(root, text="Switch Theme", command=self.switch_theme, bg=self.theme["button_bg"], fg=self.theme["button_fg"]).place(x=150, y=660)

        
        tk.Button(root, text="Start", command=self.start_sending, bg="#28a745", fg="white").place(x=150, y=700)
        tk.Button(root, text="Cancel", command=self.cancel_sending, bg="#dc3545", fg="white").place(x=220, y=700)
        tk.Button(root, text="Exit", command=root.quit, bg="#6c757d", fg="white").place(x=290, y=700)

    def attach_file(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file")
        if self.filename:
            self.file_label.config(text=os.path.basename(self.filename))

    def send_email(self):
        try:
            fromaddr = self.sender_email.get()
            toaddr = self.recipient_emails.get().split(',')

            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = ", ".join(toaddr)
            msg['Subject'] = f"Scheduled Email with Log File"

            body = self.body_message.get("1.0", tk.END)
            msg.attach(MIMEText(body, 'plain'))

            if self.filename:
                attachment = open(self.filename, 'rb')
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename={os.path.basename(self.filename)}")
                msg.attach(part)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, self.app_password.get())
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()

            messagebox.showinfo("Success", "Email sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {e}")

    def schedule_email(self):
        scheduled_time = self.get_scheduled_time()
        while datetime.now() < scheduled_time:
            time.sleep(1)
        self.send_email()

    def get_scheduled_time(self):
        date_str = self.calendar.get_date()
        time_str = self.time_entry.get()
        datetime_str = f"{date_str} {time_str}"
        return datetime.strptime(datetime_str, "%m/%d/%y %H:%M:%S")

    def start_sending(self):
        if self.interval.get():
            interval = int(self.interval.get())
            schedule.every(interval).seconds.do(self.send_email)
        else:
            scheduled_time = self.get_scheduled_time()
            schedule.every().day.at(scheduled_time.strftime("%H:%M:%S")).do(self.schedule_email)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def cancel_sending(self):
        schedule.clear()
        messagebox.showinfo("Cancelled", "Scheduled email sending has been cancelled.")

    def switch_theme(self):
        if self.is_dark_mode:
            self.theme = self.light_theme
            self.is_dark_mode = False
        else:
            self.theme = self.dark_theme
            self.is_dark_mode = True
        self.configure_theme()

    def configure_theme(self):
        self.root.configure(bg=self.theme["bg"])
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label) or isinstance(widget, tk.Entry) or isinstance(widget, tk.Text) or isinstance(widget, tk.Button):
                widget.configure(bg=self.theme["bg"], fg=self.theme["fg"])
            if isinstance(widget, tk.Button):
                widget.configure(bg=self.theme["button_bg"], fg=self.theme["button_fg"])

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailSchedulerApp(root)
    root.mainloop()
