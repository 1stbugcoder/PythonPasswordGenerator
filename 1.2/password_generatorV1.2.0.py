#!!!!!!!!!!WARNING!!!!!!!!!!
#本项目遵循Apache License 2.0开源协议
#Version:1.2.0
import random


rangeA = "1234567890"
rangeB = "qwertyuiopasdfghjklzxcvbnm"
rangeC = "QWERTYUIOPASDFGHJKLZXCVBNM"
rangeD = ",.?!@#$%^&*"
password_range = []    #密码范围

def append():    #将密码范围添加到列表中
    for x in range:
        password_range.append(x)
        
def customize():    #自定义密码范围
    global rangeE    #因为函数内的变量不允许在函数外调用，因此必须声明全局变量
    rangeE = ""    #下面要判断变量是否为空，因此先创建变量
    while rangeE == "":
        rangeE = input("请输入密码范围，请勿重复输入：")
        if rangeE == "":
            print("输入不能为空")
        
def error_warning():    #错误输入警告
    print("无效的输入，请重启此程序以重新输入")
    exit()
    

introduction = """
密码类型说明
a   0~9
b   小写字母
c   大写字母
d   特殊字符,.?!@#$%^&*
e   自定义密码范围
若需要自定义密码范围，请只输入e
若不需要自定义密码范围，输入中有e将被忽略
例如，输入bc，bbcc，bce效果是一样的
"""
print(introduction)
type = input("请输入密码类型：")
range = ""    #先创建一个空字符串，否则如果直接输入d，就因为没有变量range而报错

if type != "":
    if "a" in type:    #判断密码类型
        range = rangeA
    if "b" in type:
        range = range + rangeB
    if "c" in type:
        range = range + rangeC
    if "d" in type:
        range = range + rangeD
    if type == "e":
        customize()
        range = rangeE
    append()
    if password_range == []:
        error_warning()
        
else:
    error_warning()
    
try:
    bit = int(input("请输入要生成的密码位数："))
except:
    error_warning()
    
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

        