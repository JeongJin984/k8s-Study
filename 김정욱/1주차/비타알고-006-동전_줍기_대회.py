# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
length = int(input())
coin_list = list(map(int, input().split()))

MAX=0

for i in range(0, length):
	SUM=0
	
	for j in range(i,length):
		SUM += int(coin_list[j])
		
		if MAX <= SUM:
			MAX = SUM
			

print(MAX)