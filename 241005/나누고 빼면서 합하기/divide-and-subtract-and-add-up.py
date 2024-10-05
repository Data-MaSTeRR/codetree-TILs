n, m = map(int, input().split())
sequence = list(map(int, input().split()))


def idx_list(m):
    
    idx_list = [m]
    while m > 1:
        
        if m % 2 == 0:
            m = int(m / 2)
            idx_list.append(m)
            
        else:
            m -= 1
            idx_list.append(m)

    return idx_list

idx_list = idx_list(m)


sum_sequence = 0
for idx in idx_list:
    sum_sequence += sequence[idx-1]

print(sum_sequence)