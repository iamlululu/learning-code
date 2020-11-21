class Cel:
    def __init__(self,value = 26.0):
        self.value = value
    def __get__(self, instance, owner):
        return  self.value
    def __set__(self, instance, value):
        self.value = value


class Fah():
    def __get__(self, instance, owner):
        return (float(instance.cel) ) * 1.8 + 32
    def __set__(self, instance, value):
        instance.cel = (float(value - 32)) / 1.8


class Temprature:
    cel = Cel()
    fah = Fah()
