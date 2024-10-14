n = input()

def _10stDigit(n):

    n_list = [ int(i) for i in list(n) ]
    
    tendigit = 0
    temp = 0
    for n in n_list[::-1]:

        tendigit += n * (2 ** temp)
        temp += 1
    
    return tendigit

def _2ndDigit(n):

    twodigit_list = []
    while True:

        if n < 2:
            twodigit_list.append(n)
            break
        
        twodigit_list.append(n % 2)
        n //= 2

    twodigit_list = twodigit_list[::-1]
    twodigit = int(''.join(map(str, twodigit_list)))
        
    return twodigit

print(_2ndDigit(_10stDigit(n) * 17))