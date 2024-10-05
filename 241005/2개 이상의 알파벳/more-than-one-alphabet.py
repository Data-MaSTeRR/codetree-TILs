s = input()

def len_sepStr(s):

    s = list(set(s))
    len_s = len(s)

    if len_s >= 2:
        return "Yes"
    
    else:
        return "No"


print(len_sepStr(s))