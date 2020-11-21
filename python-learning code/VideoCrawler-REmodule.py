import re
import requests
import os

def Download(url):

    response = requests.get(url)
    html = response.text

    mp4_url = re.findall('srcUrl="(.*?)"', html)
    mp4_url_result = requests.get(mp4_url[0])

    name = re.findall(r'<h1 class="video-tt">(.*?)</h1>', html)
    print(name)

    f = open(name[0] + '.mp4', 'wb')
    f.write(mp4_url_result.content)
    f.close()


os.mkdir('H:/VideoDownload')
os.chdir('H:/VideoDownload')

url = 'https://www.pearvideo.com/category_130'
response = requests.get(url)

video_url = re.findall(r'<a href="(.*?)" class="vervideo-lilink actplay">', response.text)

for i in video_url:
   Download('https://www.pearvideo.com/' + i)