from tkinter import *
import webbrowser

root = Tk()

text = Text(root,width = 30,height = 5)
text.pack()

text.insert(INSERT,'It is My Webside')

text.tag_add('link','1.6','1.16')
text.tag_config('link',foreground = 'blue',underline = TRUE)


def func1(event):
    text.config(cursor = 'arrow')

def func2(event):
    text.config(cursor='xterm')

def func3(event):
    webbrowser.open('http://www.baidu.com')



text.tag_bind('link','<Enter>',func1)
text.tag_bind('link','<Leave>',func2)
text.tag_bind('link','<Button-1>',func3)

mainloop()





