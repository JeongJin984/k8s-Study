import re

user_input = input()

N = int(user_input)

for i in range(N):
    user_input = input()
    sub = re.sub("[^aeiouAEIOU]", "", user_input)
    if sub == "":
        sub = "???"
    print(sub)
