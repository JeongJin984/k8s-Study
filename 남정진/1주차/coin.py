length = int(input())

input_list = input().split(" ")

int_list = []

for v in input_list:
    int_list.append(int(v))

int_max = 0
for i in range(1, length):
    temp = int_list[i] + int_list[i-1]
    if temp > int_list[i]:
        int_list[i] = temp
    int_max = max(temp, int_max)

print(int_max)
