#import turtle as t
#for i in range(7): #重复7次
#	t.forward(100) #画笔前进200
#	t.right(51.42) #向右转90度
	#t.circle(100,360)
	#t.begin_fill()
	#t.circle(100,180)
	#t.end_fill()
pip install urllib3 BeautifulSoup4
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
