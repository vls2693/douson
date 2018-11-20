people = ['Риваль', 'Василий', 'Геннадий', 'Егор', 'Михаил', 'Ильнар',
          'Дядя Саша'] # люди
summ = [1771, 638, 500, 0, 0, 0, 0] # потраченное каждым


def amount(summ):
    amount = 0
    for i in range(0, len(summ)):
        amount = round(amount + summ[i], 2)
    return amount


def average(summ, amount): # среднее арифметическое потраченного
    average = round(amount / len(summ), 2)
    return average


amount = amount(summ)
average = average(summ, amount)


def distributor(people, summ, average):
    plus_people = []
    minus_people = []
    plus_summ = []
    minus_summ = []
    for i in range(0, len(summ)):
        if summ[i] > average:
            m = summ[i] - average
            plus_summ.append(m)
            plus_people.append(people[i])
        elif summ[i] < average:
            n = average - summ[i]
            minus_summ.append(n)
            minus_people.append(people[i])
        else:
            continue
    return plus_people, plus_summ, minus_people, minus_summ


def transaction(plus_people, plus_summ, minus_people, minus_summ):
    for i in range(0, len(minus_summ)):
        for l in range(len(plus_summ)):
            print()



plus_people, plus_summ, minus_people, minus_summ = distributor(people, summ,
                                                               average)

print(plus_people, plus_summ, minus_people, minus_summ)


def report2(people, summ, amount, average, plus_people, plus_summ, minus_people,
            minus_summ): # отчёт
    print('Скидывали:')
    for i in range(0, len(summ)):
        if summ[i] != 0:
            print(str(people[i]) + " - " + str(summ[i]) + "р.")
    print()
    print("Всего потрачено: " + str(amount))
    print()
    print("Среднее арифметическое потраченного " + str(average) + "р.")
    print()
    print("Должны скинуть: ")
    for i in range(0, len(minus_people)):
        print(str(minus_people[i]) + ' - ' + str(minus_summ[i]) + "р.")
    print()
    print("Должны получить: ")
    for i in range(0, len(plus_people)):
        print(str(plus_people[i]) + ' - ' + str(plus_summ[i]) + "р.")


report2(people, summ, amount, average, plus_people, plus_summ, minus_people,
            minus_summ)


'''
from Rebel:

никогда  не называй
переменные и функции одним и тем же именем
транслитом

def transaction(plus_people, plus_summ, minus_people, minus_summ):
    for i in range(0, len(minus_summ)):
        for l in range(len(plus_summ)):
            print()
короче адок. Никогда так не делай. Не надо все в отдельных переменных хранить
Должен быть класс человека
и у него параметры
аргументы

print("Всего потрачено: " + str(amount))
не надо складывать. Плохая привычка
потому что память начинает хратить 3 варианта - два отдельных слагаемых и сумму
лучше .join или .format

print("Всего потрачено: {}".format(amount))
тут str не нужно, обрати внимание, про format  все переменные полиморфируют в стринги
'''


'''
def calc_person(b):
    #n = int(input())
    for i in range(b):
        new_element = str(input())
        a.append(new_element)


def calc_bill(b):
    #n = int(input())
    for i in range(b):
        new_element = int(input())
        b.append(new_element)


calc_person(people)
calc_bill(summ)

print(people)
print(summ)
'''
'''
d = {'Риваль': 1771, 'Василий': 638, 'Геннадий': 500, 'Егор': 0, 'Михаил': 0,
     'Ильнар': 0, 'Дядя Саша': 0}
print(dict.items(d))
print(dict.keys(d))
'''