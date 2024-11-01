a = input()
a_list = list(a)


for idx in range(len(a)):
    if a_list[idx] == '0':
        a_list[idx] = '1'
        break

a = ''.join(a_list)
int_a = int(a)

_10int  = 0
for i in range(len(a)):

    _10int += int_a % 10 * (2 ** i)
    int_a //= 10

if a == '1':
    print(0)
else:
    print(_10int)