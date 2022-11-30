import random
import math

random.seed()
# s：座標(x,y)である点が)塗りつぶし部分の中に入った回数
s = 0

# 試行回数
n = 100

pie = 0

# 各点からの距離が1より小さい場合，示された部分に入ったことになる
for i in range(0, n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    a_r = math.sqrt(x**2 + y**2)
    b_r = math.sqrt((1 - x) ** 2 + y**2)
    c_r = math.sqrt((1 - x) ** 2 + (1 - y) ** 2)
    d_r = math.sqrt(x**2 + (1 - y) ** 2)
    if a_r <= 1 and b_r <= 1 and c_r <= 1 and d_r <= 1:
        s += 1

pie = 3 * (s / n + math.sqrt(3) - 1)

print(1 - math.sqrt(3) + pie / 3)
