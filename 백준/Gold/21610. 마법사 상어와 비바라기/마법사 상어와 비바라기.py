
def step2():
    for cx,cy in [(x,y+1),(x-1,y+1),(x-1,y)] :
        if cx == -1:
            cx = N - 1
        if cy == -1:
            cy = N - 1
        if cx == N:
            cx = 0
        if cy == N:
            cy = 0
        lst[cx][cy] += 1
        cloud.append((cx,cy))
def step3():
    for ci,cj in cloud :
        for ni,nj in [(ci+1,cj+1),(ci-1,cj-1),(ci+1,cj-1),(ci-1,cj+1)] :
            if 0<=ni<N and 0<=nj<N and lst[ni][nj] != 0 :
                lst[ci][cj] += 1
def step4():
    for r in range(N) :
        for c in range(N) :
            if lst[r][c] >= 2 and (r,c) not in cloud :
                lst[r][c] -= 2
                if lst[r][c] < 0 :
                    lst[r][c] = 0
# 입력
N,M = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]
# 시작점
x, y = N - 1, 0
dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]
cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]
for _ in range(M) :
    # 이동 정보
    d,s = map(int,input().split())
    cloud2 = []
    # step1 이동 정보에 따라 구름 이동
    for cr,cc in cloud :
        cx = cr+dx[d]*s
        cy = cc+dy[d]*s
        while cx >= N :
            cx -= N
        while cy >= N :
            cy -= N
        while cx < 0 :
            cx += N
        while cy < 0 :
            cy += N
        cloud2.append((cx,cy))
        lst[cx][cy] += 1
    # step2 구름의 위치에 +1

    # step3 물복사 버그(구름이 이동할 때와는 다르게 배열 안에서만 체크)
    for ci,cj in cloud2 :
        for ni,nj in [(ci+1,cj+1),(ci-1,cj-1),(ci+1,cj-1),(ci-1,cj+1)] :
            if 0<=ni<N and 0<=nj<N and lst[ni][nj] != 0 :
                lst[ci][cj] += 1
    # step4 구름이 있지 않는 지역의 물 감소 (2 이상일때만)
    cloud.clear()
    for r in range(N):
        for c in range(N):
            if lst[r][c] >= 2 and (r, c) not in cloud2:
                lst[r][c] -= 2
                if lst[r][c] < 0:
                    lst[r][c] = 0
                cloud.append((r,c))


ret = 0
for q in range(N) :
    for w in range(N) :
        ret += lst[q][w]

print(ret)


