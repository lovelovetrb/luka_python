# 問4のプログラムは, 数字の中を検索する際に 正規表現 と呼ばれる方法で文字列のルールを決めて
# そのルールに合う部分を検索しているよ！

#  正規表現の書き方についてのおすすめサイト
# https://ai-inter1.com/python-regex/#st-toc-h-9
# 適当に見つけただけだから python 正規表現 書き方 とかでググってみてね〜

import re

str = ['1.2345', '12.345', '123.45', '1234.5']

# 変数 rex の中身が正規表現！
# カッコで囲むと後で search関数を使うときに括弧の中に括ったところだけ取り出せるよ！
rex = r'([1-9]+)¥.([1-9]+)'


for s in str:
    # ここで実際に検索をしているよ！
    kekka = re.search(rex, s)
    if kekka:
        print('整数部分', kekka.group(1))
        print('少数部分', kekka.group(2))
        # おまけ
        print('全体', kekka.group(), '¥n')
