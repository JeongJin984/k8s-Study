N = int(input())

user_input = input().split(" ")
cur1 = [float(user_input[0]), float(user_input[1])]
user_input = input().split(" ")
cur2 = [float(user_input[0]), float(user_input[1])]

for i in range(N-2):
    user_input = input().split(" ")
    cur3 = [float(user_input[0]), float(user_input[1])]

    vec1 = [cur2[0] - cur1[0], cur2[1] - cur1[1]]
    vec2 = [cur3[0] - cur2[0], cur3[1] - cur2[1]]

    if (vec1[0] * vec2[1] - vec1[1] * vec2[0]) < 0:
        print("RIGHT")
    else:
        print("LEFT")

    cur1 = cur2
    cur2 = cur3


