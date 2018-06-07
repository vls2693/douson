try:
    num = float(input("\nВведите число: "))
except ValueError:
    print("Это не число!")
else:
    print("Вы ввели число ", num)
input("\n\nНажмите Enter, чтобы выйти")