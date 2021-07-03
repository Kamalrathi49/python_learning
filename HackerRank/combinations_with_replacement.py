from itertools import combinations_with_replacement

a = input()
a = a.split(" ")
s, n = a[0], int(a[1])

flst = sorted(list(combinations_with_replacement(s, n)))

lst = []

for i in flst:
    lst.append(i)

for i in lst:
    li = (i)
    strng = ''.join(li)
    print(strng)
