from tkinter import *
import hashlib

root = Tk()


text = Text(root,width = 30,height = 5)
text.pack()

text.insert(INSERT,'I love FishC.com!')
text.tag_add('link','1.7','1.17')
text.tag_config('link',foreground = 'blue',underline = TRUE)

content = text.get('1.0',END)
hash_value = hashlib.md5(content.encode()).digest()



def hash(content):
    return hashlib.md5(content.encode()).digest()



def check():
    content = text.get('1.0',END)
    if hash_value != hash(content):
        print('erro')
    else:
        print('right')

button = Button(root,text = 'check',command = check)
button.pack()


mainloop()