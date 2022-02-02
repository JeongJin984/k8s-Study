# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def find(low, high, target):
    if low <= high:
        mid = int((low + high) / 2)

        if arr[mid] < target:
            return find(mid + 1, high, target)
        elif arr[mid] == target:
            return 1
        else:
            return find(low, mid-1, target)
    else:
        return 0


arr_len = int(input())
arr = []

user_input = input().split(" ")
for v in user_input:
    arr.append(int(v))

arr.sort()

answer_len = int(input())
answer = []

user_input = input().split()
for v in user_input:
    answer.append(int(v))

result = []
for v in answer:
    print(find(0, len(arr)-1, v))
