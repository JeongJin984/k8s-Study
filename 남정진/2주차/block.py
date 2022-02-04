max_block = int(input())

stack1_top = 0
stack2_top = 0

stack1 = [0]
answer = 0
for i in range(max_block * 2):
    user_input = input().split(" ")
    command = user_input[0]
    if command == "add":
        stack1_top = int(user_input[1])
        stack1.append(stack1_top)
    else:                                   # target number MUST contain in stack1
        if stack1_top == stack2_top + 1:
            if len(stack1) == 0:
                stack2_top += 1
                stack1_top = stack2_top + 1
            else:
                stack2_top = stack1.pop()
                if len(stack1) == 0:
                    stack1_top = stack2_top + 1
                else:
                    stack1_top = stack1[-1]
        else:
            stack1 = []
            answer += 1
            stack2_top += 1
            stack1_top = stack2_top + 1

print(answer)
