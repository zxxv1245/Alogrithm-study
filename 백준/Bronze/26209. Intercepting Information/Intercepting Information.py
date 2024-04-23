lst = list(map(int,input().split()))
flag =0
for i in lst :
    if i not in [0,1] :
        flag = 1

if flag == 1 :
    print('F')
else :
    print('S')