n = int(input())
n_list = list(map(int, input().split()))

def median(n_list):

    temp_list = []
    median_list = []
    cnt = 1
    for n in n_list:
        
        idx = 0
        if cnt % 2 != 0:
            
            idx = ((cnt + 1) / 2) - 1
            print(idx)

            median_list.append(n_list[cnt])
            temp_list.append(n)
            cnt += 1

        temp_list.append(n)
    
    return median_list
        

for n in median(n_list):
    print(n, end= " ")