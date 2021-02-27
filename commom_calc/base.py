from commom_calc.amount import amount_counter
from commom_calc.average import average_counter
from commom_calc.sorting import sorting
from commom_calc.report import report
from commom_calc.transaction import transaction


def receiver(whole_list):
    people = []
    common_sum = []
    whole_list = whole_list
    for i in range(0, int(len(whole_list) / 2)):
        print(whole_list.get('name{}'.format(i)))
        if whole_list.get('name{}'.format(i)) == '':
            break
        else:
            people.append(whole_list.get('name{}'.format(i)))
            common_sum.append(int(whole_list.get('sum{}'.format(i))))

    amount = amount_counter(common_sum)
    average = average_counter(common_sum, amount)

    plus_people, plus_sum, minus_people, minus_sum, plus_people_rep, \
        plus_sum_rep, minus_people_rep, minus_sum_rep = \
        sorting(people, common_sum, average)

    transaction_minus, transaction_sum, transaction_plus = transaction(
        plus_people, plus_sum, minus_people, minus_sum)

    report(people, common_sum, amount, average, plus_people_rep, plus_sum_rep,
           minus_people_rep, minus_sum_rep, transaction_minus,
           transaction_sum, transaction_plus)


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
