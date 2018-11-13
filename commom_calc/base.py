x = ['первый', 'второй', 'третий']


def x3(*args):
    for i in range(0, 3):
        print(*args[0][i])


x3(x)
