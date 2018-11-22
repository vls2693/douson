def report(people, summ, amount, average, plus_people, plus_summ, minus_people,
            minus_summ): # отчёт
    print('Скидывали:')
    for i in range(0, len(summ)):
        if summ[i] != 0:
            print(str(people[i]) + " - " + str(summ[i]) + "р.")
    print()
    print("Всего потрачено: {}".format(amount))
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