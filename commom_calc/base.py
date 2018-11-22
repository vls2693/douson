from commom_calc.amount import amount_counter
from commom_calc.average import average_counter
from commom_calc.distributor import distributor
from commom_calc.report import report

people = ['Риваль', 'Василий', 'Геннадий', 'Егор', 'Михаил', 'Ильнар',
          'Дядя Саша']  # люди
summ = [1771, 638, 500, 0, 0, 0, 0]  # потраченное каждым

amount = amount_counter(summ)
average = average_counter(summ, amount)


def transaction(plus_people, plus_summ, minus_people, minus_summ):
    transaction_minus = []
    transaction_summ = []
    transaction_plus = []
    for i in range(0, len(minus_summ)):
        for l in range(0, len(plus_summ)):
            if minus_summ[i] < plus_summ[l]:
                transaction_minus.append(minus_people[i])
                transaction_summ.append(minus_summ[i])
                transaction_plus.append(plus_people[l])
                plus_summ[l] = plus_summ[l] - minus_summ[i]
            elif minus_summ[i] >= plus_summ[l]:
                transaction_minus.append(minus_people[i])
                transaction_summ.append(plus_summ[l])
                transaction_plus.append(plus_people[l])
                del plus_summ[l]
                del plus_people[l]
                minus_summ[i] = minus_summ[i] - plus_summ[l]
                continue

    return transaction_minus, transaction_summ, transaction_plus



plus_people, plus_summ, minus_people, minus_summ = distributor(people, summ,
                                                               average)


print(transaction(plus_people, plus_summ, minus_people, minus_summ))
print(plus_people, plus_summ, minus_people, minus_summ)
print(len(plus_people), len(plus_summ), len(minus_people), len(minus_summ))
report(people, summ, amount, average, plus_people, plus_summ, minus_people,
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
тут str не нужно, обрати внимание, 
про format  все переменные полиморфируют в стринги
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
