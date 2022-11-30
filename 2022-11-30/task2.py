import random
import math

random.seed()
# s：座標(x,y,z)である点が球の中に入った回数
s = 0

# 試行回数
n = 100

for i in range(0, n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    z = random.uniform(-1, 1)
    r = math.sqrt(x**2 + y**2 + z**2)
    if r <= 1:
        s += 1

print(s * 8 / n / 4 * 3)
