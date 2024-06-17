# 从origin.txt中读取所有以 https://mp.weixin.qq.com/ 开头的链接，爬取网页内容，保存在/data目录下
import requests
import re
import os

index = 0

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    try:
        html = re.findall(r'<div class="rich_media_content(.*?)>(.*?)</div>', response.text, re.S)
        print('成功爬取' + url)
        title = re.findall(r'var title = \'(.*?)\';', response.text)[0]
        timestamp = re.findall(r'var oriCreateTime = \'(.*?)\';', response.text)[0]
        addTitle = '<Title title="' + title + '" link="' + url + '" timestamp="' + timestamp + '"/>\n'
        return addTitle+html[0][1]
    except:
        print('非文章类型，跳过')
        return ''

def save_html(url, html):
    if html == '':
        return
    global index
    index += 1
    if not os.path.exists('data'):
        os.makedirs('data')
    with open('data/' + str(index) + '.html', 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    with open('origin.txt', 'r', encoding='utf-8') as f:
        urls = f.readlines()
    # 全文搜索
    for url in urls:
        if 'https://mp.weixin.qq.com/' in url:
            link = re.findall(r'"doc_url": "(.*?)"', url)
            save_html(link, get_html(link[0]))

if __name__ == '__main__':
    main()