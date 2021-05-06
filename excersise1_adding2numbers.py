from tkinter import *
window = Tk()
window.title("Adding two numbers")
window.geometry("500x500")


Lb1=Label(window, text="Please Enter First Number")
Lb1.pack(side=LEFT)
num1=Entry(window, bd=2)
num1.pack(side=RIGHT)
Lb1.place(x=2, y=0)
num1.place(x=10, y=50)


Lb2=Label(window, text="Please Enter Second Number")
Lb2.pack(side=LEFT)
num2=Entry(window, bd=2)
num2.pack(side=RIGHT)
Lb2.place(x=-2, y=0)
num2.place(x=60, y=50)

Lb3 = Label(window, text="Your Answer")


def add_numbers():
    pass

the_sum = float (entry_1())




window.mainloop()
