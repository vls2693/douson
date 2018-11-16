people = ['Риваль', 'Василий', 'Геннадий', 'Егор', 'Михаил', 'Ильнар', 'Дядя Саша'] # люди
summ = [1771, 638, 500, 0, 0, 0, 0] # потраченное каждым

def amount(summ):
    amount = 0;
    for i in range(0, len(summ)):
        amount = round(amount + summ[i], 2)
    return amount

def average(summ, amount): # среднее арифметическое потраченного
    average = round(amount / len(summ), 2)
    return average

def shortage(summ, average): # определяем кто сколько должен доплатить
    shortage = []
    for i in range(0, len(summ)):
        short = round(average - summ[i], 2)
        shortage.append(short)
    return shortage

def money(summ, average): # определяем кто сколько должен получить
    money = []
    for i in range(0, len(summ)):
        inc = round(summ[i] - average, 2)
        money.append(inc)
    return money

amount = amount(summ)
average = average(summ, amount)
shortage = shortage(summ, average)
money = money(summ, average)


def report(people, summ, amount, average, shortage, money): # отчёт
    print('Скидывали:')
    for i in range(0, len(summ)):
        if summ[i] != 0:
            print(str(people[i]) + " - " + str(summ[i]) + "р.")
    print()
    print("Всего потрачено: " + str(amount))
    print()
    print("С каждого по " + str(average) + "р.")
    print()
    print("Должны скинуть: ")
    for i in range(0, len(shortage)):
        if shortage[i] > 0:
            print(str(people[i]) + ' - ' + str(shortage[i]) + "р.")
    print()
    print("Должны получить: ")
    for i in range(0, len(money)):
        if money[i] > 0:
            print(str(people[i]) + ' - ' + str(money[i]) + "р.")
report(people, summ, amount, average, shortage, money)


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