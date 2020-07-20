T=int(input())
for _ in range(T):
    basic_salary=int(input())
    if basic_salary<1500:
        print("{0:.2f}".format(2*basic_salary))
    else:
        print("{0:.2f}".format(1.98*basic_salary+500))


