import math

user_input = input()

input_string = user_input.split(" ")

a = int(input_string[0])
b = int(input_string[1])

if a != b:
    print(2)
else:
    total = 0
    flag = True
    for i in range(2, int(math.sqrt(a) + 1)):
        if a % i == 0:
            flag = False
            print(i)
            break
    if flag:
        print(a)

