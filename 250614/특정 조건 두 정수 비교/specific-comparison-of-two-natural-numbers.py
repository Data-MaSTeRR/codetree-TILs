a, b = map(int, input().split())
ar, br = 0, 0
if a < b:
    ar = 1
else:
    ar = 0

if a == b:
    br = 1
else:
    br = 0

print(ar, br)