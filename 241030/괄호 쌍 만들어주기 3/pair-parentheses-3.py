s = input()

cnt = 0
for i in range(len(s)):
    for j in range(i+1, len(s)):
        
        if s[i] == ')':
            break
        
        if s[j] == ')':
            cnt += 1

print(cnt)