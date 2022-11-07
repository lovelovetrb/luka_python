import re


str = r'<tr><td>330-9301</td><td>さいたま市</td></tr>'
rex = r'<td>(.+?)</td>'


results = re.findall(rex, str)

print(results[1]+'の郵便番号は'+results[0]+'です')
