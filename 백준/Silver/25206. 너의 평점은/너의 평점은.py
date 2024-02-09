N = 20
sumb = 0
aaa = 0
for _ in range(N) :
    a, b, c = input().split()
    b = float(b)
    if c != 'P' :
        sumb += b

    arr = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0,
           'D+' : 1.5, 'D0' : 1.0, 'F' : 0 }

    if c in arr :
        c = arr[c]
        aaa += b * c

ret = aaa / sumb
print(ret)