N = int(input())
s = input()

cnt = 0
for c in range(N-2):
    for o in range(c+1, N-1):
        for w in range(o+1, N):
            if s[c] == 'C' and s[o] == 'O' and s[w] == 'W':
                cnt += 1
            
print(cnt)