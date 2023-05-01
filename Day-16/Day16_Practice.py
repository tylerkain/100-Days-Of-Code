
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon", "Type"]
table.add_row(["Squirtle", "Water"])

print(table)
