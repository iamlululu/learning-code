import  random as r

class Fish():
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        self.x -= 1
        self.y -= 1
        print('我的位置是：',self.x,self.y)

class Afish(Fish):
    pass
class Bfish(Fish):
    pass
class Cfish(Fish):
    def __init__(self):
        super().__init__()
    def eat(self):
        r.randint(0,1)
        if self.hungry:
            print('我要吃饭！！！！')
            self.hungry = False
        else:
            print('我吃饱了，哈哈哈哈哈')