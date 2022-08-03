dept_header     = "   ID   |       Created        |        Updated        |     Name     "
salaries_header = "   ID   |       Created        |        Updated        |  Amount  "

def read_departments(path):
    data = open(path, 'r')
    for line in data:
        line = line.replace("\n", "")
        list_items = line.split(';')
        print(f"  {list_items[0]} | {list_items[2]}  | {list_items[3]}   |  {list_items[1]}  ")
    data.close()

def show_items(file_name):
    path = 'organization/' + file_name + '.csv'
    if file_name == "departments":
        print(dept_header)
        read_departments(path)
    if file_name == "salaries":
        print(salaries_header)
        read_salaries(path)

def read_salaries(path):
    data = open(path, 'r')
    for line in data:
        line = line.replace("\n", "")
        list_items = line.split(';')
        print(f"  {list_items[0]} | {list_items[2]}  | {list_items[3]}   |  {list_items[1]}  ")
    data.close()
