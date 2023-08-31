from tkinter import *

master = Tk()
e = Entry(master)
e.pack()

e.focus_set()




def printSomething():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(master, text = str(e.get()))
    #this creates a new label to the GUI
    label.pack() 


button = Button(master, text="Print sum", command=printSomething) 
button.pack()

mainloop()

print(terms)

quit()

