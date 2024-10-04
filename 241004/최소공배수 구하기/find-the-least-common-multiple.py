def baesu(num):

    l = []
    cnt = 1
    mul_num = num
    while (mul_num <= 100):
        
        l.append(mul_num)
        cnt += 1
        mul_num = num * cnt

    return l


def min_baesu(n_list, m_list):

    min_value = 0
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
n_list = baesu(n)
m_list = baesu(m)

min_baesu(n_list, m_list)