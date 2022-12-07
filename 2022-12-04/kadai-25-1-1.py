import random

# 乱数初期化
p = 100
# 乱数発生
random.seed(p)
x = random.randrange(2**16)

# 乱数(10 進数)
print(x)
# 乱数(2 進数)
print(bin(x))

# 平文を「東」とする
str = "東"

# 文字符号(10 進数)
print(ord(str))
# 文字符号(2 進数)
print(bin(ord(str)))

# 暗号化
enc = x ^ ord(str)

# 暗号(10 進数)
print(enc)
# 暗号(2 進数)
print(bin(enc))

# 復号化
dec = x ^ enc
# 復号化されたデータ(10 進数)
print(dec)
# 復号化されたデータ(2 進数)
print(bin(dec))
# 復号化されたデータ(文字)
print(chr(dec))
