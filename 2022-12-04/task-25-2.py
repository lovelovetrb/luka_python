# p = 307
# q = 311

# 公開鍵
n = 95477
#  n = p * q
a = 94873

# 秘密鍵
b = 7297

# 暗号化対象
M = "a"
# 暗号
m = 0

# 暗号
m = (ord(M) ** a) % n

# 復号
M = (m**b) % n

print(chr(M))
