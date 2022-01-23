# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math


length = int(input())
leaf_count = int(math.pow(2,int(length)-1))

user_input = []
for i in range(length):
	user_input.append(list(input()))

result = []

for i in range(0, leaf_count):
	result.append(0)
	for x in range(0, length):
		result[i] += ord(user_input[length-x-1][int(i/math.pow(2,x))])-64


#result.sort()

print(min(result))
print(max(result))
