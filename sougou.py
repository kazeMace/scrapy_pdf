from bs4 import BeautifulSoup
import requests

base_url = "http://mp.weixin.qq.com/profile?src=3&timestamp=1538726852&ver=1&signature=B8LotqP-Y1OqKIEnKb*NccVMGWVZQLBCuEvFgxrTLOJRvU37hny0HtKtI4RpMQYe3mqmhqiPJZGsnhe7z53KnQ=="
req = requests.get(base_url)
print(req.text)