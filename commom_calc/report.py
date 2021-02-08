from flask import render_template


def report(people, summ, amount, average, plus_people_rep, plus_summ_rep,
           minus_people_rep, minus_summ_rep, transaction_minus,
           transaction_summ, transaction_plus):  # отчёт
    name_list = 'Скидывали:'
    br = '<br>'
    with open("../flask/templates/file.html", "w", encoding="utf-8") as file:
        file.write(name_list)
        file.write(br)
        for i in range(0, len(summ)):
            names = (str(people[i]) + " - " + str(summ[i]) + "р.")
            # Write to HTML to file.html
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
            debt = (str(minus_people_rep[i]) + ' - {}р.'.format(minus_summ_rep[i]))
            file.write(debt)
            file.write(br)
        file.write(br)
        file.write("Должны получить: ")
        file.write(br)
        for i in range(0, len(plus_people_rep)):
            overpay = (str(plus_people_rep[i]) + ' - {}р.'.format(plus_summ_rep[i]))
            file.write(overpay)
            file.write(br)
        file.write(br)
        file.write("Список транзакций: ")
        file.write(br)
        for i in range(0, len(transaction_minus)):
            transactions = (transaction_minus[i] + ' ---> ' + transaction_plus[i] + "  " + str(transaction_summ[i])
                            + "р.")
            file.write(transactions)
            file.write(br)

    # print()
    # print("Всего потрачено: {}р.".format(amount))
    # print()
    # print("Среднее арифметическое потраченного {}р.".format(average))
    # print()
    # print("Должны скинуть: ")
    # for i in range(0, len(minus_people_rep)):
    #     print(str(minus_people_rep[i]) + ' - {}р.'.format(minus_summ_rep[i]))
    # print()
    # print("Должны получить: ")
    # for i in range(0, len(plus_people_rep)):
    #     print(plus_people_rep[i] + ' - {}р.'.format(plus_summ_rep[i]))
    # print()
    # print("Список транзакций: ")
    # for i in range(0, len(transaction_minus)):
    #     print(transaction_minus[i] + ' ---> ' + transaction_plus[i]
    #           + "  " + str(transaction_summ[i]) + "р.")
    return render_template('file.html')
    # Write to HTML to file.html


# def report(people, summ, amount, average, plus_people_rep, plus_summ_rep,
#            minus_people_rep, minus_summ_rep, transaction_minus,
#            transaction_summ, transaction_plus):  # отчёт
#     print('Скидывали:')
#     for i in range(0, len(summ)):
#         print(str(people[i]) + " - " + str(summ[i]) + "р.")
#     print()
#     print("Всего потрачено: {}р.".format(amount))
#     print()
#     print("Среднее арифметическое потраченного {}р.".format(average))
#     print()
#     print("Должны скинуть: ")
#     for i in range(0, len(minus_people_rep)):
#         print(str(minus_people_rep[i]) + ' - {}р.'.format(minus_summ_rep[i]))
#     print()
#     print("Должны получить: ")
#     for i in range(0, len(plus_people_rep)):
#         print(plus_people_rep[i] + ' - {}р.'.format(plus_summ_rep[i]))
#     print()
#     print("Список транзакций: ")
#     for i in range(0, len(transaction_minus)):
#         print(transaction_minus[i] + ' ---> ' + transaction_plus[i]
#               + "  " + str(transaction_summ[i]) + "р.")
#     return render_template('file.html')
# float('{:.2f}'.format(minus_summ[i]))
# пример записи в html
# http://qaru.site/questions/308612/how-to-write-and-save-html-file-in-python

# HTML String
# html = """
# <table border=1>
#      <tr>
#        <th>Number</th>
#        <th>Square</th>
#      </tr>
#      <indent>
#      <% for i in range(10): %>
#        <tr>
#          <td><%= i %></td>
#          <td><%= i**2 %></td>
#        </tr>
#      </indent>
# </table>
# """
# # Write to HTML to file.html
# with open("../flask/templates/file.html", "a") as file:
#     file.write(html)
