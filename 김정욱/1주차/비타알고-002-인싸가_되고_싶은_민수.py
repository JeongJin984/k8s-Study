# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import math

user_input = input().split()
#a, b는 입력받은 인자, c는 a의 루트의 정수값(소숫점은 버림)
a = int(user_input[0])
b = int(user_input[1])
c = int(math.sqrt(a))

#a와 b가 다르면 결과가 2가 될 수 밖에 없으므로 a==b인 경우만 체크
if ((a-b) == 0):
	#a의 루트에서 소숫점을 버린 정수값 까지만 체크
	for i in range(2, c+1):
		if (a % i == 0):
			print (i)
			exit(0)
		elif (i == c):
			print (a)
			exit(0)
else:
	#print ("a != b")
	print (2)