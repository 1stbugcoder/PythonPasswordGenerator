#!!!!!!!!!!WARNING!!!!!!!!!!
#本项目遵循Apache License 2.0开源协议
#Version:1.0.1
import random


range1 = "1234567890qwertyuiopasdfghjklzxcvbnm"
range2 = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
range3 = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm@#,.?!*%&$"
password_range =[]    #密码范围

def append():    #将密码范围添加到列表中
    for x in range:
        password_range.append(x)

introduction = """
密码类型说明
1   0~9和小写字母
2   0~9和大小写字母
3   0~9和大小写字母和特殊字符@#,.?!*%&$
"""
print(introduction)
try:    #如果输入的是字符串会报错，所以必须用try except
    type = int(input("请输入密码类型："))
except:
    print("无效的输入，请重启此程序以重新输入")
    exit()
    
if type == 1:    #判断密码类型
    range = range1
    append()
elif type == 2:
    range = range2
    append()
elif type == 3:
    range = range3
    append()   
else:
    print("无效的输入，请重启此程序以重新输入")
    exit()    #退出程序
    
try:    #与上面使用try except语句理由相同
    bit = int(input("请输入要生成的密码位数："))
except:
    print("无效的输入，请重启此程序以重新输入")
    exit()
i = 0
long = len(password_range)
output = ""    #创建空字符，方便和生成的随机字符相加

while True:
    index = random.randint(0,long - 1)#这里不太好讲，原因在最下面
    """
为什么要用long - 1，而不是long或long + 1？
这里我们假设用户的输入是1
即最终列表的长度为36
列表允许的索引范围为0~35
而长度却是36
random.randint(a,b)是可以取到b的
如果所以随机到36就会报错
IndexError: list index out of range
就是实际索引范围超过了允许的索引范围
(最后说一句，更让我无语的是
	以上的多行注释，居然那三个"也要缩进对齐，我呸)    
    """       
    everybit = password_range[index]    #随机选取数值
    output = output + everybit    #将随机选取的数值与空字符相加，经过循环得到最终输出
    i += 1
    if i == bit:    #确保循环次数等于密码位数时结束循环
        break

print(output)    #打印最终的结果

        