stack1 = []
stack2 = []

stack2_len = int(input())

answer = 0
for i in range(2 * stack2_len):
    user_input = input().split(" ")
    command = user_input[0]

    if command == "add":
        num = int(user_input[1])
        stack1.append(num)
    else:
        if len(stack2) == 0:
            if stack1[-1] == 1:
                stack2.append(stack1.pop())
            else:
                stack1.sort(reverse=True)
                answer += 1
                stack2.append(stack1.pop())
        elif stack2[-1] + 1 == stack1[-1]:
            stack2.append(stack1.pop())
        else:
            stack1.sort(reverse=True)
            answer += 1
            stack2.append(stack1.pop())

print(answer)
