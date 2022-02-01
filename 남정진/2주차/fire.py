di = [0, 0, 1, -1]
dj = [-1, 1, 0, 0]

user_input = input().split(" ")

R = int(user_input[0])
C = int(user_input[1])

start_point = []

fire_map = []
depth_map = []
for i in range(R):
    user_input = input()
    temp = []
    depth_temp = []
    for j in range(C):
        temp.append(user_input[j])
        depth_temp.append(0)
        if user_input[j] == '&':
            start_point = [i, j]
    fire_map.append(temp)
    depth_map.append(depth_temp)

queue = [start_point]
depth_map[start_point[0]][start_point[1]] = 1

while len(queue) > 0:
    cur_point = queue.pop(0)

    for i in range(4):
        next_point = [cur_point[0] + di[i], cur_point[1] + dj[i]]
        if 0 <= next_point[0] < R and 0 <= next_point[1] < C:
            if fire_map[next_point[0]][next_point[1]] == '.' and depth_map[next_point[0]][next_point[1]] == 0:
                queue.append(next_point)
                depth_map[next_point[0]][next_point[1]] = depth_map[cur_point[0]][cur_point[1]] + 1

            elif fire_map[next_point[0]][next_point[1]] == '@':
                print(depth_map[cur_point[0]][cur_point[1]] - 1)
                exit()

print(-1)
