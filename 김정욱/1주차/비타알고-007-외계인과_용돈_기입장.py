# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


lifetime = list(map(int,input().split()))
money = list(map(int, input().split()))
range_list = [list(map(int, input().split())) for _ in range(lifetime[1])]

#lifetime[1]에 저장해둔 기간범위의 갯수 만큼 반복하여 범위의 값을 더한 뒤 출력
for index in range(0, lifetime[1]):

	#sum 함수를 이용하여 money 리스트에서 원하는 기간의 범위만큼을 합하여 변수 SUM에 저장
	SUM = sum(money[range_list[index][0]-1:range_list[index][1]])
	if int(SUM) > 0:
		print("+"+str(SUM))
	else:
		print(SUM)