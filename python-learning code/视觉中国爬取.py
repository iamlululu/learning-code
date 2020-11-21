import os
import requests
from bs4 import BeautifulSoup

# 设置路径
if not (os.path.exists('H:/Download_pic/')):
    os.mkdir('H:/Download_pic/')
path = 'H:/Download_pic/'


# 给出主站网址，初始化请求头
url = 'https://www.vcg.com/creative/'
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
headers = {'User-Agent': agent,'Referer': 'https://www.vcg.com/'}
second_headers = {'User-Agent':agent,'Referer': 'https://www.vcg.com/creative/'}
third_headers ={'User-Agent': agent,'Referer': 'https://www.vcg.com/favor/pic-share/?fid=753501'}
forth_headers = {'User-Agent': agent}


# 对主站发起请求，返回html信息，进行解析
response = requests.get(url,headers = headers)
soup = BeautifulSoup(response.text,'html.parser')
# soup.prettify()
# print(soup)

# 提取主站内次级页面的地址和名称
same_url = 'https://www.vcg.com/favor/pic-share/?fid='
url_result =soup.find_all('a',target="_blank",class_="_2XNBX")

for i in url_result:
    # print(i['href'][-6:])
    second_url = same_url + i['href'][-6:]            # 拼接取得二级页面地址
    # print(second_url)
    foder_name = i.div.next_sibling.text              # 取得二级页面的名称，作为后续文件夹名称

    # 建立文件夹
    if (foder_name != ' '):
        print('准备抓取'+foder_name)
        if(os.path.exists(path+foder_name)):
            print('目录已经存在')
        else:
            os.mkdir(path+foder_name)
    os.chdir(path+foder_name)  # 切换到建立的文件夹


# 对二级页面进行访问
    response = requests.get(second_url,headers =second_headers)
    soup = BeautifulSoup(response.text,'html.parser')


# 取得每张图片的名字;取得图片一级地址,并访问取得图片真实地址
    pic_url = soup.find_all('a', class_="search-result-asset-link")
    result = soup.find_all('li', class_="event-id")
    for each_url, each_name in zip(pic_url,result):

        pic_addr = each_url['href']                    # 取得图片一级地址
        pic_name = each_name.span.next_sibling.text    # 取得图片名称


        # 对图片一级地址进行请求访问,取得图片真实地址
        response = requests.get(pic_addr, headers=third_headers)
        sp_ = BeautifulSoup(response.text, 'html.parser')
        sp = sp_.find_all('div', style="position:relative")
        # print(sp[-1].img['data-src'][:55])

        real_pic_url = 'http:' + sp[-1].img['data-src']         # 取得图片真实地址
        print('准备下载' + pic_name)

        # 对图片地址进行访问
        response = requests.get(real_pic_url, headers=forth_headers)

        # 保存图片
        f = open(pic_name+'.jpg','wb')
        f.write(response.content)
        f.close()
        print('下载完成' + pic_name)

    print(foder_name+'下载完成')