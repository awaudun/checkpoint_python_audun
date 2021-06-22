from os import write
import json
file_path = "python_cp1_q1_data.txt"

data = {"customers": ["James", "John", "Robert", "Mary", "Patricia", "Jennifer"],
        "salary": [155000, 755000, 455000, 1255000, 635000, 575000],
        "taxes": [55800, 317100, 182000, 451800, 171450, 71400]}
#data = {}

def print_customers_small_tax():
    for c, s, t in zip(data["customers"], data["salary"], data["taxes"]):
        if (t / s) < .3:
            print(c)

print_customers_small_tax()

# --------------------------

def load_dict():
    try:
        file = open(file_path, "r")
        data = json.load(file)
    except Exception as e:
        print("Load fail: ", e)
    finally:
        file.close()

def save_dict():
    try:
        file = open(file_path, 'w')
        json.dump(data, file)
    except Exception as e:
        print("Save fail: ", e)
    finally:
        file.close()
print("-")
# --------------------------
