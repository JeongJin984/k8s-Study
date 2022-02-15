N = int(input())

answer = 0

cur = 5
i = 1
while cur <= N:
    answer += int(N / cur)
    cur *= 5

print(answer)
