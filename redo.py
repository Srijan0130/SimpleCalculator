from tkinter import *

sc= Tk()
sc.title("Simple Calculator")

e = Entry(sc, width= 35, borderwidth=5)
e.grid(row=0, column= 0, columnspan= 3, padx= 10, pady= 10)

def button_click(num):

    current=e.get()
    e.delete(0, END)
    e.insert(0,num, str(current)+ str(num))

def button_clear():
    e.delete(0, END)

# Defining Buttons

button_1= Button(sc, text= "1", padx=40, pady=20, command= lambda: button_click(1))
button_2= Button(sc, text= "2", padx=40, pady=20, command= lambda: button_click(2))
button_3= Button(sc, text= "3", padx=40, pady=20, command= lambda: button_click(3))
button_4= Button(sc, text= "4", padx=40, pady=20, command= lambda: button_click(4))
button_5= Button(sc, text= "5", padx=40, pady=20, command= lambda: button_click(5))
button_6= Button(sc, text= "6", padx=40, pady=20, command= lambda: button_click(6))
button_7= Button(sc, text= "7", padx=40, pady=20, command= lambda: button_click(7))
button_8= Button(sc, text= "8", padx=40, pady=20, command= lambda: button_click(8))
button_9= Button(sc, text= "9", padx=40, pady=20, command= lambda: button_click(9))
button_0= Button(sc, text= "0", padx=40, pady=20, command= lambda: button_click(0))
button_add= Button(sc, text= "+", padx=40, pady=20, command= button_click)
button_equal= Button(sc, text= "=", padx=90, pady=20, command= button_click)
button_clear= Button(sc, text= "AC", padx=80, pady=20, command= button_click)

# putting the buttons on the screen


button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan= 2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

mainloop()
