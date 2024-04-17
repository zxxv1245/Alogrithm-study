

K,N = map(int,input().split())
lst = []

for i in range(K) :
    w = int(input())
    lst.append(w)

start = 0
end = 2**31
ret = 0

while end>=start :
    mid = (start+end)//2
    cnt = 0
    for i in lst :
        cnt += i//mid
    if cnt >= N :
        ret = mid
        start = mid+1
    else :
        end = mid-1

print(ret)