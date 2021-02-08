def transaction(plus_people, plus_sum, minus_people, minus_sum):
    transaction_minus = []
    transaction_summ = []
    transaction_plus = []
    for i in range(0, len(minus_sum)):
        for k in range(0, len(plus_sum)):
            if plus_sum[k] <= 0:
                continue
            elif minus_sum[i] <= 0:
                continue
            else:
                if minus_sum[i] < plus_sum[k]:
                    transaction_minus.append(minus_people[i])
                    minus_sum[i] = float('{:.2f}'.format(minus_sum[i]))
                    transaction_summ.append(minus_sum[i])
                    transaction_plus.append(plus_people[k])
                    plus_sum[k] = plus_sum[k] - minus_sum[i]
                    minus_sum[i] = 0
                elif minus_sum[i] >= plus_sum[k]:
                    transaction_minus.append(minus_people[i])
                    plus_sum[k] = float('{:.2f}'.format(plus_sum[k]))
                    transaction_summ.append(plus_sum[k])
                    transaction_plus.append(plus_people[k])
                    minus_sum[i] = minus_sum[i] - plus_sum[k]

    return transaction_minus, transaction_summ, transaction_plus
