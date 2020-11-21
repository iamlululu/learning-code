import urllib.request
response = urllib.request.urlopen('https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%B8%83%E5%81%B6%E7%8C%AB&hs=2&pn=0&spn=0&di=38830&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&ie=utf-8&oe=utf-8&cl=2&lm=-1&cs=1314931656%2C964889876&os=1535382644%2C3363172598&simid=4064635600%2C522409922&adpicid=0&lpn=0&ln=30&fr=ala&fm=&sme=&cg=&bdtype=0&oriquery=%E5%B8%83%E5%81%B6%E7%8C%AB&objurl=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201605%2F09%2F20160509144239_xSTPX.thumb.700_0.jpeg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B17tpwg2_z%26e3Bv54AzdH3Fks52AzdH3F%3Ft1%3Dc098c9ldd&gsm=1&islist=&querylist=')
cat_img = response.read()
with open('猫.jpg','wb') as f:
    f.write(cat_img)
