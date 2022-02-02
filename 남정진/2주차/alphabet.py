tri_height = int(input())

tri_map = []

for i in range(tri_height):
    user_input = input()
    temp = []
    for c in user_input:
        temp.append(ord(c) - ord('A') + 1)
    tri_map.append(temp)


result_map = [tri_map[0]]
for h in range(tri_height-1):
    temp = []
    first_value = result_map[h][0] + tri_map[h+1][0]
    last_value = result_map[h][-1] + tri_map[h+1][-1]

    for i in range(1, len(tri_map[h])):
        temp.append(max(result_map[h][i], result_map[h][i-1]) + tri_map[h+1][i])

    result_map.append(temp)
    temp.insert(0, first_value)
    temp.append(last_value)

answer = 0
for v in result_map[-1]:
    answer = max(answer, v)

print(answer)
