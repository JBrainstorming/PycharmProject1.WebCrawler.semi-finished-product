import urllib.request

"""
  #获取一个get请求
response = urllib.request.urlopen("http://www.baidu.com")

print(response)
#运行结果：<http.client.HTTPResponse object at 0x000001CECC653CA0>

#print(response.read())
'''运行结果：
b'<!DOCTYPE html><!--STATUS OK--><html><head><meta http-equiv="Content-Type" content="text/html;charset=utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><meta content="always" name="referrer"><meta name="theme-color" content="#ffffff"><meta name="description" content="\xe5\x85\xa8\xe7\x90\x83\xe9\xa2\x86\xe5\x85\x88\xe7\x9a\x84\xe4\xb8\xad\xe6\x96\x87\xe6\x90\x9c\xe7\xb4\xa2\xe5\xbc\x95\xe6\x93\x8e\xe3\x80\x81\xe8\x87\xb4\xe5\x8a\x9b\xe4\xba\x8e\xe8\xae\xa9\xe7\xbd\x91\xe6\xb0\x91\xe6\x9b\xb4\xe4\xbe\xbf\xe6\x8d\xb7\xe5\x9c\xb0\xe8\x8e\xb7\xe5\x8f\x96\xe4\xbf\xa1\xe6\x81\xaf\xef\xbc\x8c\xe6\x89\xbe\xe5\x88\xb0\xe6\x89\x80\xe6\xb1\x82\xe3\x80\x82\xe7\x99\xbe\xe5\xba\xa6\xe8\xb6\x85\xe8\xbf\x87\xe5\x8d\x83\xe4\xba\xbf\xe7\x9a\x84\xe4\xb8\xad\xe6\x96\x87\xe7\xbd\x91\xe9\xa1\xb5\xe6\x95\xb0\xe6\x8d\xae\xe5\xba\x93\xef\xbc\x8c\xe5\x8f\xaf\xe4\xbb\xa5\xe7\x9e\xac\xe9\x97\xb4\xe6\x89\xbe\xe5\x88\xb0\xe7\x9b\xb8\xe5\x85\xb3\xe7\x9a\x84\xe6\x90\x9c\xe7\xb4\xa2\xe7\xbb\x93\xe6\x9e\x9c\xe3\x80\x82"><link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" /><link rel="search" type="application/opensearchdescription+xml" href="/content-search.xml" title="\xe7\x99\xbe\xe5\xba\xa6\xe6\x90\x9c\xe7\xb4\xa2" /><link rel="icon" sizes="any" mask href="//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg"><link rel="dns-prefetch" href="//dss0.bdstatic.com"/><link rel="dns-prefetch" href="//dss1.bdstatic.com"/><link rel="dns-prefetch" href="//ss1.bdstatic.com"/><link rel="dns-prefetch" href="//sp0.baidu.com"/><link rel="dns-prefetch" href="//sp1.baidu.com"/><link rel="dns-prefetch" href="//sp2.baidu.com"/><link rel="apple-touch-icon-precomposed" href="https://psstatic.cdn.bcebos.com/video/wiseindex/aa6eef91f8b5b1a33b454c401_1660835115000.png"><title>\xe7\x99\xbe\xe5\xba\xa6\xe4\xb8\x80\xe4\xb8\x8b\xef\xbc\x8c\xe4\xbd\xa0\xe5\xb0\xb1\xe7\x9f\xa5\xe9\x81\x93</title><style index="newi" type="text/css">#form .bdsug{top:39px}.bdsug{display:none;position:absolute;width:535px;background:#fff;border:1px solid #ccc!important;_overflow:hidden;box-shadow:1px 1px 3px #ededed;-webkit-box-shadow:1px 1px 3px #ededed;-moz-box-shadow:1px 1px 3px #ededed;-o-box-shadow:1px 1px 3px #ededed}.bdsug li{width:519px;color:#000;font:14px arial;line-height:25px;padding:0 8px;position:relative;cursor:default}.bdsug li.bdsug-s{background:#f0f0f0}.bdsug-store span,.bdsug-store b{color:#7A77C8}.bdsug-store-del{font-size:12px;color:#666;text-decoration:underline;position:absolute;right:8px;top:0;cursor:pointer;display:none}.bdsug-s .bdsug-store-del{display:inline-block}.bdsug-ala{display:inline-block;border-bottom:1px solid #e6e6e6}.bdsug-ala h3{line-height:14px;background:url(//www.baidu.com/img/sug_bd.png?v=09816787.png) no-repeat left center;margin:6px 0 4px;font-size:12px;font-weight:400;color:#7B7B7B;
'''
print(response.read().decode("utf-8"))
"""
  #获取一个post请求

#httpbin.org: 一个专门用于测试服务器相应的网站
#测试post："http://httpbin.org/post"

import urllib.parse  #解析器
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/post",data=data)
print(response.read().decode("utf-8"))

respons3 = urllib.request.urlopen("http://httpbin.org/get")
print(respons3.read().decode("utf-8"))

try:
    response = urllib.request.urlopen("http://httpbin.org/post", timeout=0.0001)
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("timeout!")

response4 = urllib.request.urlopen("http://httpbin.org/get")

#response5 = urllib.request.urlopen("https://douban.com")
#print(response5.status)

response6 = urllib.request.urlopen("http://www.baidu.com")
print(response6.getheader("Server"))

url = "https://movie.douban.com"

headers = {
"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42"
}
data = bytes(urllib.parse.urlencode({'name':'江心月'}),encoding="utf-8")

req = urllib.request.Request(url = url,data = data,headers = headers,method="POST")

response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
