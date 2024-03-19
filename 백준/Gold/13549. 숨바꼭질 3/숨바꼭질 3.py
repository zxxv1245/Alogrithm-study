from collections import deque

def bfs() :

    while Q :
        x = Q.popleft()

        if x == M :
            return lst[x]

        for i in [x*2,x-1,x+1] :
            if 0 <= i <= 100000 and lst[i] == 0 :
                if i == x*2 :
                    lst[i] = lst[x]
                    Q.append(i)
                else :
                    lst[i] = lst[x]+1
                    Q.append(i)
                    
                    
N,M = map(int,input().split())
lst = [0]*100001
Q = deque()
Q.append(N)

print(bfs())