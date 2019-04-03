def inToBin32(i):
    return (bin(((1<<32)-1)&i)[2:]).zfill(32)
#(1<<32)-1 = 0xffffffff


def bin32ToInt(s):
    return int(s[1:],2)-int(s[0])*(1<<31)

i = 10
print(i)
a= (1<<32)
#2的32次方
print(a)
a = a-1
print(a)
a = a&i
print(a)
a = bin(a)
print(a)
a = a[2:]
print(a)
a = a.zfill(32)
print(a)
