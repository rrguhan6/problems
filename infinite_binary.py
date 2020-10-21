# 0
# 1
# 00
# 11
# 000
# 001


b = ['0', '1']

while(True):
    a = b.pop(0)
    print(a)

    b.append(a + '0')
    b.append(a + '1')
