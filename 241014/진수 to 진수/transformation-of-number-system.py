a, b = map(int, input().split())
n = int(input())

# a진수인 n, 10진수 변환
def _10Digit(a, n):

    n_list = [ int(i) for i in list(str(n)) ]
    tendigit = 0
    temp = 0

    for n in n_list[::-1]:
        
        tendigit += n * (a ** temp)
        temp += 1

    return tendigit

# 10진수 -> b진수로 변환
def _bDigit(tendigit, b):

    bdigit_list = []

    while True:

        if tendigit < b:
            bdigit_list.append(tendigit)
            break
        
        bdigit_list.append(tendigit % b)
        tendigit //= b

    bdigit_list = bdigit_list[::-1]
    bdigit = int(''.join(map(str, bdigit_list)))

    return bdigit

tendigit = _10Digit(a, n)
print(_bDigit(tendigit, b))