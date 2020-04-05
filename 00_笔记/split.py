# str.split(str="", num=string.count(str))   返回分割后的字符串列表
# str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# num -- 分割次数。默认为 -1, 即分隔所有。
# str.splitlines()    返回一个列表，按照行进行分割
# 将 字符串“1,2,3” 转换为 列表["1","2","3"]
r = "1,2,3"
new_r = r.split(",")
print(new_r)


s = '''weewrw
      dsaafa
      dsdg
      gsgsgs'''
new_s = s.splitlines
print(new_s)


