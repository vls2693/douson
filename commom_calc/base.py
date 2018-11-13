people = []
summ = []


def calc_person(a):
    #a = []
    n = int(input())
    for i in range(n):
        new_element = str(input())
        a.append(new_element)


def calc_bill(b):
    #b = []
    n = int(input())
    for i in range(n):
        new_element = int(input())
        b.append(new_element)


calc_person(people)
calc_bill(summ)

print(people)
print(summ)
