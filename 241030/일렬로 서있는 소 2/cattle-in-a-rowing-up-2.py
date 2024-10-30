N = int(input())
a_list = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            
            # a_list[i] <= a_list[j] and a_list[j] <= a_list[k]
            if a_list[i] <= a_list[j] <= a_list[k]:
                cnt += 1

print(cnt)