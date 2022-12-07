# 暗号化したい文字一文字
M = "大東"

separater = "-"

# 暗号化された文字列を代入する変数(10進数)
DecimalNumEnc = ""

# 文字列の長さを保jする変数
index = len(M)
counter = 0

for s in M:
    # 乱数と文章の文字コードから排他的論理和をとって暗号化(10進数)
    # 配列の最後はseparaterを削除
    if counter == index - 1:
        DecimalNumEnc += str(x ^ ord(s))
    else:
        DecimalNumEnc += str(x ^ ord(s)) + separater

    counter += 1


