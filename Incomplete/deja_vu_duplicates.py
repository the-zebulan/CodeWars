class Employee:
    def __init__(self, f_name, l_name, u_name):
        self.first_name = f_name
        self.last_name = l_name
        self.user_name = u_name


def find_duplicates(employees):
    duplicates = []
    seen = set()
    for i, employee in enumerate(employees):
        current = tuple(sorted(employee.__dict__.items()))  # sort?
        print current
        if current in seen:
            duplicates.append(employee)
            employees.pop(i)
            # employees.remove(employee)
        else:
            seen.add(current)
    return duplicates


guys = [["Johnathan", "Joestar", "JoJo"], ["Dio", "Brando", "DIO"],
        ["Joseph", "Joestar", "JoJo"], ["Kars", "", "the ultimate being"]]
employees = []
length = len(guys)
for guy in xrange(5):
    g = guy % length
    employees.append(Employee(*guys[g]))
solution = [employees[4]]
# print solution
print find_duplicates(employees) == solution
print len(employees) == 4
