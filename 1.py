#calculator V1

from colorama import init
from colorama import Fore, Back, Style

init()

print ( Fore.BLACK )

print ( Back.GREEN )

what = input( "Что будем делать? (+, - or * ,/ ): ")

print ( Back.CYAN )

a = float( input("Введите первое число: "))
b = float( input("Ведите второе число: "))

print ( Back.RED )

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
	print("Выбранна неправильная операцыя")

input()