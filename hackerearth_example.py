a, b = input().split(" ")
a = int(a)
b = int(b)
count = 0
if a >= b:
    for i in range(1,a):
        if a%i == 0 and b%i == 0:
            count += 1
else:
    for i in range(1,b):
        if  a % i == 0 and b % i == 0:
            count += 1

print(count)