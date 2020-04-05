import re
#将正则表达式匹配的内容 替换  用sub()实现

def fun(matched):
    ''''''
    value = "《基础" + (matched.group("lang")) + "课程》"
    return value
str = "python很好,java也很好！"
str1 = re.sub(r"(?P<lang>\w+)", fun,str, flags=re.A)
print(str1)


'''上面程序使用 sub() 函数执行替换时，指定使用 fun() 函数作为替换内容，
而 fun() 函数则负责在 pattern 匹配的字符串之前添加“《基础”，在 pattern 匹配的字符串之后添加“教程》”。
运行上面程序，可以看到如下输出结果：
《基础python课程》很好,《基础java课程》也很好！

由于此时还未深入介绍正则表达式的语法，因此前面所使用的正则表达式都很简单，
但此处使用了一个稍微复杂的正则表达式： r'(? P<lang>\w+)'。

r'(?P<lang>\w+)' 正则表达式用圆括号表达式创建了一个组，并使用“?P”选项为该
组起名为 lang（所起的组名要放在尖括号内）。剩下的“\w+”才是正则表达式的内容，
其中“\w”代表任意字符；“+”用于限定前面的“\w”可出现一次到多次，因此“\w+”代表
一个或多个任意字符。又由于程序执行 sub() 函数时指定了 re.A 选项，这样“\w”就
只能代表 ASCII 字符，不能代表汉字。
'''

print(re.__all__)
import datetime

