from tkinter import *

def callback():
    var.set('BullShit!')

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)


var = StringVar()
var.set('未满18周岁禁止观看...\n请满足要求后再观看')

textlable = Label(frame1,textvariable = var,justify = LEFT)
textlable.pack(side = LEFT)


photo = PhotoImage(file = 'ban.gif')
imglable = Label(frame1,image = photo)
imglable.pack(side = RIGHT)


theButton = Button(frame2,text = '我已满18周岁',command = callback)
theButton.pack()

frame1.pack(padx = 10,pady = 10)
frame2.pack(padx = 10,pady = 10)

mainloop()

