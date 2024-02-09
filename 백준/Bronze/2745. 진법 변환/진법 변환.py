N, B = input().split()

indexA = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ret = 0

for i in N :
    c = indexA.index(i)
    ret = ret*int(B) + c

print(ret)