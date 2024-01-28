N = int(input())
a = ' '
b = '*'
for i in range(1,2*N) :
    if i < N :
        print((N-i)*a + (2*i-1)*b) 
    elif i == N :
        print((2*N-1)*b)
    elif i > N :
        print((i-N)*a + (((2*N-1)-2*(i-N)))*b)