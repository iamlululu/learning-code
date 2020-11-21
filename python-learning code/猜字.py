import random
secret = random.randint(1,10)
print("-----------------------------")
tempt = input("猜一个数字")
guss = int(tempt)
while guss != secret:
    if guss > secret:
        print("猜大了")
    else:
        print("猜小了")
    tempt = input("再猜一遍")
    guss = int(tempt)
    if guss == secret:
        print("猜对了")
print("再见")
