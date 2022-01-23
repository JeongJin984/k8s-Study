# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import re

length = input()
#개행문자까지 고려해서 리스트 형태로 입력받음
user_input = [input() for _ in range(int(length))]

for string in user_input:
	word = re.findall('[aAeEiIoOuU]+',string)
	if word:
		print(''.join(word))
	else:
		print("???")