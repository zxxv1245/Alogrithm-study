from itertools import combinations
from collections import deque
def bfs() :

    while Q :
        x,y = Q.popleft()

        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] :
            if 0<=nx<N and 0<=ny<N :
                if lst[nx][ny] == 1 :
                    visited[nx][ny] = -1
                elif lst[nx][ny] != 1 and visited[nx][ny] == 0 :
                    visited[nx][ny] = visited[x][y] + 1
                    Q.append((nx,ny))

N,M = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]
tot = []
for i in range(N) :
    for j in range(N) :
        if lst[i][j] == 2 :
            tot.append((i,j))

combi = combinations(tot,M)

minV = 21e8
flag = 1
ret = []
for a in combi :
    visited = [[0]*N for _ in range(N)]
    Q = deque()
    for x,y in a :
        visited[x][y] = 1
        Q.append((x,y))
    bfs()

    zero = 0
    maxV = -1
    for r in range(N) :
        for c in range(N) :
            if visited[r][c] == 0 and lst[r][c] != 1 :
                zero += 1
            else :
                if maxV < visited[r][c] :
                    maxV = visited[r][c]

    if zero == 0 :
        flag = 0
        ret.append(maxV)


if flag == 1 :
    print(-1)
else :
    print(min(ret)-1)