def square(n):
    i = 1
    for _ in range(n):
        for _ in range(n):
            print(i, end= " ")
            i += 1
            if i == 10:
                i = 1
        print()

n = int(input())
square(n)