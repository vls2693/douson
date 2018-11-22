def amount_counter(summ):
    amount = 0
    for i in range(0, len(summ)):
        amount = round(amount + summ[i], 2)
    return amount
