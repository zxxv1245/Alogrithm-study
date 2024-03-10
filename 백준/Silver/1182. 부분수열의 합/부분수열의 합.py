def abc(k,start) :
    global cnt
    # print(path)
    if path and sum(path) == S:
        cnt += 1


    if k == N :
        # if sum(path) == S :
        #     cnt += 1
        return

    for i in range(start,N) :
        if v1[i] == 1 : continue
        v1[i] = 1
        path.append(lst[i])
        abc(k+1,i+1)
        path.pop()
        v1[i] = 0

N,S = map(int,input().split())

lst = list(map(int,input().split()))

path = []
v1 = [0]*N
cnt = 0
abc(0,0)
print(cnt)
