def abc(k) :

    if k == M :
        print(*path)
        return

    for i in range(N) :
        
        path[k] = lst[i]
        abc(k+1)

N,M =map(int,input().split())

lst = list(range(1,N+1))
path = [0]*M

abc(0)