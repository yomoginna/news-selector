"""
News get library
次にやること
・表示の整形検討
"""
import os
import urllib.request  # URLアクセス
import urllib.parse  # URL生成
import json  # JSON（APIの受け取り形式）
from datetime import datetime as dt  # 今日の日付

from lib import DeepLAPI


def create_news_info(index, article):
    # Webサービスからの出力を解析
    return """------ No. {} ------
[title] {}
[日本語訳] {}
******
[description] {}
[日本語訳] {}
******
[url] {}""".format(
                    index,  # No.
                    article["title"],
                    DeepLAPI.DeepLtranslate(article["title"]),
                    article["description"],
                    DeepLAPI.DeepLtranslate(article["description"]),
                    article["url"])


def create_result_info(json_result):
    # Webサービスからの出力を解析
    return f"{json_result['totalResults']}件のニュースが見つかりました。最初の10件のニュースを表示します。"


def get_latest_news_text(keywords):
    """
    APIでnews一覧をgetし、それをtext一つにまとめて返す
    """
    # 環境変数 API_KEYを取得
    API_KEY = os.environ["NEWSAPI_KEY"]

    today = dt.today().strftime('%Y-%m-%d')  # 今日の日付を取得
    # お手本url: https://newsapi.org/v2/everything?q=tesla&from=2022-05-28&sortBy=publishedAt&apiKey=API_KEY
    url = "https://newsapi.org/v2/top-headlines?{}&sortBy=publishedAt".format(
            urllib.parse.urlencode(
                {   # 入力からqueryを生成
                    "apiKey": API_KEY,
                    "q": keywords,
                    "from": today
                }))  # 日付
    # print("URL:", url)
    f_url = urllib.request.urlopen(url).read()
    json_result = json.loads(f_url.decode('utf-8'))  # JSON形式の実行結果を格納

    # 出力
    n = len(json_result["articles"])
    if n > 10:
        n = 10
    text = f"{json_result['totalResults']}件のニュースが見つかりました。最初の{n}件のニュースを表示します。\n"

    for index, article in enumerate(json_result["articles"][:n]):
        # newsAPIからの記事1つを解析->翻訳と整形をして表示文を生成する
        text = text + create_news_info(index+1, article) + '\n'

    print(text)
    return text
