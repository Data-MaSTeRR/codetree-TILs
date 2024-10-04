def yaksu(number):
    
    l = []
    for i in range(1, number+1):
        if number % i == 0:
            l.append(i)

    return l
    

def max_yaksu(n_list, m_list):

    reverse_n_list = sorted(n_list, reverse= True)
    reverse_m_list = sorted(m_list, reverse= True)

    flag = False
    for i in reverse_n_list:
        for j in reverse_m_list:
            if i == j:
                max_yaksu = j
                flag = True
                break
        
        if flag:
            return print(max_yaksu)
            break
        
            

n, m = map(int, input().split())
n_list = yaksu(n)
m_list = yaksu(m)

max_yaksu(n_list, m_list)