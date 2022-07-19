# Create GUI Calender
from tkinter import *
from PIL import Image,ImageTk
import calendar
root=Tk()
root.title("Calender")
root.geometry("780x600+100+100")
root.configure(background="gray")
def showCalender():
    gui = Tk()
    gui.configure(background="gray")
    gui.geometry("550x600+320+120")
    gui.title("Calender For The Year")

    year = int(chicked.get())
    calenderV=calendar.calendar(year)
    calYear= Label(gui, text=calenderV,font=("Consolas",10,"bold"))
    calYear.grid(row=5,column=1,padx=20)
    gui.mainloop()


labelCal= LabelFrame(root, text="Calender",font=("Helvetica", 30,"normal","bold"),background="gray",padx=40, pady=60)
labelCal.grid(row=1,column=0)

labelEn=Label(labelCal,text="Select Year:",font=("Courier",12),background="dark gray",borderwidth=2)
labelEn.grid(row=0,column=0)

options=[
    2022,
    2021,
    2020,
    2019,2018,2017,2016,
    2015,2014,2013,2012,2011,2010
    ,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000,
    1999,1998
]
chicked=IntVar()
chicked.set(options[0])
year=OptionMenu(labelCal,chicked,*options)
year.grid(row=1,column=0,pady=7)
showCal= Button(labelCal,text="Show Calender",bg="blue",command=showCalender)
showCal.grid(row=4,column=0,pady=7)
exitButton= Button(labelCal, text="Exit",command=root.quit,bg="blue")
exitButton.grid(row=6,column=0,pady=7,ipadx=10)
root.mainloop()