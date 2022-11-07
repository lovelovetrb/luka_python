import re

emails = [
    's181419999@st.daito.ac.jp',  # 検索に引っかかる　
    '18870111@shizuoka.ac.jp',
    'info@yotuba.company.ne.jp',  # 検索に引っかかる　
    '8721837@tokyo.agriculture.ac.jp',  # 検索に引っかかる　
    '17766532@city-sakado.ed.jp'
]

# メールアドレスのドメイン名にピリオドが3個含まれるような正規表現
rex = r'(.*)@(.*)¥.(.*)¥.(.*)¥.(.*)'

for email in emails:
    # 正規表現モジュール re のsearch関数でデータ内を検索
    result = re.search(rex, email)
    if result:
        print('結果 : ', result.group())
