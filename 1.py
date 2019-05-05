#calculator V1


what = input( "Що будемо робити? (+, - чи * ,/ ): ")

a = float( input("Введіть перше число: "))
b = float( input("Введіть друге число: "))

if what == "+":
	c = a + b
	print ("Результат: " + str(c))
elif what == "-":
	c = a - b
	print ("Результат: " + str(c))
elif what == "*":
	c = a * b
	print ("Результат: " + str(c))
elif what == "/":
	c = a / b
	print ("Результат: " + str(c))

else:
	print("Вибрана не вірна операція")

input()
