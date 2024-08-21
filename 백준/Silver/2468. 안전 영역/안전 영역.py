dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs() :


    while Q :
        x,y = Q.popleft()

        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] > K and visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                arr[nx][ny] = 0
                Q.append((nx,ny))

from collections import deque
import copy
N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]
Q = deque()
maxV = 0
for i in range(N) :
    for j in range(N) :
        if maxV < lst[i][j] :
            maxV = lst[i][j]
maxVV = -21e8

K = 0
while K <= maxV :
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    arr = copy.deepcopy(lst)
    for x in range(N) :
        for y in range(N) :
            if arr[x][y] > K and visited[x][y] == 0:
                Q.append((x,y))
                bfs()
                cnt += 1

    if maxVV < cnt :
        maxVV = cnt

    K += 1

print(maxVV)