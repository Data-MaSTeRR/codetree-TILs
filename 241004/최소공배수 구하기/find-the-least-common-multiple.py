def baesu(num, length):

    l = []
    mul_num = num
    
    for cnt in range(1, length + 1):
        
        mul_num = num * cnt
        l.append(mul_num)

    return l


def min_baesu(n_list, m_list):

    min_value = 1
    flag = False
    for n in n_list:
        for m in m_list:
            if n == m:
                min_value = m
                flag = True
                break
        
        if flag:
            break

    print(min_value)

    return min_value




n, m = map(int, input().split())
n_list = baesu(n, m)
m_list = baesu(m, n)

min_baesu(n_list, m_list)