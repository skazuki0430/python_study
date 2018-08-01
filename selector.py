# coding: UTF-8
import urllib.request
from bs4 import BeautifulSoup

# アクセスするURL
url = "https://www.nikkei.com/markets/kabu/"

# URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰ってきます
with urllib.request.urlopen(url) as response:
    html = response.read()

# instanceからHTMLを取り出して、BeautifulSoupで扱えるようにパースします
soup = BeautifulSoup(html, "html.parser")

# CSSセレクターを使って指定した場所のtextを表示します
css_selector = (r"#CONTENTS_MARROW > div.mk-top_stock_average.cmn-clearfix > div.cmn-clearfix > div.mkc-guidepost > div.mkc-prices > span.mkc-stock_prices")
print(soup.select_one (css_selector).text)

