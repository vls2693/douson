def transaction(plus_people, plus_summ, minus_people, minus_summ):
    transaction_minus = []
    transaction_summ = []
    transaction_plus = []
    for i in range(0, len(minus_summ)):
        for k in range(0, len(plus_summ)):
            if plus_summ[k] <= 0:
                continue
            elif minus_summ[i] <= 0:
                continue
            else:
                if minus_summ[i] < plus_summ[k]:
                    transaction_minus.append(minus_people[i])
                    minus_summ[i] = float('{:.2f}'.format(minus_summ[i]))
                    transaction_summ.append(minus_summ[i])
                    transaction_plus.append(plus_people[k])
                    plus_summ[k] = plus_summ[k] - minus_summ[i]
                    minus_summ[i] = 0
                elif minus_summ[i] >= plus_summ[k]:
                    transaction_minus.append(minus_people[i])
                    plus_summ[k] = float('{:.2f}'.format(plus_summ[k]))
                    transaction_summ.append(plus_summ[k])
                    transaction_plus.append(plus_people[k])
                    minus_summ[i] = minus_summ[i] - plus_summ[k]

    return transaction_minus, transaction_summ, transaction_plus
