N = 9

lst = [list(map(int, input().split()))for _ in range(N)]
x = y = maxV = 0
for i in range(N) :
    for j in range(N) :
        if maxV <= lst[i][j] :
            maxV = lst[i][j]
            x = i + 1
            y = j + 1

print(maxV)
print(x, y)