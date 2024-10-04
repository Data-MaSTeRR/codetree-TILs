a, b = map(int, input().split())

def _isPrime(n):
    for i in range(2, n):
        
        if n == 1:
            return False
        if n % i == 0:
            return True
    
    return False

cum_sum = 0
for n in range(a, b+1):
    if _isPrime(n) == False:
        if n != 1
            cum_sum += n

print(cum_sum)