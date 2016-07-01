__author__ = 'hmly'

SEC_IN_YEAR = 365 * 24 * 60 * 60


def project_pop(pop, year):
    birth = SEC_IN_YEAR / 7
    death = SEC_IN_YEAR / 13
    immigrant = SEC_IN_YEAR / 45

    for i in range(year):
        pop += birth - death + immigrant
    return pop


year2 = 5
curr_pop = 312032487
print("After %d years, the population is %d" % (year2, project_pop(curr_pop, year2)))
