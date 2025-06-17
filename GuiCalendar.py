import tkinter as tk
from tkcalendar import Calendar
import calendar

window = tk.Tk()
window.title("Calendar App")

myCal = Calendar(window, selectmode="day", date_pattern="dd/mm/yyyy")
myCal.pack(pady=20)

def show_date():
    date = myCal.get_date()
    date_label.config(text="Selected Date: " + date)


show_button = tk.Button(window, text="Show Date", command=show_date)
show_button.pack(pady=10)

date_label = tk.Label(window, text="")
date_label.pack(pady=10)
window.mainloop()
