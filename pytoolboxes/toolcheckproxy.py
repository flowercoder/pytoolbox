import re
from fake_useragent import UserAgent
import requests

# check proxy by http://icanhazip.com
def checkproxy(iport):
    try:
        ip = iport[:iport.find(":")]
        proxy = {
          'http': f'http://{iport}',
          'https': f'https://{iport}'
        }
        print(proxy)
        ua = UserAgent(verify_ssl=False)
        head = {'User-Agent': ua.random,
               'Connection': 'keep-alive'}
        '''http://icanhazip.com会返回当前的IP地址'''
        checkres = requests.get('http://icanhazip.com', headers=head, proxies=proxy, timeout=3)
        # checkres = requests.get('http://icanhazip.com', headers=head, timeout=5)
        step = str(checkres.text)
        pattern = re.compile(r'[0-9].+')
        res = pattern.findall(step)
        test = [ip] == res
        print(f"proxy:[{iport}]checkresult:[{test}]")
        return iport
    except:
        print("this proxy does not work!!!")
if __name__ == '__main__':
    checkproxy("58.246.58.150:9002")