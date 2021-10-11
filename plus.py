def plus(num1, num2 = 100, *nums, **strings):
	res = num1 + num2
	i = 0

	for number in nums:
		res += number

	for key, val in strings.items():
		print(key + " => " + val)
	return res

print(plus(100))
print(plus(100, 20))

print(plus(100, 10, 20, 30))

print(plus(1, 2, 3, 4, 5, 6, 7, name = "Vasya", surname = "Petechkin"))
