
#str.split(str="", num=string.count(str))
# str:分割字符   默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
# num: 分割次数  默认分割所有
string = "\t锄禾日当午汗滴禾下土\n谁知盘中餐\n粒粒皆辛苦"

print(string)
print(string.split())


# str.join(seq):用于将序列中(seq)的元素以指定的字符(str)连接生成一个新的字符串。
print(" ".join(string))

l = ["http:","//"]
print("".join(l))
