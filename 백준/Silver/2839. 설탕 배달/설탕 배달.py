
N = int(input())

cnt = -1
minV = 21e8
if N-3 >= 0 or N-5 >= 0 :
    for i in range(N//3,-1,-1) :
        for j in range(0,N//5+1,1) :
            if 3*i + 5*j == N :
                cnt = i + j
                if minV > cnt :
                    minV = cnt

print(cnt)