# -*- coding = utf-8 -*-
# @Time : 2022/11/15 17:51
# @author : 江心月
# @File : spider.py
# @Software : PyCharm-Community

import re  # 正则表达式，用于文字匹配
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite3数据库操作
from bs4 import BeautifulSoup  # 网页解析，用于获取数据
import urllib.request, urllib.error  # 获取网页数据


def main():
    print("开始爬取......\n")
    baseurl = "https://movie.douban.com/top250?start="
    # step1：爬取数据
    datalist = getdata(baseurl)
    path = r".\douban_Top250.xls"
    dbpath = "douban250.db"
    # step2：保存数据
    savedata(datalist, path)
    askURL(baseurl)
    # step3： SQLite3
    savedata2Database(datalist, dbpath)
    # step4:  Flask


# 影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">', re.S)  # 创建正则表达式对象，表示规则（字符串的模式）
# 影片图片
findImgSrc = re.compile(r'<img (.*?) src="(.*?)"', re.S)  # re.S: 忽略里面的换行情况
# 影片片名
findTitle = re.compile(r'<span class="title">(.*?)</span>', re.S)
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>', re.S)
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>', re.S)
# 电影概况
findInq = re.compile(r'<span class="inq">(.*)</span>', re.S)
# 电影背景介绍
findBg = re.compile(r'<p class="">(.*?)</p>', re.S)


def getdata(baseurl):  # 获取数据
    datalist = []
    for i in range(0, 10):  # 10次调用获取页面信息的函数
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码

        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，返回一个列表
            # print(item)  #测试：查看电影item全部信息
            data = []  # 保存一部电影的所有信息
            item = str(item)

            link = re.findall(findLink, item)[0]  # 使用re库来通过正则表达式查找指定的字符
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc[1])
            titles = re.findall(findTitle, item)  # 片名可能只有中文的，也可能只有外文的，
            if len(titles) == 2:  # 添加中文名|外文名
                CH_title = titles[0]
                data.append(CH_title)
                O_title = titles[1].replace("/", "")  # 去掉无关的符号
                O_title.replace("\xa0", "")
                data.append(O_title)
            else:
                data.append(titles[0])
                data.append(' ')  # 没有外文名时为空

            rating = re.findall(findRating, item)  # 添加评分
            data.append(rating)
            judgeNum = re.findall(findJudge, item)  # 添加评委人数
            data.append(judgeNum)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                data.append(inq)  # 添加概述
            else:
                data.append(" ")  # 若没有概述，留空

            bg = re.findall(findBg, item)[0]
            bg = re.sub('<br(\s+)?/>(\s+)?', " ", bg)  # 去掉<br/>
            bg = re.sub('/', " ", bg)  # 替换 /
            data.append(bg.strip())  # 去掉前后的空格
            datalist.append(data)
    print(datalist)
    return datalist


def askURL(url):
    # 模拟浏览器头部信息，向豆瓣服务器发送消息
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42 "
    }
    # 用户代理，表示告诉服务器浏览器类型（本质上是告诉能够接受什么水平的文件）
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)  # 打印报错源代码
        if hasattr(e, "reason"):
            print(e.reason)  # 打印报错原因
    return html


def savedata(datalist, path):  # 保存数据
    print("saving......")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    # 创建工作表
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])  # 数据
    book.save('Top250.xls')  # 保存


def init_db(dbpath):  # 初始化database并创建数据表
    # sql = '''
    #     create table movie250
    #     (
    #     id integer primary key autoincrement,
    #     info_link text,
    #     pic_link text,
    #     cname varchar,
    #     ename varchar,
    #     rated numeric,
    #     introduction text,
    #     info text
    #     )
    # '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    # cursor.execute(sql)
    conn.commit()
    conn.close()


def savedata2Database(datalist, dbpath):
    print("saving to database......")
    init_db("movie250.db")  # 初始化一个数据库douban_db
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for idx in range(len(data)):
            data[idx] = '"' + str(data[idx]) + '"'
        # sql = '''
        #     insert into moive250(info_link, pic_link, cname, ename, score, rated, introduction, info)
        #     values(%s)''' % ",".join(str(partial) for partial in data)
        # print(sql)
        # cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":  # 当spider.py被调用时，执行本函数
    main()
