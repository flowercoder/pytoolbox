import requests as requests
from fake_useragent import UserAgent
from lxml import etree

def reqbee(url):
    # url = "https://www.beesproxy.com/free/page/2"

    ua = UserAgent(verify_ssl=False)
    headers = {
        'User-agent': ua.random
    }
    payload={}
    response= requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)
    page = etree.HTML(response.text)
    return page
# print(type(page))
def getproxy(page):
    proxys = []
    for i in range(1, 20):
        j = str(i)
        ip = page.xpath('/html/body/div[2]/section[1]/div/div/div/div[1]/div/article/div[2]/div/figure/table/tbody/tr['+j+']/td[1]/text()')
        port = page.xpath('/html/body/div[2]/section[1]/div/div/div/div[1]/div/article/div[2]/div/figure/table/tbody/tr['+j+']/td[2]/text()')
        res = f"{ip[0]}:{port[0]}"
        proxys.append(res)
    print(proxys)
    return proxys

if __name__ == '__main__':
    getproxy(reqbee("https://www.beesproxy.com/free/page/2"))
