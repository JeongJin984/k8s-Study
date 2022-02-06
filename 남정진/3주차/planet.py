user_input = input().split(" ")

planet_num = int(user_input[0])
info_num = int(user_input[1])

planet_small_map = {}
planet_big_map = {}

visited = [False] * (planet_num + 1)

result_small = [0] * (planet_num + 1)
result_big = [0] * (planet_num + 1)


def dfs_small(cur: int, target: int):
    visited[cur] = True

    for p in planet_small_map[cur]:
        if not visited[p]:
            result_small[target] += 1
            dfs_small(p, target)


def dfs_big(cur: int, target: int):
    visited[cur] = True

    for p in planet_big_map[cur]:
        if not visited[p]:
            result_big[target] += 1
            dfs_big(p, target)


for i in range(1, planet_num + 1):
    planet_small_map[i] = set()
    planet_big_map[i] = set()

for i in range(info_num):
    user_input = input().split(" ")
    p1 = int(user_input[0])
    p2 = int(user_input[1])
    planet_small_map[p1].add(p2)
    planet_big_map[p2].add(p1)

for i in range(1, planet_num + 1):
    visited = [False] * (planet_num + 1)
    dfs_small(i, i)
    visited = [False] * (planet_num + 1)
    dfs_big(i, i)

for i in range(1, planet_num + 1):
    print(result_big[i], result_small[i])
