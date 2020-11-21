from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack(padx = 10,pady = 10)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()


def test(content):
    return content.isdigit()

testCMD = root.register(test)

e1 = Entry(frame,width = 10,textvariable =v1,validate = 'key',validatecommand = (testCMD,'%P')).grid(row = 0,column = 0)
lable1 = Label(frame,text = '+').grid(row = 0,column = 1)


e2 = Entry(frame,width = 10,textvariable =v2,validate = 'key',validatecommand = (testCMD,'%P')).grid(row = 0,column = 2)
lable2 = Label(frame,text = '=').grid(row = 0,column = 3)


e3 = Entry(frame,width = 10,textvariable =v3,state = 'readonly').grid(row = 0,column = 4)


def calc():
    v3.set(int(v1.get()) + int(v2.get()))
b1 = Button(frame,text = '计算',command = calc).grid(row = 1,column = 1)
b2 = Button(frame,text = '退出',command = root.quit).grid(row = 1,column = 4)

mainloop()