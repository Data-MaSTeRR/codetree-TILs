a, b = map(int, input().split())

def _isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return True
    
    return False

cum_sum = 0
for n in range(a, b+1):
    if _isPrime(n) == False:
        cum_sum += n
        
if a == 1 and b == 1:
    print(0)
else: 
    print(cum_sum)