from commom_calc.amount import amount_counter
from commom_calc.average import average_counter
from commom_calc.sorting import sorting
from commom_calc.report import report
from commom_calc.transaction import transaction

people = ['Риваль', 'Василий', 'Геннадий', 'Егор', 'Михаил', 'Ильнар',
          'Дядя Саша']  # люди

summ = [1771, 638, 500, 0, 0, 0, 0]  # потраченное каждым

amount = amount_counter(summ)
average = average_counter(summ, amount)

plus_people, plus_summ, minus_people, minus_summ, plus_people_rep, \
plus_summ_rep, minus_people_rep, minus_summ_rep = sorting(people, summ,
                                                          average)

transaction_minus, transaction_summ, transaction_plus = transaction(plus_people,
                                                                    plus_summ, minus_people, minus_summ)

report(people, summ, amount, average, plus_people_rep, plus_summ_rep, minus_people_rep,
       minus_summ_rep, transaction_minus, transaction_summ, transaction_plus)

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
