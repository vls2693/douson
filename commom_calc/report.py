from flask import render_template


def report(people, common_sum, amount, average, plus_people_rep, plus_sum_rep,
           minus_people_rep, minus_sum_rep, transaction_minus,
           transaction_sum, transaction_plus):  # отчёт
    name_list = 'Скидывали:'
    br = '<br>'
    back_link = '<a href="/">Вернуться назад</a>'
    with open("../flask/templates/file.html", "w", encoding="utf-8") as file:
        file.write(name_list)
        file.write(br)
        for i in range(0, len(common_sum)):
            names = (str(people[i]) + " - " + str(common_sum[i]) + "р.")
            # Write HTML to file.html
            file.write(names)
            file.write(br)
        file.write(br)
        file.write(str("Всего потрачено: {}р.".format(amount)))
        file.write(br)
        file.write(br)
        file.write(str("Среднее арифметическое потраченного {}р.".format(average)))
        file.write(br)
        file.write(br)
        file.write("Должны скинуть: ")
        file.write(br)
        for i in range(0, len(minus_people_rep)):
            debt = (str(minus_people_rep[i]) + ' - {}р.'.format(minus_sum_rep[i]))
            file.write(debt)
            file.write(br)
        file.write(br)
        file.write("Должны получить: ")
        file.write(br)
        for i in range(0, len(plus_people_rep)):
            overpay = ('{} - {}р.'.format(plus_people_rep[i], plus_sum_rep[i]))
            file.write(overpay)
            file.write(br)
        file.write(br)
        file.write("Список транзакций: ")
        file.write(br)
        for i in range(0, len(transaction_minus)):
            transactions = (transaction_minus[i] + ' ---> ' + transaction_plus[i] + "  " + str(transaction_sum[i])
                            + "р.")
            file.write(transactions)
            file.write(br)
        file.write(back_link)
        file.close()
    return render_template('file.html')

# пример записи в html
# http://qaru.site/questions/308612/how-to-write-and-save-html-file-in-python
