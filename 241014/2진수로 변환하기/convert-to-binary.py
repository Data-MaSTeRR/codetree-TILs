n = int(input())

def _2ndDigit(n):

    num = n
    digit_list = []

    while True:

        if num < 2:
            digit_list.append(num)
            break
        
        digit_list.append(num % 2)
        num //= 2
    
    return digit_list

for i in _2ndDigit(n)[::-1]:
    print(i, end="")