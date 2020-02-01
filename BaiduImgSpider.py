import requests
import json
import os
import time
import eventlet
from bs4 import BeautifulSoup
table = {} # 解码字典
table['w'] = 'a'
table['k'] = 'b'
table['v'] = 'c'
table['1'] = 'd'
table['j'] = 'e'
table['u'] = 'f'
table['2'] = 'g'
table['i'] = 'h'
table['t'] = 'i'
table['3'] = 'j'
table['h'] = 'k'
table['s'] = 'l'
table['4'] = 'm'
table['g'] = 'n'
table['5'] = 'o'
table['r'] = 'p'
table['q'] = 'q'
table['6'] = 'r'
table['f'] = 's'
table['p'] = 't'
table['7'] = 'u'
table['e'] = 'v'
table['o'] = 'w'
table['8'] = '1'
table['d'] = '2'
table['n'] = '3'
table['9'] = '4'
table['c'] = '5'
table['m'] = '6'
table['0'] = '7'
table['b'] = '8'
table['l'] = '9'
table['a'] = '0'
def Decode(url):  # 对百度加密的objRUL进行解码，
    ans = ''
    l = len(url)
    i = 0
    while i < l:
        if url[i] == '_':
            if url[i:i+6] == '_z2C$q':
                ans += ':'
                i += 6
            elif url[i:i+6] == '_z&e3B':
                ans += '.'
                i += 6
            else:
                ans += url[i]
                i += 1
        elif url[i] == 'A':
            if url[i:i+6] == 'AzdH3F':
                ans += '/'
                i += 6
            else:
                ans += url[i]
                i += 1
        else:
            try:
                ans += table[url[i]]
                i += 1
            except:
                ans += url[i]
                i += 1
    return ans
if __name__ == '__main__':
    # base_url：后台请求request URL：访问之后是JSON数据，保存即将加载的图片，其中每张图片的URL在json中的objURL
    base_url ='http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=piao+bao+ying&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=0&ic=&hd=&latest=&copyright=&word=piao+bao+ying&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&rn=30&'
    os.makedirs('./img/', exist_ok=True)
    eventlet.monkey_patch()  # 激活 eventlet模块
    print(f'come here')
    num = 1
    for j in range(5):
        print(f'正在爬取第{j}组数据.......')
        suf_url = 'pn=' + str(j*30)
        html = json.loads(requests.get(base_url + suf_url).text) # 将JSON数据转换为dict格式
        for item in html['data']:
            try:
                url = Decode(item['objURL'])
                print(url)
                with eventlet.Timeout(2, False):  # 部分图片加载失败，所以限时2s,超过直接跳过
                    img = requests.get(url)
                    with open(f'./img/img{num}.png', 'wb') as f:
                        f.write(img.content)
                        num += 1
            except:
                pass

