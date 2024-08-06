# Inicializar um dicionário vazio
# O mesmo do conjunto, mas com:
dict = {}

# Declare um dicionário com pares de chaves/valores
dict2 = {'a': 5, 'b': 10, 'c': 100, 'd': 9.5}

print(dict2['b'])

dict2['b'] = 50

print(dict2['b'])

dict2['z'] = 999

print(dict2['z'])


dict["greeting"] = "hello message"
dict["alphabet"] = ['a', 'b', 'c', 'd', 'e']
dict["check-in"] = False
dict["phoneNumber"] = 8007782346

print(dict)

dict[('a','b', 'c')] = [False, True, False]
print(dict)

# Podemos também buscar todas as chaves
print(dict.keys())
print(dict.values())
print(dict.items())