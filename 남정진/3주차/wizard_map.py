user_input = input().split(" ")

N = int(user_input[0])
M = int(user_input[1])
mana = int(user_input[2])

visited = []

for k in range(int(mana / 10)+1):
    temp1 = []
    for i in range(N):
        temp2 = []
        for j in range(M):
            temp2.append(False)
        temp1.append(temp2)
    visited.append(temp1)

test_map = []
for i in range(N):
    test_map.append([])
    visited.append([])
    user_input = input()
    for j in range(M):
        test_map[i].append(int(user_input[j]))

queue_list = [[0, 0]]

dp = [[0, 1], [0, -1], [1, 0], [-1, 0]]

state_queue = [[0, 0, int(mana / 10), 0]]
visited[int(mana / 10)][0][0] = True
while len(state_queue) > 0:
    cur_state = state_queue.pop()

    if cur_state[0] == N - 1 and cur_state[1] == M - 1:
        print(cur_state[3])
        exit()

    for i in range(4):
        next_state = [
            cur_state[0] + dp[i][0],
            cur_state[1] + dp[i][1],
            cur_state[2],
            cur_state[3] + 1
        ]

        if 0 <= next_state[0] < N and 0 <= next_state[1] < M:
            if not visited[next_state[2]][next_state[0]][next_state[1]]:
                if test_map[next_state[0]][next_state[1]] == 1 and next_state[2] > 0:
                    next_state = [
                        2 * next_state[0] - cur_state[0],
                        2 * next_state[1] - cur_state[1],
                        next_state[2] - 1,
                        next_state[3]
                    ]
                    if not(0 <= next_state[0] < N and 0 <= next_state[1] < M) \
                            or test_map[next_state[0]][next_state[1]] == 1:
                        continue
                    visited[next_state[2]][next_state[0]][next_state[1]] = True
                    state_queue.insert(0, next_state)
                elif test_map[next_state[0]][next_state[1]] == 0:
                    visited[next_state[2]][next_state[0]][next_state[1]] = True
                    state_queue.insert(0, next_state)

print(-1)
