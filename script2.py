from  tkinter import *

#create window
window=Tk()

def convert_kg():
	kg_grams=float(e1_value.get())*1000
	t1.insert(END, kg_grams)

	kg_pounds= float(e1_value.get())*2.20462
	t2.insert(END, kg_pounds)

	kg_ounces= float(e1_value.get())*35.274
	t3.insert(END, kg_ounces)

#add button, entry, label, and text widgets to window

var = StringVar()
lb= Label(window, textvariable=var, height=1, width=20)
var.set("kg")
lb.grid(row=0, column=0)


#Create string entry object to be used by entry widget
e1_value=StringVar()

e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)


b1=Button(window, text="Convert", command=convert_kg)
b1.grid(row=0,column=2)

t1=Text(window, height=1, width=20)
t1.grid(row=1, column=0)
t2=Text(window, height=1, width=20)
t2.grid(row=1, column=1)
t3=Text(window, height=1, width=20)
t3.grid(row=1, column=2)


window.mainloop()
