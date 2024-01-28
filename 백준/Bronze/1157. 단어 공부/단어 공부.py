T = input().upper()

set_T = set()

for a in T :
    set_T.add(a)

list_T = list(set_T)
count_T = []
for b in list_T :
    count_T.append(T.count(b))

max_count_T = max(count_T)
max_count_count_T = count_T.count(max_count_T)
if max_count_count_T >= 2 :
    print('?')

else :
    max_count_T_index = count_T.index(max_count_T)
    print(list_T[max_count_T_index])