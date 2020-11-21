import time as t

class Mytimer():
    
    def __init__(self):
        self.unit = ['年','月','天','时','分','秒']
        self.prompt = '计时未开始...'
        self.begain = 0
        self.end = 0
        self.lasted = []
        
    def __str__(self):
        return self.prompt
    __rper__ = __str__
    
    #两个计时器对象相加的时间
    def __add__(self,other):
        prompt = '总共的时间为'
        result = []
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                prompt += (str(result[index])+self.unit[index])
        return prompt
            


    #计时开始
    def start(self):
        self.begain = t.localtime()
        self.prompt = '请先调用stop()停止计时...'
        print('计时开始...')


    #计时结束
    def stop(self):
        if not self.begain:
            print('请先开始计时...')
        else:
            self.end = t.localtime()
            self._calc()
            print('计时结束...')


    #内部计算时间差
    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            self.lasted.append(self.end[index] - self.begain[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index])+self.unit[index])
        print(self.prompt)
        #为下一轮进行初始化
        self.begain = 0
        self.end = 0
        
       
        
        
        
