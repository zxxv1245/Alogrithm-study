
def abc(ret) :
    global A
    global B
    global cnt


    if ret and A <= int(ret) <= B:
        cnt += 1

    if ret and int(ret) >= B :
        return

    for i in range(2) :
        abc(ret+lst[i])


A, B = map(int,input().split())

lst = ['4','7']
ret = ''
cnt = 0
abc(ret)
print(cnt)
