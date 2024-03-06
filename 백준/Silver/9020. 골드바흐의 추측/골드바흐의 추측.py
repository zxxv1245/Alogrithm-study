import sys
input = sys.stdin.readline

def is_prime_number(N) :
    arr = [1]*(N+1)
    arr[0] = 0
    arr[1] = 0

    for i in range(2,N+1) :
        if arr[i] == 1 :
            j = 2

            while i*j <= N :
                arr[i*j] = 0
                j += 1
    return arr
T = int(input())

for Test in range(1,T+1) :
    N = int(input())
    A = N//2
    B = N//2
    arr = is_prime_number(N)

    while True :
        if arr[A] and arr[B] :
            print(A,B)
            break
        A -= 1
        B += 1
