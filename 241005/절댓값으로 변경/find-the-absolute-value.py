N = int(input())
n_list = list(map(int, input().split()))

def absolute(n):

    if n >= 0:
        return n
    else:
        return -n

abs_list = []
for n in n_list:
    abs_list.append(absolute(n))

for n in abs_list:
    print(n, end= " ")