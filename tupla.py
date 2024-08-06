# Inicializar uma tupla vazia
y = tuple()
print(y)

# Criar uma nova tupla de elementos
x = (1,2,3)
print(x)
print(y)
#x.append(4)
print(x)
x + (4,5,6)
print(x)
x * 2
print(x)

a,b,c = 1,2,3
print(a)
print(b)
print(c)

xx = (1,2,3,4)
list(xx)
print(xx)

# Declarar uma nova tupla, nome "person"
person  = ('Jane','Doe', 21)

# "Pacote"/associar cada elemento da tupla com uma etiqueta. Observe a ordem das etiquetas.
first, last, age = person

print(first)
print(last)
print(age)

# ERROR: x é uma tupla de 4 valores, mas está tentando descompactar SOMENTE 3 elementos.
# Incompatibilidade no tamanho da tupla
x = (1,2,3,4)

a,b,c,d = x

print(a)
print(b)
print(c)
print(d)
