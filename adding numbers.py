from tkinter import*

window = Tk()
window.geometry("550x350")

window.config(bg='pink')

window.title('Adding two numbers')


label_1 = Label(window, text = "Enter 1st Number")
label_2 = Label(window, text = "Enter 2nd Number")
label_3 = Label(window, text = "Answer")
label_4 = Label(window)

first_number = Entry (window)
second_number = Entry (window)
total = Entry (window)

def button_clear ():

    total.delete (0, END)
    first_number.delete(0, END)
    second_number.delete(0, END)

def button_add ():
    dig_1 = first_number.get();
    dig_2 = second_number.get();
    first_addition = int(dig_1)
    second_addition = int(dig_2)
    sum = first_addition + second_addition

    total.insert(0, sum)

def button_exit ():
    import sys
    sys.exit()

button_add = Button (window, borderwidth=5, font=("Consolas 15 bold"),text="Add", bg="white", fg="black", width=10, command=button_add)
button_clear = Button (window, text = "Clear", borderwidth=5, font=("Consolas 15 bold"), bg="white", fg="black", width=10, command=button_clear)
button_exit = Button (window, text = "Exit", borderwidth=5, font=("Consolas 15 bold"), bg="white", fg="black", width=10, command=button_exit)

label_1.grid(row=0, column=0, padx=10, pady=10)
label_2.grid(row=1, column=0, padx=10, pady=10)
label_3.grid(row=2, column=2, padx=10, pady=10)
first_number.grid(row=0, column=1, padx=10, pady=10)
second_number.grid(row=1, column=1, padx=10, pady=10)
total.grid(row=2, column=1, padx=10, pady=10)
button_add.place(x=20, y=150)
button_clear.place(x=200, y=150)
button_exit.place(x=380, y=150)
window.mainloop()