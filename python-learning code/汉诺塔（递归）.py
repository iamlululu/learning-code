def hanoi(n,x,y,z):
    if n == 1:
        print(x,'-->',z)
    else: 
        hanoi(n-1,x,z,y)          #将n-1个盘子从x移动到y上
        print(x,'-->',z)          #将x上最后一个盘子移动到z上
        hanoi(n-1,y,x,z)          #将y上n-1个盘子移动到z上

number = int(input('请输入汉诺塔层数：'))
hanoi(number,'X','Y','Z')
