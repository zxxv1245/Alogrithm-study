def abc(k) :
    # global cnt
    # print(path)
    # if path and sum(path) == S:
    #     cnt += 1


    if k == M :
        # if sum(path) == S :
        #     cnt += 1
        print(*path)
        return

    for i in range(N) :
        if v1[i] == 1 : continue
        v1[i] = 1
        path.append(lst[i])
        abc(k+1)
        path.pop()
        v1[i] = 0

N,M = map(int,input().split())

lst = list(map(int,input().split()))
lst.sort()
path = []
v1 = [0]*N
# cnt = 0
abc(0)
# print(cnt)
