#import turtle as t
#for i in range(7): #重复7次
#	t.forward(100) #画笔前进200
#	t.right(51.42) #向右转90度
	#t.circle(100,360)
	#t.begin_fill()
	#t.circle(100,180)
	#t.end_fill()
#pip install urllib3 BeautifulSoup4
import urllib3

def download_conent(url):
	http = urllib3.PoolManager()
	response = http.request("Get",url)
	reponse_data = response.data
	html_content - response_data.decode()
	return html_content

def save_to_file(filename, content):
    fo = open(filename, "w", encoding="utf-8")
    fo.write(content)
    fo.close()


def main():
    # 下载报考指南的网页
    url = "https://zkaoy.com/sions/exam"
    result = download_content(url)
    save_to_file("tips1.html", result)


if __name__ == '__main__':
    main()

# requests 代码
# file_name:Crawler_requests.py
import requests


def download_content(url):
 
def save_to_file(filename, content):
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(content)


def main():
    # 下载报考指南的网页
    url = "https://zkaoy.com/sions/exam"
    result = download_content(url)
    save_to_file("tips1.html", result)


if __name__ == '__main__':
    main()

# file_name:html_parse.py
# 解析方法一
from bs4 import BeautifulSoup

# 输入参数为要分析的 html 文件名，返回值为对应的 BeautifulSoup 对象
def create_doc_from_filename(filename):
	with open(filename, "r", encoding='utf-8') as f:
		html_content = f.read()
		doc = BeautifulSoup(html_content)
	return doc

def parse(doc):
	post_list = doc.find_all("div", class_="post-info")
	for post in post_list:
		link = post.find_all("a")[1]
		print(link.text.strip())
		print(link["href"])

def main():
	filename = "tips1.html"
	doc = create_doc_from_filename(filename)
	parse(doc)

if __name__ == '__main__':
	main()

#file_name:html_parse_lxml.py
from bs4 import BeautifulSoup

# 输入参数为要分析的 html 文件名，返回值为对应的 BeautifulSoup 对象
def create_doc_from_filename(filename):
	with open(filename, "r", encoding='utf-8') as f:
		html_content = f.read()
		soup = BeautifulSoup(html_content, "lxml")
	return soup

def parse(soup):
	post_list = soup.find_all("div", class_="post-info")
	for post in post_list:
		link = post.find_all("a")[1]
		print(link.text.strip())
		print(link["href"])

def main():
	filename = "tips1.html"
	soup = create_doc_from_filename(filename)
	parse(soup)

if __name__ == '__main__':
	main()

