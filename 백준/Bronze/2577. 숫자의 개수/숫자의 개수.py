A,B,C = map(int,open(0))
ret = A*B*C
ret = str(ret)
arr = [0]*10
for a in ret :
    arr[int(a)] += 1

for b in arr :
    print(b)