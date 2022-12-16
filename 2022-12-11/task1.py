f = 0b000000000000111111
b = 0b100000
gf = open("./src/lily.jpg", "rb")
for j in range(1000):
    dr = [gf.read(1), gf.read(1), gf.read(1)]
    d = (ord(dr[0]) << 16) + (ord(dr[1]) << 8) + ord(dr[2])
    for i in range(4):
        s = 6 * i
        print(chr(((d & f << s) >> s) + b), end="")
gf.close()
