import requests
from bs4 import BeautifulSoup
import re

# 设置请求头
# 更换一下爬虫的User-Agent，这是最常规的爬虫设置
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


# 获取天气信息
def get_weather():
    html = requests.get("http://www.weather.com.cn/weather/101280601.shtml", headers=headers)
    html.encoding = "utf-8"
    if html.status_code == 200:
        soup = BeautifulSoup(html.text, "lxml")
        light_list = soup.select('p.tem span')
        night_list = soup.select('p.tem i')
        for index in range(0, len(light_list)):
            print('白天温度：{0}, 夜晚温度：{1}'.format(light_list[index].get_text(), night_list[index].get_text()))


# 获取贴吧回复数
def get_bar():
    html = requests.get("http://tieba.baidu.com/f?ie=utf-8&kw=python3", headers=headers)
    html.encoding = "utf-8"
    if html.status_code == 200:
        # <span class="threadlist_rep_num center_text" title="回复">9</span>
        tag_list = re.findall(r'(?<="回复">)\d*(?=</span>)', html.text)
        print(tag_list)


if __name__ == '__main__':
    get_weather()
    get_bar()
