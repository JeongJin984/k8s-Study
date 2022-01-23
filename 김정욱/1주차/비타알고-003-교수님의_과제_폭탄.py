# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


length = input()
user_input = []
temp = []
working = [0, 0]
#user_input = sorted([input().split() for _ in range(int(length))])
for i in range(int(length)):
	temp = input().replace('/',' ').split()
	user_input.append([int(temp[0])*100+int(temp[1]), int(temp[2])*100+int(temp[3])])

#lambda 함수를 이용하여 x[0](과제시작값)의 내림차순, x[0](과제시작값)이 같은것 끼리는 x[1](과제종료값)의 오름차순 정렬
user_input = sorted(user_input, key=lambda x : (-x[0], x[1]))

for index, homework in enumerate(user_input):
	#user_input[index]와 user_input[index+1]을 비교하므로 리스트의 크기를 벗어나지 않는 범위에서만 체크
	if index < int(length)-1:
		#현재 잡고있는 과제의 종료일이 이전 과제의 종료일보다 크면 과제실패의 가능성이 있음!!
		if homework[1] > user_input[index+1][1]:
			#print (str(homework[1])+" vs "+str(user_input[index+1][1]))
			##############현재 잡고있는 과제의 시작값이 이전 과제의 종료값과 같거나 작으면 과제실패
			#현재 잡고있는 과제의 시작값이 이전 과제의 종료값보다 작으면 과제실패
			if homework[0] < user_input[index+1][1]:
				print ("No")
				exit()
		
print ("Yes")