def transaction(plus_people, plus_summ, minus_people, minus_summ):
    transaction_minus = []
    transaction_summ = []
    transaction_plus = []
    for i in range(0, len(minus_summ)):
        for l in range(0, len(plus_summ)):
            if plus_summ[l] <= 0:
                continue
            elif minus_summ[i] <= 0:
                continue
            else:
                if minus_summ[i] < plus_summ[l]:
                    transaction_minus.append(minus_people[i])
                    minus_summ[i] = float('{:.2f}'.format(minus_summ[i]))
                    transaction_summ.append(minus_summ[i])
                    transaction_plus.append(plus_people[l])
                    plus_summ[l] = plus_summ[l] - minus_summ[i]
                    minus_summ[i] = 0
                elif minus_summ[i] >= plus_summ[l]:
                    transaction_minus.append(minus_people[i])
                    plus_summ[l] = float('{:.2f}'.format(plus_summ[l]))
                    transaction_summ.append(plus_summ[l])
                    transaction_plus.append(plus_people[l])
                    minus_summ[i] = minus_summ[i] - plus_summ[l]

    return transaction_minus, transaction_summ, transaction_plus
