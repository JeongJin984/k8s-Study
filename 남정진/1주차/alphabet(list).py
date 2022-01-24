import math

tree_height = int(input())
data_list = []

for i in range(0, tree_height):
    data_string = input()
    temp = []
    for c in data_string:
        temp.append(ord(c) - ord('A') + 1)
    data_list.append(temp)

for h in range(0, tree_height - 1):
    for i in range(0, int(math.pow(2, h))):
        data_list[h+1][i * 2] += data_list[h][i]
        data_list[h + 1][i * 2 + 1] += data_list[h][i]

tree_max = 0
tree_min = 999999999
for v in data_list[tree_height-1]:
    tree_max = max(tree_max, v)
    tree_min = min(tree_min, v)

print(tree_min)
print(tree_max)
