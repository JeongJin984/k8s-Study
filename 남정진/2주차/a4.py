user_input = input().split(" ")

N = int(user_input[0])
M = int(user_input[1])

n1 = int(N / 40)
n2 = int(N / 20)
m1 = int(M / 40)
m2 = int(M / 20)

print(n1 * m2 + n2 * m1 - 2 * (n1 * m1))

