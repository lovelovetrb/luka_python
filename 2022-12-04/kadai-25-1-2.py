import random

p = 100

# 初期化
random.seed(p)

# 2^16の範囲で乱数を生成
x = random.randrange(2**16)
print(x)

# 0bで始まる2進数表現を得る
print(bin(x))

# 暗号化したい文字一文字
string = "大東"

separater = "-"

# 暗号化された文字列を代入する変数(2進数)
BinaryNumEnc = ""

# 暗号化された文字列を代入する変数(10進数)
DecimalNumEnc = ""

# 文字列の長さを保jする変数
index = len(string)
counter = 0

for s in string:
    # 乱数と文章の文字コードから排他的論理和をとって暗号化(2進数)
    # 配列の最後はseparaterを削除
    if counter == index - 1:
        BinaryNumEnc += str(bin(x ^ ord(s)))
    else:
        BinaryNumEnc += str(bin(x ^ ord(s))) + separater

    # 乱数と文章の文字コードから排他的論理和をとって暗号化(10進数)
    # 配列の最後はseparaterを削除
    if counter == index - 1:
        DecimalNumEnc += str(x ^ ord(s))
    else:
        DecimalNumEnc += str(x ^ ord(s)) + separater

    counter += 1


print("2進数の暗号文:" + BinaryNumEnc)
print("10進数の暗号文:" + DecimalNumEnc)

# Encode対象の文字列をseparaterで削除し配列として保持
BinEncList = BinaryNumEnc.split(separater)
DevEncList = DecimalNumEnc.split(separater)

# 平文化した文字列を保持する変数
BinDecText = ""
DevDecText = ""

for enc in BinEncList:
    # 複合化されたデータ(2進数)
    dec = x ^ int(enc, 2)

    # 文字列変換
    BinDecText += chr(dec)

for enc in DevEncList:
    # 複合化されたデータ(10進数)
    dec = x ^ int(enc)

    # 文字列変換
    DevDecText += chr(dec)

print("2進数の平文：" + BinDecText)
print("10進数の平文：" + DevDecText)
