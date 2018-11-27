def distributor(people, summ, average):
    plus_people = []
    minus_people = []
    plus_summ = []
    minus_summ = []
    plus_people_rep = []
    minus_people_rep = []
    plus_summ_rep = []
    minus_summ_rep = []
    for i in range(0, len(summ)):
        if summ[i] > average:
            m = summ[i] - average
            plus_summ.append(m)
            plus_people.append(people[i])
            plus_summ_rep.append(m)
            plus_people_rep.append(people[i])
        elif summ[i] < average:
            n = average - summ[i]
            minus_summ.append(n)
            minus_people.append(people[i])
            minus_summ_rep.append(n)
            minus_people_rep.append(people[i])
        else:
            continue
    return plus_people, plus_summ, minus_people, minus_summ, plus_people_rep, \
           plus_summ_rep, minus_people_rep, minus_summ_rep
