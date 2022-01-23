# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()

p12 = user_input.find('12')
p21 = user_input.find('21')

#12 또는 21을 못찾은 경우
if p12 == -1 or p21 == -1:
	print ("No")
	exit()
#12가 먼저 나온 경우 뒤에서부터 21의 위치를 다시 찾음
elif p12 < p21:
	if (user_input.rfind('21') - p12) > 1:
		print ("Yes")
	else:
		print ("No")
#21이 먼저 나온 경우 뒤에서부터 12의 위치를 다시 찾음
elif p21 < p12:
	if (user_input.rfind('12') - p21) > 1:
		print ("Yes")
	else:
		print ("No")