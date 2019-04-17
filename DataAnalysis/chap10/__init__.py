import requests
import json
from lxml import etree
import re
from selenium import webdriver
query = '王祖贤'


# 下载图片
def download(src, id):
    # dir = './' + str(id) + '.webp'
    rstr = r"[\/\\\:\*\?\"\<\>\|]"
    title = re.sub(rstr, "", id)
    dir = './' + str(title) + '.jpg'
    try:
        pic = requests.get(src, timeout=10)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('图片无法下载')


# 获取电影数量
def get_film_amount(performer_name):
    url = 'https://www.douban.com/j/search?q=' + query + '&start=0&cat=1002'
    result = requests.get(url)
    result_obj = json.loads(result.text)
    return int(result_obj['total'])


# 获取电影信息
def get_film_info(query_name):
    # XPath规则
    title_xpath = "//div[@class='content']/div[@class='title']/h3/a"
    pic_xpath = "//div[@class='pic']/a[@class='nbg']/img/@src"

    titles = []
    pics = []

    film_amount = get_film_amount(query_name)

    for i in range(0, film_amount, 20):
        url = 'https://www.douban.com/j/search?q=' + query_name + '&start='+ str(i)+ '&cat=1002'
        result = requests.get(url)
        result_obj = json.loads(result.text)

        for item in result_obj['items']:
            html = etree.HTML(item)
            tmp_titles = html.xpath(title_xpath)
            tmp_pics = html.xpath(pic_xpath)

            if 'default_small' not in tmp_pics[0]:
                titles.append(tmp_titles[0].text.strip())
                pics.append(tmp_pics[0])

    return {'name': query_name, 'amount': film_amount, 'list': zip(titles,pics)}


def get_film_by_json():
    info = get_film_info(query)
    for title, src in info.get('list'):
        download(src, title)


def get_film_by_selenium():
    request_url = 'https://movie.douban.com/subject_search?search_text=' + query + '&cat=1002'
    # options = webdriver.ChromeOptions
    # options.add_argument(argument='--incogito')  #隐身模式
    driver = webdriver.Chrome()
    driver.get(request_url)
    html = etree.HTML(driver.page_source)

    src_xpath = "//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
    title_xpath = "//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"
    srcs = list(html.xpath(src_xpath))
    print(len(srcs))
    titles = html.xpath(title_xpath)
    # for src, title in zip(srcs, titles):
    #     download(src, title.text)
    driver.close()


def get_picture():
    for i in range(0, 30, 20) :
        url = 'https://www.douban.com/j/search_photo?q='+ query +'&limit=20&start=' + str(i)
        html = requests.get(url).text
        response = json.loads(html, encoding='utf-8')
        for image in response['images']:
            print(image['src'])
            download(image['src'], image['id'])


get_film_by_selenium()