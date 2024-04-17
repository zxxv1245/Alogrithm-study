a,b,c,d,e,f = map(int,input().split())
flag = 0
for i in range(1,2000):
    for j in range(1,2000) :
        if (a*(i-1000) + b*(j-1000) == c) and (d*(i-1000) + e*(j-1000) == f) :
            flag = 1
            x = i-1000
            y = j-1000
            break
    if flag == 1 :
        break

print(x, y)