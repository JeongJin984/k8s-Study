import re

user_input = input().split(" ")

N = int(user_input[0])
M = int(user_input[1])

target = input()

regex = "(A)" + "{" + str(M) + ",}"

for i in range(ord('B'), ord('Z')+1):
    regex += "|" + "(" + chr(i) + ")" + "{" + str(M) + ",}"

sub_target = re.sub(regex, "", target, 1)
while sub_target != target:
    target = sub_target
    sub_target = re.sub(regex, "", sub_target, 1)

if len(target) == 0:
    print("CLEAR!")
else:
    print(target)
