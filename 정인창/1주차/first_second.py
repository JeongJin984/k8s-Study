import re

numbers = input()
rule = re.compile('.*21.*12.*|.*12.*21.*')
matched = rule.match(numbers)

if matched is None:
	print("No")
else:
	print("Yes")