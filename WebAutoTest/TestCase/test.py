a = 1
b = 2
x = 100000000000
y = 100000000000

p = a*(10**(x-1))%b
l = []
for i in range(x, y+1):
    zheng = str((p*10)//b)
    p = (p*10)%b
    l.append(zheng)
r = ''.join(l)
print(r)