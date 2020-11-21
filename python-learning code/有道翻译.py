import urllib.request
import urllib.parse
import json
import time
while True:
    contens = input('请输入需要翻译的内容：(输入!!退出程序)')
    if contens == '!!':
        break
    url = 'http://fanyi.youdao.com/translate'
    data = {}
    data['i'] =contens
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] ='dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15825411119972'
    data['sign'] = '0e299dedf8c184b5505080d84e891cef'
    data['ts'] = '1582541111997'
    data['bv'] = 'ce084dcc4db5baebbfa03de553252029'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTlME'
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3742.400 QQBrowser/10.5.3864.400')

    respond = urllib.request.urlopen(req)
    f = respond.read().decode('utf-8')
    target =json.loads(f)
    print('翻译的结果为：%s' % target['translateResult'][0][0]["tgt"])
    time.sleep(5)