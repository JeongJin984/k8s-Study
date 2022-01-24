def string_to_date(start: str):
    start_split = start.split("/")
    if len(start_split[1]) == 1:
        return int(start_split[0] + "0" + start_split[1])
    else:
        return int(start_split[0] + start_split[1])


input_string = input()
work_schedule = []

for i in range(1, int(input_string)+1):
    start_end = input().split(" ")
    work_schedule.append([string_to_date(start_end[0]), string_to_date(start_end[1])])

work_schedule.sort(key=lambda x: (x[0], -x[1]))

work_order = []

for i in range(1, len(work_schedule) + 1):
    work_order.append([work_schedule[i-1][0], i])
    work_order.append([work_schedule[i-1][1], -i])

work_order.sort(key=lambda x:(x[0], x[1]))

stack = []

for w in work_order:
    if w[1] > 0:
        stack.append(w)
    else:
        peek = stack.pop()
        if abs(peek[1]) != abs(w[1]):
            print("No")
            exit()

print("Yes")
