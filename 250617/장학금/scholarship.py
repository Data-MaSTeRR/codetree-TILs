mid, fin = map(int, input().split())
if mid >= 90:
    if 95 <= fin <= 100:
        print(100000)
    elif fin >= 90:
        print(50000)
else:
    print(0)