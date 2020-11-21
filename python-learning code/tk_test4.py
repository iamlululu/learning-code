from tkinter import *

root = Tk()

theLB = Listbox(root)
theLB.pack()

for item in range(11):
    theLB.insert(END,item)


BT = Button(root,text = '删除',command = lambda x = theLB:x.delete(ACTIVE))
BT.pack()


mainloop()