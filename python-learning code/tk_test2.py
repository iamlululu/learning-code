from tkinter import *

sel = [('杨玉环',1),('西施',2),('王昭君',3),('貂婵',4)]


root = Tk()


group = LabelFrame(root,text = '最漂亮的是？',padx = 5,pady = 5)
group.pack(padx = 10,pady = 10)


v = IntVar()


for name,num in sel:

    b = Radiobutton(group,text = name,variable = v,value = num)
    b.pack(anchor = CENTER)


mainloop()