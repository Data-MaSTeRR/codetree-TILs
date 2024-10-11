n = int(input())
n_list = list(map(int, input().split()))

def median(n_list):

    temp_list = []
    median_list = []
    cnt = 1
    for n in n_list:
        
        if n % 2 != 0:
            
            temp_list.append(n)

            idx = int(((cnt + 1) / 2)) - 1
            median_list.append(temp_list[idx])
            
            cnt += 1

        else:
            temp_list.append(n)
            cnt += 1
        

    return median_list
        

for n in median(n_list):
    print(n, end= " ")