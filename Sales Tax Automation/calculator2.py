import tkinter as tk
import itertools

numbers = []
target = 100
result = ""



master = tk.Tk()

tk.Label(master, text="Target Value")
tk.Label(master, text="Numbers separated by commas (no spaces)")

e = tk.Entry(master)
e1 = tk.Entry(master)

e.pack()
e1.pack()
e.focus_set()


def printSomething():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()

    num_list = e.get()
    num_list = num_list.split(",")
    for term in num_list:
        numbers.append(float(term))


    result = [seq for i in range(len(numbers), 0, -1)
        for seq in itertools.combinations(numbers, i)
        if sum(seq) == target]
    
    label = Label(master, text = str(result)).pack()
    #this creates a new label to the GUI
    label.pack() 
    


button = tk.Button(master, text="Print sum", command=printSomething) 
button.pack()

tk.mainloop()

print(terms)

quit()

