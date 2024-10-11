n = int(input())
n_list = list(map(int, input().split()))

n_list.sort()
for i in n_list:
    print(i, end= " ")

n_list.sort(reverse=True)
print()

for j in n_list:
    print(j, end= " ")