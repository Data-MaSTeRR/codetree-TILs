y = int(input())

def yoon_year(y):

    if y % 4 == 0:
        return "true"

    if y % 100 == 0:
        if y % 400 !=0:
            return "false"
    
    return "false"

print(yoon_year(y))