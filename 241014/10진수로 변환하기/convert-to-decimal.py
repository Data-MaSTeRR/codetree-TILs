n = input()

def _10stDigit(n):

    n_list = list(n)
    n_list = [ int(i) for i in n_list ]

    num = 0
    temp = 0

    for n in n_list[::-1]:
        
        num += n * (2 ** temp)
        temp += 1
    
    return num

print(_10stDigit(n))