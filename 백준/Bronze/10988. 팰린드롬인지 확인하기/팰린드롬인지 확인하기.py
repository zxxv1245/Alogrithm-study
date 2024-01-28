T = input()
mm = len(T)//2
if len(T) % 2 == 0 :
    if T[:mm] == T[mm:][::-1]:
        print(1)
    else :
        print(0)
elif len(T) % 2 == 1 :
    if T[:mm] == T[mm+1:][::-1]:
        print(1)
    else:
        print(0)

