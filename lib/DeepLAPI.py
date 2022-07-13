"""
translate by DeepL API library
textを日本語に変換する
"""
import os
import urllib.request  # URLアクセス
import urllib.parse  # URL生成
import json  # JSON（APIの受け取り形式）


def access2DeepL(text):
    # 環境変数 DeepLのauth_keyを取得
    AUTH_KEY = os.environ["DEEPL_AUTH_KEY"]
    # お手本url: https://api-free.deepl.com/v2/translate \
    # -d auth_key=AUTH_KEY\
    # -d "text=Hello, world!"  \
    # -d "target_lang=DE"
    # urlを生成
    url = "https://api-free.deepl.com/v2/translate?&{}&target_lang=JA".format(
            urllib.parse.urlencode(
                {
                    "auth_key": AUTH_KEY,
                    "text": text
                }))
    # urlでdeepLにアクセスし、結果を取得
    f_url = urllib.request.urlopen(url).read()
    # 結果をjson形式に変換
    json_result = json.loads(f_url.decode('utf-8'))

    return json_result


def DeepLtranslate(text):
    # DeepLにアクセスして、json形式の結果を取得
    json_result = access2DeepL(text)
    return json_result['translations'][0]['text']
