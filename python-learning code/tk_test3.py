from tkinter import *

root = Tk()



lable1 = Label(root,text = '账号：').grid(row = 0,column = 0)
lable2 = Label(root,text = '密码：').grid(row = 1,column = 0)

v1 = StringVar()
v2 = StringVar()

en1 = Entry(root,textvariable = v1)
en1.grid(row = 0,column = 1,padx = 10,pady = 5)
en2 = Entry(root,textvariable = v2,show = '*')
en2.grid(row = 1,column = 1,padx = 10,pady = 5)

def c1():
    print('账号：%s' % en1.get())
    print('密码：%s' % en2.get())

def c2():
    exit()

b1 = Button(root,text = '获取信息',width = 10,command = c1).grid(row = 3,column = 0,sticky = W,padx = 10,pady =5)
b2 = Button(root,text = '退出',width = 10,command = c2).grid(row = 3,column = 1,sticky = E,padx = 10,pady =5)


mainloop()

