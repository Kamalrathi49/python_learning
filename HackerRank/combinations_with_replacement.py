a = list(map(int, input().split()))

li = []

for _ in range(a[0]):
    inpt = max(list(map(int, input().split())))
    li.append(inpt ** 2)

print(sum(li) % a[1])