N = int(input())
lst = list(map(int,input().split()))
lst.sort()
slst = set(lst)
print(*slst)