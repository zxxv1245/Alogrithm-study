from collections import deque
from copy import deepcopy
# 2 <= N <= Q
# 1 <= Q <= 1000
# 0 <= A[r][c] <= 100
# 0 <= L <= N

# 입력
# 첫째 줄 N Q
# 둘째 줄부터 2**N 배열
# 마지막 줄 Q개 파이어스톰 시전

N,Q = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(2**N)]
asd = list(map(int,input().split()))

Qlst = deque()
for s in asd :
    Qlst.append(s)


# 구현
# Qlst 앞에서 하나 뽑아서 배열 돌리기

while Qlst :
    L = Qlst.popleft()
    for a in range(0,2**N,2**L) :
        for b in range(0,2**N,2**L) :
            small_lst = [[0] * (2 ** L) for _ in range(2 ** L)]
            for c in range(2**L) :
                for d in range(2**L) :
                    small_lst[c][d] = lst[a+c][b+d]

            new_small_lst = [[0] * (2 ** L) for _ in range(2 ** L)]
            for i in range(2**L) :
                for j in range(2**L) :
                    new_small_lst[j][(2**L)-i-1] = small_lst[i][j]

            for e in range(2**L) :
                for f in range(2**L) :
                    lst[a+e][b+f] = new_small_lst[e][f]

    # 배열 다 돌렸으면 다시 배열 돌면서 주변 칸 3개 이상에 얼음이 없다면 해당 칸 -1
    copy_lst = deepcopy(lst)

    for a in range(0,2**N) :
        for b in range(0,2**N) :
            if lst[a][b] != 0 :
                cnt_lst = 0
                for na,nb in ((a+1,b),(a-1,b),(a,b+1),(a,b-1)) :
                    if 0<= na < 2**N and 0<= nb < 2**N :
                        if copy_lst[na][nb] != 0 :
                            cnt_lst += 1
                if cnt_lst < 3 :
                    lst[a][b] -= 1



# 출력
# 1. 남아있는 얼음 A[r][c]의 합
# 2. 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
# 첫째 줄에 남아있는 얼음 A[r][c]의 합을 출력하고, 둘째 줄에 가장 큰 덩어리가 차지하는
# 칸의 개수를 출력. 단, 덩어리가 없으면 0을 출력

retA = 0
retB = 1
for arr in lst :
    for a in arr :
        retA += a
print(retA)

visited = [[0]*(2**N) for _ in range(2**N)]

for i in range(2**N) :
    for j in range(2**N) :
        if lst[i][j] == 0 :
            visited[i][j] = 1

for i in range(2**N) :
    for j in range(2**N) :
        if visited[i][j] == 0 :
            q = deque()
            q.append((i,j))
            visited[i][j] = 1
            cnt = 1
            while q :
                x,y = q.popleft()

                for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)) :
                    if 0<= nx < 2**N and 0<= ny < 2**N :
                        if visited[nx][ny] == 0 :
                            visited[nx][ny] = 1
                            q.append((nx,ny))
                            cnt += 1

            if retB < cnt :
                retB = cnt


if retB == 1 :
    retB = 0
print(retB)
