N = int(input())

lst = [int(input()) for _ in range(N)]


st = []

arr = []
for i in range(1,N+1) :

    st.append(i)
    arr.append(1)
    while st and st[-1] == lst[0] :
        st.pop()
        lst.pop(0)
        arr.append(0)

if bool(st) == True :
    print('NO')
else :
    for i in arr :
        if i == 1 :
            print('+')
        else :
            print('-')