# 알파벳
import sys
input = sys.stdin.readline
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def dfs(x,y,cnt) :
    global maxV

    maxV = max(maxV,cnt)
    for a in range(4) :
        nx = x + dx[a]
        ny = y + dy[a]
        if not(0<=nx<N and 0<=ny<M) or alpha[ord(lst[nx][ny])-65] == 1 : continue
        alpha[ord(lst[nx][ny]) - 65] = 1
        dfs(nx,ny,cnt + 1)
        alpha[ord(lst[nx][ny]) - 65] = 0


N,M = map(int,input().split())

lst = [list(input()) for _ in range(N)]
alpha = [0]*26
alpha[ord(lst[0][0]) - 65] = 1


maxV = -21e8
dfs(0,0,1)
print(maxV)

