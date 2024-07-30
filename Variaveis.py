valor = 20
print(valor)
type(valor)

#conversão de variáveis

valorFloat = float(valor)
type(valorFloat)

# Operações matemáticas básicas com Números

# Adição
print(5+23)

# Subtração
print(100-25)

# Multiplicação
print(5*10)

# Potência/Exponente
# o operador ** é equivalente ao expoente
print(5**2)

# 5*5 = 5^2 = 5**2 
print(5*5)


# Divisão (float)
# Retornar o valor decimal real da divisão
print(36/4)
print(10/3)         

# Divisão (int)
# Retornar um int. Se o quociente real for um valor decimal, apenas um número inteiro irá retornar
print(10//3)
print(19//6)

# Divisão Modular: retornar o restante da divisão
print(10%3)

# Operações com Strings e Caracteres
print("foo" * 5)
print('x'*3)

print("hello " + str(5))

# Adição de String = concatenação   
print("hello " + "world")           

# Comparadores: retornar valor booleano

# Igualdade ==
# Nota: DEVE ser sinais de igual Duplos, um sinal de igual único é atribuição
print(5 == 5.0)

# Maior do que >
print(7 > 1)

# Menor do que <
print(1.5 < 90)

# Maior ou igual a >=
print(5.0 >= 5)
print(5.0 >= 4)
print(5 >= 13)

# Menor ou igual a <=
print(10 <= 10.0)
print(10 <= 20)
print(8 <= 3)

# Comparadores em Strings

print("hello" < "world")
print("hello" == "world")
print("hello" > "world")

print("hello" == "hello")

print("cat" < "dog")