check = [1,1,2,2,2,8]

A = list(map(int, input().split()))
new_list = []

for i in range(0,6) :
        if A[i] != check[i] :
            c = check[i] - A[i]
            new_list.append(c)
        else :
            new_list.append(0)

print(*new_list)
