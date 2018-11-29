def amount_counter(list_of_summ):
    amount = 0
    for i in range(0, len(list_of_summ)):
        amount = round(amount + list_of_summ[i], 2)
    return amount
