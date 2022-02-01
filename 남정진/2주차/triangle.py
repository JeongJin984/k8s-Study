user_input = input().split(" ")
p1 = [int(user_input[0]), int(user_input[1])]

user_input = input().split(" ")
p2 = [int(user_input[0]), int(user_input[1])]

user_input = input().split(" ")
p3 = [int(user_input[0]), int(user_input[1])]

s1 = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]
s2 = p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1]

print("{:.2f}".format(round(abs(s1 - s2) / 2, 2)))
