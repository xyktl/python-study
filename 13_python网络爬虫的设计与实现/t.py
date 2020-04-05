import re
s1 = ["?75.22","d55.43"]
s2 = ["1111条频率","1434条频率"]
print(s1)
s1 = map(lambda x : re.sub(r'\?','',x),s1)
print(list(s1))
s2 = map(lambda x : re.sub(r'条频率','',x),s2)    #map对象相当于生成器
for i in s2:
    print(i)



list = ['tu=d37b3e79010b526f853a69732e5d9600;Path=/uipp', 'cmddl=1f37cdb7dbb39d487ed7ae456241d71c;Path=/kl', 'popod_=e910be433b4e6;Path=/ffg']
list1 = map(lambda x : re.sub(";Path=[^\']+", '', x), list)
print(list1)