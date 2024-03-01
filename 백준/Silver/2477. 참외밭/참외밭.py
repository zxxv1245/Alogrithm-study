N = int(input())
maxW = -21e8
maxH = -21e8
lst = []
for _ in range(6) :
    M, length = map(int,input().split())
    lst.append((M,length))
    if M == 1 or M == 2 :
        if maxW < length :
            maxW = length
            maxx = M
    else :
        if maxH < length :
            maxH = length
            maxy = M



if (maxx == 2 and maxy == 4)  or (maxx == 1 and maxy == 3) :
    for i in range(6) :
        if lst[i][0] == 1 or lst[i][0] == 2 :
            if lst[i][1] == maxW :
                if i + 1 < 6 :
                    orderH = lst[i+1][1]
                elif i + 1 >= 6 :
                    orderH = lst[0][1]

        elif lst[i][0] == 3 or lst[i][0] == 4 :
            if lst[i][1] == maxH :
                orderW = lst[i - 1][1]
elif (maxx == 1 and maxy == 4)  or (maxx == 2 and maxy == 3) :
    for i in range(6):
        if lst[i][0] == 3 or lst[i][0] == 4:
            if lst[i][1] == maxH:
                if i + 1 < 6:
                    orderW = lst[i + 1][1]
                elif i + 1 >= 6:
                    orderW = lst[0][1]

        elif lst[i][0] == 1 or lst[i][0] == 2:
            if lst[i][1] == maxW:
                orderH = lst[i - 1][1]

area = (maxW*maxH) - (maxW-orderW)*(maxH-orderH)

ret = N * area

print(ret)