n = int(input())
n_list = list(map(int, input().split()))

def median(n_list):

    temp_list = []
    median_list = []
    cnt = 1
    for n in n_list:
        
        if cnt % 2 != 0:
            
            temp_list.append(n)
            sort_list = sorted(temp_list)

            idx = int(((cnt + 1) / 2) - 1)
            median_list.append(sort_list[idx])
            
            cnt += 1

        else:
            temp_list.append(n)
            cnt += 1
        
        sort_list = []
        

    return median_list
        

for n in median(n_list):
    print(n, end= " ")