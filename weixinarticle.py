from bs4 import BeautifulSoup
import requests
from file import weixin_file
import html2text
import re
import datetime
import time
def clean_text(article):
    clean_article = article
    [s.extract() for s in clean_article('script')]
    for s in clean_article("div"):
        if "阅读更多" in s.text:
            s.extract()
    return str(clean_article).strip()
def format_publish_time_stamp(time_str):
    date = time.mktime(time.strptime(time_str,'%Y-%m-%d'))
    x = time.localtime(1538368652)
    pass

# base_url = "https://mp.weixin.qq.com/s/J6QZPj-JC3ai3euAfuiViQ"
base_url = "https://mp.weixin.qq.com/s?src=11&timestamp=1538724326&ver=1163&signature=fT0ncmInTyeopNfcaPiKfRYKrEgh0ZZtWhHNEcikuEAaOQGcOMVE2UnPr7aOy7B7sHoQjFS0UssztpHiblplF2wZuLHi0OoaReOAV0J*-TmZs5k*JAuJZfvjFfRqfEv-&new=1"
req = requests.get(base_url)
h = html2text.HTML2Text()
html = BeautifulSoup(req.text, 'html5lib')
print(req.text)
article_title = html.select("#activity-name")[0].getText().strip()
try:
    original_author = html.select("#meta_content > span.rich_media_meta.rich_media_meta_text")[0].getText().strip()
except:
    original_author = ""
appId_nickname = html.select("#js_name")[0].getText().strip()
try:
    publish_time = re.search(re.compile(r'var publish_time = "(.+)" \|\| ""'),str(html)).group(1)
except Exception as e:
    publish_time = ""
try:
    publish_time_stamp = re.search(re.compile(r'var ct="(.+)"\*1;'), str(html)).group(1)
except Exception as e:
    publish_time_stamp = time.time()

appId_detail = html.select("#js_profile_qrcode > div.profile_inner")[0]
appId_qrcode_url = html.select("img#js_profile_qrcode_img")[0]
appId = appId_detail.select("p")[0].select("span")[0].getText().strip()
appId_introduce = html.select("p")[1].select("span")[0].getText().strip()

# print(appId_qrcode_url)
# print(appId)
# print(appId_introduce)

article = html.select(".rich_media_content")[0]
clean_article = clean_text(article)
new_article = list(BeautifulSoup(clean_article,'lxml').select(".rich_media_content")[0].children)
md_article = []
img_list = []
for line in new_article:
    if line == "\n":
        continue
    if "推荐阅读" in str(line):
        break
    if "阅读原文" in str(line):
        break
    if "img" in str(line):
        img_url = line.select("img")[0].get("data-src")
        img_list.append(img_url)
        # md_article.append(tomd.Tomd(clean_text(line)).markdown.replace("<br/>",""))
        md_img = "![]("+img_url+")"
        md_article.append(md_img)
    else:
        md_article.append(h.handle(clean_text(line)))
markdown_file = "".join(md_article).strip()
# print(markdown_file)
