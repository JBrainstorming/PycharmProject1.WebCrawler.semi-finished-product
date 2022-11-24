#此文件为bs4的测试文件，相当于草稿，以便后面回过来查阅用

from bs4 import BeautifulSoup

file = open("douban.html", "rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")

'''
print(bs.a)
#print(bs.head)
print(bs.a.attr)  #不返回属性
print(bs.a.attrs) #返回属性簇

print(bs.a.string)
print(type(bs.a.string))

#输出：豆瓣
#     <class 'bs4.element.NavigableString'>
#可见
'''

"""
遍历文档树
①.contents:获取Tag的所有子节点
print(bs.head.contents)
#tag的.content 属性可以将tag的子节点以列表的方式输出，返回一个list
print(bs.head.contents[1])
#用列表索引来获取它的第一个元素
②.children 获取Tag的所有节点，返回一个生成器
③.descendants 获取Tag的所有子孙节点
④.strings 如果Tag包含多个字符串，即在子孙节点中有内容，可以用此获取，而后进行遍历
⑤.stripped_strings 与strings用法一致，但可以删去多余的空白内容
⑥.parent 获取Tag的父节点
如：
print(bs.head.contents)  #以一个列表形式返回head中的所有内容
"""

"""
搜索文档
"""
t_list = bs.find_all("a")  #直接查找所有的a
print(t_list)  #输出所有的超链接

'''
import re
#法2： 正则表达式搜索：使用search()方法来匹配内容
t_list = bs.find_all(re.compile("a"))
print(t_list)
'''

"""
法3 自定义搜索方法（推荐使用）

#方法： 传入一个函数（方法），根据函数的要求来搜索
def name_is_exists(tag):
    return tag.has_attr("name")

t_list = bs.find_all(name_is_exists("tag"))
#可以满足个人需求的定义，可考虑采用，注意灵活使用return

    
"""
# other: kwargs   参数

#1. t_list = bs.find_all(id="div")  #找到所有块级元素

#2. t_list = bs.find_all(class_ = "market-spu-pic")

#3. t_list = bs.find_all(class_ = True)  #返回所有具有class属性的元素

#4. text = ["电影","豆瓣"]
#   t_list = bs.find_all(text = re.compile("\d")) #找到所有含数字的文本

#5. t_list = bs.find_all("a",limit=3) #最多只要3个<a>标签内容

#6. 选择器   （利用css自身具有的特点，层层索引、实现精准定位）
'''
for item in t_list:
    print(item)
'''
print(bs.select('title'))   #通过标签来查找
print(bs.select(".market-spu-title"))    #通过类名查找
print(bs.select("#u1"))     #通过id来查找
print(bs.select("a[class='market-spu-title']"))
print(bs.select("head > title"))         #通过属性来查找
print(bs.select(".mnav ~ .brother")[0].get_text())     #通过子标签来查找
