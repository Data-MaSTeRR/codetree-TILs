n = int(input())
a_list = list(map(int, input().split()))

move_list = []
for i in range(n):
    total_move = 0
    for j in range(n):
        total_move += abs(i - j) * a_list[j]
    
    move_list.append(total_move)

print(min(move_list))