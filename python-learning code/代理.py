import urllib.request

url = 'http://www.whatismyip.com.tw'

proxy = urllib.request.ProxyHandler({'http':'222.95.240.100:3000'})

opener = urllib.request.build_opener(proxy)

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')

print(html)


