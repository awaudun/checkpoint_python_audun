customers = ["James", "John", "Robert", "Mary", "Patricia", "Jennifer"]
salary = [155000, 755000, 455000, 1255000, 635000, 575000]
taxes = [55800, 317100, 182000, 451800, 171450, 71400]

for c, s, t in zip(customers, salary, taxes):
    if (t / s) < .3:
        print(c)

