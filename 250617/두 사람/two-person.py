age1, sex1 = input().split()
age2, sex2 = input().split()
age1, age2 = int(age1), int(age2)

if (age1 >= 19 and sex1 == 'M') or (age2 >= 19 and sex2 == 'M'):
    print(1)
else:
    print(0)