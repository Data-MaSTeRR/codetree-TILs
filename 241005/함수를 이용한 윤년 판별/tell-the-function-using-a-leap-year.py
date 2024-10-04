y = int(input())

def yoon_year(y):

    if y % 100 == 0:
        if y % 400 !=0:
            return "false"
    
    if y % 4 == 0:
        return "true"
    
    return "false"

print(yoon_year(y))