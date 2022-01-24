user_input = input().split(" ")

length = int(user_input[0])
num = int(user_input[1])

user_input = input().split(" ")

int_list = [int(user_input[0])]
for i in range(1, length):
    int_list.append(int(user_input[i]) + int_list[i-1])

int_sum = 0
for i in range(num):
    user_input = input().split(" ")
    start = int(user_input[0])
    end = int(user_input[1])

    if start == 1:
        int_sum = int_list[end-1]
    else:
        int_sum = int_list[end-1] - int_list[start-2]

    if int_sum > 0:
        print("+" + str(int_sum))
    else:
        print(int_sum)



