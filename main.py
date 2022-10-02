import numpy as np
import os

def win_check (arr):
	if (arr[0, 0] == 'X' and arr[0, 1] == 'X' and arr[0, 2] == 'X'):
		return 1
	if (arr[1, 0] == 'X' and arr[1, 1] == 'X' and arr[1, 2] == 'X'):
		return 1
	if (arr[2, 0] == 'X' and arr[2, 1] == 'X' and arr[2, 2] == 'X'):
		return 1
	if (arr[0, 0] == 'X' and arr[1, 0] == 'X' and arr[2, 0] == 'X'):
		return 1
	if (arr[0, 1] == 'X' and arr[1, 1] == 'X' and arr[2, 1] == 'X'):
		return 1
	if (arr[0, 2] == 'X' and arr[1, 2] == 'X' and arr[2, 2] == 'X'):
		return 1
	if (arr[0, 0] == 'X' and arr[1, 1] == 'X' and arr[2, 2] == 'X'):
		return 1
	if (arr[0, 2] == 'X' and arr[1, 1] == 'X' and arr[2, 0] == 'X'):
		return 1
	if (arr[0, 0] == 'O' and arr[0, 1] == 'O' and arr[0, 2] == 'O'):
		return 2
	if (arr[1, 0] == 'O' and arr[1, 1] == 'O' and arr[1, 2] == 'O'):
		return 2
	if (arr[2, 0] == 'O' and arr[2, 1] == 'O' and arr[2, 2] == 'O'):
		return 2
	if (arr[0, 0] == 'O' and arr[1, 0] == 'O' and arr[2, 0] == 'O'):
		return 2
	if (arr[0, 1] == 'O' and arr[1, 1] == 'O' and arr[2, 1] == 'O'):
		return 2
	if (arr[0, 2] == 'O' and arr[1, 2] == 'O' and arr[2, 2] == 'O'):
		return 2
	if (arr[0, 0] == 'O' and arr[1, 1] == 'O' and arr[2, 2] == 'O'):
		return 2
	if (arr[0, 2] == 'O' and arr[1, 1] == 'O' and arr[2, 0] == 'O'):
		return 2
	return 0

arr = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
player = 1
while (1):
	os.system('CLS')
	print(arr)
	if (player == 1):
		print ("Игрок 1, введите куда ставить крестик")
	else:
		print("Игрок 2, введите куда ставить нолик")
	y = int(input ("введите строку\n"))
	x = int(input ("введите столбец\n"))
	if (y > 3 or y < 1 or x > 3 or y < 1):
		print ("Ваши координаты за пределами")
		continue
	if (arr[y - 1, x - 1] != ' '):
		print ("Клетка занята")
		continue
	if (player == 1):
		arr[y - 1, x - 1] = 'X'
		player = 2
	else:
		arr[y - 1, x - 1] = 'O'
		player = 1
	if (win_check(arr) == 1):
		print("Игрок 1 выиграл")
		break
	elif (win_check(arr) == 2):
		print("Игрок 2 выиграл")
		break
