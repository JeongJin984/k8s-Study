user_input = input().split(" ")

n = int(user_input[0])
max_use = int(user_input[1])

tissue_length = []
max_length = 0

user_input = input().split(" ")
for i in range(n):
    tissue_length.append(int(user_input[i]))
    if max_length < int(user_input[i]):
        max_length = int(user_input[i])

to_use = 0
for i in range(n):
    to_use += max_length - tissue_length[i]

if max_use < to_use:
    print("No way!")
else:
    print(max_length + int((max_use - to_use) / n))

