def even_five(n):

    s = 0
    s += n // 10
    s += n % 10

    if n % 2 == 0 and s % 5 == 0:
        return "Yes"
    
    else:
        return "No"

n = int(input())
print(even_five(n))