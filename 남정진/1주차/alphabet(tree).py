tree_height = int(input())
data_list = []

for i in range(0, tree_height):
    data_string = input()
    temp = []
    for c in data_string:
        temp.append(ord(c) - ord('A') + 1)
    data_list.append(temp)


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def inorder(node, cur_sum):
    if node:
        inorder(node.left, cur_sum + node.data)
        inorder(node.right, cur_sum + node.data)
    else:
        inorder.max = max(cur_sum, inorder.max)
        inorder.min = min(cur_sum, inorder.min)


def init(cur_node, cur_height, index):
    if cur_height < tree_height - 1:
        cur_node.left = Node(data_list[cur_height + 1][index * 2])
        cur_node.right = Node(data_list[cur_height + 1][index * 2 + 1])
        init(cur_node.left, cur_height + 1, 2 * index)
        init(cur_node.right, cur_height + 1, 2 * index + 1)


root = data_list[0][0]
tree_map = Node(root)

init(tree_map, 0, 0)
inorder.max = 0
inorder.min = 9999999999
inorder(tree_map, 0)

print(inorder.min)
print(inorder.max)
