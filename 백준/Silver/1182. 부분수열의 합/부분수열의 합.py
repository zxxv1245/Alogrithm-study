def abc(k,arr) :
    global cnt




    if k == N :
        if len(arr) >= 1 and sum(arr) == S:
            cnt += 1
        return

    abc(k+1,arr)
    abc(k+1,arr+[lst[k]])


N,S = map(int,input().split())

lst = list(map(int,input().split()))
prev = 0
cnt = 0
abc(0,[])
print(cnt)
