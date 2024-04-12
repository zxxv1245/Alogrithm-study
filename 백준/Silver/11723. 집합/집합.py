import sys
input = sys.stdin.readline
N = int(input())
S = set()
for _ in range(N) :
    arr = input().strip().split()
    if arr[0] == 'add' : S.add(int(arr[1]))
    elif arr[0] == 'check' :
        if int(arr[1]) in S : print(1)
        else : print(0)
    elif arr[0] == 'remove' :
        if int(arr[1]) in S : S.remove(int(arr[1]))
    elif arr[0] == 'toggle' :
        if int(arr[1]) in S : S.remove(int(arr[1]))
        else : S.add(int(arr[1]))
    elif arr[0] == 'all': S = set(range(1, 21))
    elif arr[0] == 'empty' : S = set()