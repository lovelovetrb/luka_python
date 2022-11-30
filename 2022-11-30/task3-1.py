import random
import math

random.seed()
# s：座標(x,y)である点が)塗りつぶし部分の中に入った回数
s = 0

# 試行回数
n = 100

pie = 0

# A,C両方の点からの距離が1より小さい場合，示された部分に入ったことになる
for i in range(0, n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    r1 = math.sqrt(x**2 + y**2)
    r2 = math.sqrt((1 - x) ** 2 + (1 - y) ** 2)
    if r1 <= 1 and r2 <= 1:
        s += 1

pie = 2 * (s / n + 1)

print(pie / 2 - 1)
