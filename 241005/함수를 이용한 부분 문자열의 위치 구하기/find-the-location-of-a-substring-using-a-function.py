input_s = input()
target_s = input()

def exist_str(input_s, target_s):

    for s in range(len(input_s) - len(target_s) + 1):
        if input_s[s: s + len(target_s)] == target_s:
            return s
        
    return -1

print(exist_str(input_s, target_s))