a, b = map(int, input().split())


if a == b:
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            a = i
            break
    print(a)
else:
    print(2)