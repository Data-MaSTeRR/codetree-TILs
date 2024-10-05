n1, n2 = map(int, input().split())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

def is_subsequence(A_list, B_list):
    len_A, len_B = len(A_list), len(B_list)

    for i in range(len_A - len_B + 1):
        if A_list[i : i + len_B] == B_list:
            return "Yes"
    
    return "No"

print(is_subsequence(A_list, B_list))