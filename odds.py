banknotes = [10 , 20, 50, 100 ,200, 500, 1000]
llen = len(banknotes)

number = (int(input('Введите сумму которую хотите снять :')))
limit = 10

for i, note in enumerate(banknotes):
	amount = limit

	if number // note < limit:
		amount = note // amount

	res = number - note * amount

	if i < llen - 1:
		while res % banknotes[i+1]:
			res -= note
			amount -= 1
	number -= note * amount
	print(str(note) + " by " + str(amount))
	if number <= 0:
		break
