from bs4 import BeautifulSoup
import requests
import file
import html2text



def clean_text(article):
    clean_article = article
    [s.extract() for s in clean_article('script')]
    for s in clean_article("div"):
        if "阅读更多" in s.text:
            s.extract()
    return str(clean_article).strip()

headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Cookie": "TY_SESSION_ID=80e15cb8-b4ec-4850-b5d6-04d7d890e005; dc_session_id=10_1538652544866.693652; uuid_tt_dd=2158444260722136093_20181004; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1538623745; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; dc_tos=pg21ti; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1538623927",
"Host": "blog.csdn.net",
"Referer": "https://www.csdn.net/",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
}

h = html2text.HTML2Text()
base_url = "https://blog.csdn.net/dQCFKyQDXYm3F8rB0/article/details/82922394"
# base_url = "https://blog.csdn.net/meishenghang1148/article/details/78570243"
req = requests.get(base_url)
html = BeautifulSoup(req.text, "lxml")
# html = BeautifulSoup(file.html_file, 'lxml')
content = html.select("#blog-content-box")
article_title = html.select("#mainBox > main > div.blog-content-box > div > div > div.article-title-box > h1")[0].getText()
article = html.select("article")[0]
clean_article = clean_text(article)
origin_time = html.select("#mainBox > main > div.blog-content-box > div > div > div.article-info-box > div.article-bar-top > span.time")[0].getText()
original_author = html.select("#mainBox > main > div.blog-content-box > div > div > div.article-info-box > div.article-bar-top > a")[0].getText()
original_author_url = html.select("#mainBox > main > div.blog-content-box > div > div > div.article-info-box > div.article-bar-top > a")[0].get("href")
img_list_html = article.select("img")
img_list = [img_tag.get("src") for img_tag in img_list_html]
# print(img_list)
# print(origin_time)
# print(original_author)
# print(original_author_url)
print(h.handle(clean_article))

