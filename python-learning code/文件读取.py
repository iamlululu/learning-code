def save_file(boy,girl,count):       #保存文件函数
    file_name_boy = 'boy_' + str(count) + '.txt'  # 文件命名
    file_name_girl = 'girl_' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'w')  # 打开创建文件
    girl_file = open(file_name_girl, 'w')

    boy_file.writelines(boy)  # 将序列数据写入文件
    girl_file.writelines(girl)

    boy_file.close()            #关闭文件
    girl_file.close()

def split_file(file_name):
    f = open(file_name,errors= 'ignore')
    boy = []
    girl = []
    count = 1
    for each_line in f:
        if each_line[:3] != '===':
            (role,line_spoken) = each_line.split(':',1)
            if role == '陆':
                boy.append(line_spoken)
            if role == '伟':
                girl.append(line_spoken)
        else:
            save_file(boy,girl,count)    #调用函数
            boy = []
            girl = []
            count += 1

    f.close()

split_file('Z:/python_pycharm/programs/talk.txt')



