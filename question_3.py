jordan_belfort = {"calls": 178, "meetings":17, "sales":6}
James_a = {"calls": 108, "meetings":15, "sales":10}
John_b = {"calls": 138, "meetings":30, "sales":4}
Robert_c = {"calls": 153, "meetings":10, "sales":3}
Mary_d = {"calls": 49, "meetings":9, "sales":0}
Patricia_e = {"calls": 520, "meetings":57, "sales":46}
Jennifer_f = {"calls": 490, "meetings":71, "sales":60}

def calculate_total_score(emp_dict):
    points = 0
    points += emp_dict["calls"] * 10
    points += emp_dict["meetings"] * 30
    points += emp_dict["sales"] * 100
    if ((emp_dict["calls"] > 150) or (emp_dict["meetings"] > 20) or (emp_dict["sales"] > 5)):
        points += 100
    emp_dict["score"] = points

calculate_total_score(jordan_belfort)
print("jordan_belfort", jordan_belfort)

calculate_total_score(James_a)
print("James_a", James_a)

calculate_total_score(John_b)
print("John_b", John_b)

calculate_total_score(Robert_c)
print("Robert_c", Robert_c)

calculate_total_score(Mary_d)
print("Mary_d", Mary_d)

calculate_total_score(Patricia_e)
print("Patricia_e", Patricia_e)

calculate_total_score(Jennifer_f)
print("Jennifer_f", Jennifer_f)