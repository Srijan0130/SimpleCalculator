from _ast import Lambda
from tkinter import *

cal = Tk()
cal.title("My Calculator")
cal.iconbitmap("C:/Users/gurun/Desktop/cal.ico")

e = Entry(cal, width=19, borderwidth=1, fg='white', bg='black', font=("arial", 22, 'bold'))
e.grid(row=0, column=0, columnspan=4, padx=10, ipady=10, pady=5)

bgg = 'grey'
fg1 = 'black'
fg2 = 'orange'
cal['bg'] = 'black'


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    try:
        first_number = e.get()
        global f_num
        global math
        math = "addition"
        f_num = int(first_number)
        e.delete(0, END)
    except:
        pass


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
       try:
           e.insert(0, f_num / int(second_number))
       except:
           e.insert(0, "error")


    if math == "square":
        e.insert(0, f_num ** int(second_number))


def button_sub():
    try:
        first_number = e.get()
        global f_num
        global math
        math = "subtraction"
        f_num = int(first_number)
        e.delete(0, END)
    except:
        e.delete(0, END)
        e.insert(0, "error")


def button_mul():
    try:
        first_number = e.get()
        global f_num
        global math
        math = "multiplication"
        f_num = int(first_number)
        e.delete(0, END)
    except:
        e.delete(0, END)
        e.insert(0, "error")


def button_div():
    try:
        first_number = e.get()
        global f_num
        global math
        math = "division"
        f_num = int(first_number)
        e.delete(0, END)
    except:
        e.delete(0, END)
        e.insert(0, "error")


def button_square():
    try:
        first_number = e.get()
        global f_num
        global math
        math = "square"
        f_num = int(first_number)
        e.delete(0, END)
    except:
        e.delete(0, END)
        e.insert(0, "error")


# define button

button_1 = Button(cal, text="1", fg=fg1, bg=bgg, padx=30, pady=20, font=("arial", 15, 'bold'),
                  command=lambda: button_click(1))
button_2 = Button(cal, text="2", fg=fg1, bg=bgg, padx=30, pady=20, font=("arial", 15, 'bold'),
                  command=lambda: button_click(2))
button_3 = Button(cal, text="3", fg=fg1, bg=bgg, padx=30, pady=20, font=("arial", 15, 'bold'),
                  command=lambda: button_click(3))
button_4 = Button(cal, text="4", fg=fg1, bg=bgg, padx=30, pady=20, font=("arial", 15, 'bold'),
                  command=lambda: button_click(4))
button_5 = Button(cal, text="5", fg=fg1, bg=bgg, padx=30, pady=20, font=("arial", 15, 'bold'),
                  command=lambda: button_click(5))
button_6 = Button(cal, text="6", fg=fg1, bg=bgg, padx=30, pady=20, font=("arial", 15, 'bold'),
                  command=lambda: button_click(6))
button_7 = Button(cal, text="7", fg=fg1, bg=bgg, padx=30, pady=20, font=("arial", 15, 'bold'),
                  command=lambda: button_click(7))
button_8 = Button(cal, text="8", fg=fg1, bg=bgg, padx=30, pady=20, font=("arial", 15, 'bold'),
                  command=lambda: button_click(8))
button_9 = Button(cal, text="9", fg=fg1, bg=bgg, padx=30, pady=20, font=("arial", 15, 'bold'),
                  command=lambda: button_click(9))
button_0 = Button(cal, text="0", fg=fg1, bg=bgg, padx=30, pady=20, font=("arial", 15, 'bold'),
                  command=lambda: button_click(0))
button_add = Button(cal, text="+", fg=fg1, bg=fg2, padx=30, pady=20, font=("arial", 15, 'bold'), command=button_add)
button_equal = Button(cal, text="=", fg=fg1, bg=fg2, font=("arial", 15, 'bold'), command=button_equal)
button_clear = Button(cal, text="AC", fg=fg1, bg=fg2, font=("arial", 15, 'bold'), command=button_clear)
button_sub = Button(cal, text="-", fg=fg1, bg=fg2, padx=33, pady=20, font=("arial", 15, 'bold'), command=button_sub)
button_mul = Button(cal, text="X", fg=fg1, bg=fg2, padx=30, pady=20, font=("arial", 15, 'bold'), command=button_mul)
button_div = Button(cal, text="/", fg=fg1, bg=fg2, padx=33, pady=20, font=("arial", 15, 'bold'), command=button_div)
button_square = Button(cal, text="**", fg=fg1, bg=fg2, padx=28, pady=20, font=("arial", 15, 'bold'),
                       command=button_square)

# put button on the screen

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)
button_clear.grid(row=1, column=0, ipadx=65, ipady=20, columnspan=2)
button_add.grid(row=4, column=3)
button_equal.grid(row=5, column=1, ipadx=118, ipady=20, columnspan=3)

button_sub.grid(row=3, column=3)
button_mul.grid(row=2, column=3)
button_div.grid(row=1, column=3)
button_square.grid(row=1, column=2)

mainloop()
