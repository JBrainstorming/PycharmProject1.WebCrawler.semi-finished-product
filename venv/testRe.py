#正则表达式： 字符串模式（判断字符串是否符合一定的标准）

import re
#创建模式对象

pat = re.compile("AA")
m = pat.search("CBA")
print(m)

m = pat.search("ABCAA")
print(m)

m = pat.search("AABCAADDCCAAA")
print(m)

m = re.search("asd","Aasd")
#前面的字符串是规则（模板），后面的字符串是被校验的
print(m)

print(re.findall("a","ASDaDFGAa"))
#前面的字符串是规则（正则表达式），后面的字符串是被校验的

print(re.findall("[A-Z]","ASDaDFGAa"))
print(re.findall("[A-Z]+","ASDaDFGAa"))

#sub : 分隔，替换
print(re.sub("a","A","abcdcas"))#把"abcdcas"所有的a替换成A

#总结：
#只要是对长字符串进行处理，一般都使用正则表达式进行处理，最好在字符串前加上r，这样就不用担心转义字符的问题

#如：
a = r"\aabd-\'"
print(a)
