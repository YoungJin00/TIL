def ce(n):
    p = []
    for i in range(0, 4):
        p.append((n >> ( 24 - i*8)) & 0xff)
    return p

x = 0x01020304
p = []
for i in range(0,4):
    p.append((x >> (i*8)) & 0xff)

print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))
p = ce(x)
print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))

# 4
def ce1(n):
    return (n << 24 & 0xff000000) | (n << 8 & 0xff0000) | (n >> 8 & 0xff00) | (n >> 24 & 0xff)

