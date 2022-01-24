num = int(input())

input_list = []
print_list = []

num = int(input())

input_list = []
print_list = []

for count in range(num):
	input_list.append(input())
	string = ""
	for ch in input_list[count]:
		if ch.lower() == 'a' or ch.lower() == 'e' or ch.lower() == 'i' or ch.lower() == 'o' or ch.lower() == 'u':
			string += ch
	if len(string) == 0:
		print_list.append("???")
	else:
		print_list.append(string)
	print(print_list[count])