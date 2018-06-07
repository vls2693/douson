try:
    num = float(input("\nВведите число: "))
except ValueError as e:
    print("Это не число! Интерпретатор как бы говорит нам: ")
    print(e)