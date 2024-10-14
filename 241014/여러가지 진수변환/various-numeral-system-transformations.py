N, B = map(int, input().split())

# 최소공배수법
def anystDigit(N, B):

    # n진수 변환
    n = N
    digit_list = []
    while True:

        if n < B:
            digit_list.append(n)
            break

        digit_list.append(n % B)
        n //= B

    return digit_list[::-1]

for i in anystDigit(N, B):
    print(i, end="")