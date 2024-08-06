# Inicializar um conjunto vazio
newSet = set()
print(newSet)
ex1 = {1, 2, 2, 1, 1}
print(ex1)

ex2 = {j for j in range(10)}
print(ex2)

ex2.add(2)
ex2.add(100)
ex2.add(50)
print(ex2)

# Converter uma lista em um conjunto
ages = [10, 5, 4, 5, 2, 1, 5]

set_of_ages = set(ages)

print(set_of_ages)

set_of_ages.add(3)
print(set_of_ages)


list_of_ages = list(set_of_ages)

print(list_of_ages)
list_of_ages

{1,2,3} == {2,1,3}