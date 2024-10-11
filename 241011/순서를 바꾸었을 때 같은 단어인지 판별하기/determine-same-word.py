s1 = input()
s2 = input()

def sameCheck(s1, s2):

    s1 = sorted(s1)
    s2 = sorted(s2)
    
    if len(s1) != len(s2):
        return "No"
    
    if s1 != s2:
        return "No"

    return "Yes"

print(sameCheck(s1, s2))