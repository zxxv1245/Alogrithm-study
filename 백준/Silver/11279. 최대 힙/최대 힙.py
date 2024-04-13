from heapq import heappop,heappush
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N) :
    a = int(input())
    if a == 0 :
        if heap :
            print(-heappop(heap))
        else :
            print(0)
    else :
        heappush(heap,-a)