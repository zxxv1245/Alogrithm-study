N = int(input())
cnt = 0


for i in range(N) :
    word = input()
    check = []

    ret = 1
    for a in word :
        if a not in check :
            check.append(a)
        elif a != check[-1] and a in check :
            ret = 0

    if ret == 1 :
        cnt += 1

print(cnt)
