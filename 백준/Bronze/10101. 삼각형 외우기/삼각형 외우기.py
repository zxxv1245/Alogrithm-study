a,b,c = map(int,open(0))
if a == 60 and b == 60 and c == 60 :
    print('Equilateral')
elif a+b+c == 180 :
    if a == b or b == c or c == a :
        print('Isosceles')
    elif a!=b and b != c and c !=a :
        print('Scalene')
else :
    print('Error')