# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


lifetime = list(map(int,input().split()))
money = list(map(int, input().split()))
range_list = [list(map(int, input().split())) for _ in range(lifetime[1])]
SUM_list = []

#money 리스트의 첫번째 인자로 시작하는 합의 리스트를 저장 (money[0:n])
for i in range(0, lifetime[0]):
	SUM_list.append(0)
	if i == 0:
		SUM_list[i] += money[i]
	else:
		SUM_list[i] += SUM_list[i-1] + money[i]

#print(SUM_list)

#lifetime[1]에 저장해둔 기간범위의 갯수 만큼 반복하여 범위의 값의 합산을 출력
for index in range(0, lifetime[1]):

	#sum 함수를 이용하여 money 리스트에서 원하는 기간의 범위만큼을 합하여 변수 SUM에 저장
	#SUM = sum(money[range_list[index][0]-1:range_list[index][1]])
	
	#부분합을 이용하여 range_list[index]에 저장된 기간 내의 돈의 합을 계산하여 출력
	if range_list[index][0] == 1:
		SUM = SUM_list[range_list[index][1]-1]
	else:
		SUM = SUM_list[range_list[index][1]-1] - SUM_list[range_list[index][0]-2]
	
	if int(SUM) > 0:
		print("+"+str(SUM))
	else:
		print(SUM)
