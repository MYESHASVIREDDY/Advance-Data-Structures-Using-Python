# searching an element in a dictionary
a_dict = { "a" : ["1", "3"], "b" : ["3","4"], "c": ["5", "6"]}

search = "3"
values = []
for value in a_dict.values():
  if search in value:
        values.append(value)

print(values)