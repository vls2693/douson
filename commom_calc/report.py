

def report(people, summ, amount, average, plus_people_rep, plus_summ_rep,
           minus_people_rep, minus_summ_rep, transaction_minus,
           transaction_summ, transaction_plus):  # отчёт
    html = """
    <p>
    print('Скидывали:')
    for i in range(0, len(summ)):
        print(str(people[i]) + " - " + str(summ[i]) + "р.")
    print()
    print("Всего потрачено: {}р.".format(amount))
    print()
    print("Среднее арифметическое потраченного {}р.".format(average))
    print()
    print("Должны скинуть: ")
    for i in range(0, len(minus_people_rep)):
        print(str(minus_people_rep[i]) + ' - {}р.'.format(minus_summ_rep[i]))
    print()
    print("Должны получить: ")
    for i in range(0, len(plus_people_rep)):
        print(plus_people_rep[i] + ' - {}р.'.format(plus_summ_rep[i]))
    print()
    print("Список транзакций: ")
    for i in range(0, len(transaction_minus)):
        print(transaction_minus[i] + ' ---> ' + transaction_plus[i]
              + "  " + str(transaction_summ[i]) + "р.")
    </p>
    """

# float('{:.2f}'.format(minus_summ[i]))
# пример записи в html
# http://qaru.site/questions/308612/how-to-write-and-save-html-file-in-python


# Write to HTML to file.html
with open("file.html", "w") as file:
    file.write(report)
