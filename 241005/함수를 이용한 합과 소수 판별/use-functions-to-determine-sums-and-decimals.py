a, b = map(int, input().split())

# True는 소수
def check_prime(n):

    if n == 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def check_sumEven(n):

    cum_sum = 0
    while n:
        cum_sum += (n % 10)
        n //= 10

    if cum_sum % 2 == 0:
        return True
    
    return False

cnt = 0
for n in range(a, b+1):
    
    if check_prime(n) == True and check_sumEven(n) == True:
        cnt += 1

print(cnt)