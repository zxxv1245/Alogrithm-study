while True :
    N = int(input())
    if N == 0 :
        break
    ret = 0
    for i in range(N,0,-1) :
        ret += i

    print(ret)