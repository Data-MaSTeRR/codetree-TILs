N = int(input())
n_list = list(map(int, input().split()))

def checkEven_newList(n_list):

    new_list = []
    for n in n_list:
        if n % 2 == 0:
            n /= 2
            n = int(n)
            new_list.append(n)
        else:
            new_list.append(n)

    return new_list

new_list = checkEven_newList(n_list)
for i in new_list:
    print(i, end= " ")