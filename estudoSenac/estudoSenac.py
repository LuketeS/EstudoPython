#Parte 1
#print("Hello World")

#Variaveis e tipos tipagem dinâmica e forte

#a = 5
#b = 6.7
#c = "string"
#boolean = True # ou false
#nulo = None
#print(nulo)


#Parte 2 Coleções

#Lista = array
#lista_ruim = [1, "nome", True, [2]] #diferentes tipos de item
#lista = [5, 8, 9, 0]

#tamanho = len(lista)
#elemento = lista[0]
#lista.append(99)

#print(lista)

#Parte 3 - Dicionários ou hash

#dicionario = {"a" : 1, "b" : 2, "c" : 1}
#print(dicionario)
#print(dicionario["c"])
#dicionario["d"] = 99
#print(dicionario)

#Parte 4 - Estruturas de controle IF
#idade = 70
#if idade >= 60:
    #print("idoso")
    #print("passou aqui")
#elif idade >= 18:
    #print("adulto")
#else:
    #print("jovem")
#print("fim")
#Parte 4 - Estruturas de controle WHILE
#i = 0
#while i < 10:
    #print(i)
    #i += 1

#Parte 4 - Estruturas de controle FOR é bom para usar com coleções

#lista = [5, 8, 9, 0]
#for item in lista:
    #print(item + 10)

# dicionario = {"a" : 1, "b" : 2, "c" : 1}
#   for item in dicionario:
#     #print(item) #anda pelas chaves
#     #print(item + " - " + str(dicionario[item])) #o str converte para string

# for chave, valor in dicionario.items():
#     print(chave + "-" + str(valor))

#Parte 5 Funções
# def fahrentheit_para_celsius (temp_fahr):
#     return (temp_fahr - 32 ) *5/9

# temp_celsius = fahrentheit_para_celsius(70)
# print(temp_celsius)


# #Parte 6 Objetos
# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome
    
#     def setaIdade(self, idade):
#         self.idade = idade
    
#     def getIdade(self):
#         return self.idade

#     def __str__(self): #se utilizar esse __str__ vocë escolhe como vai ser printado o objeto, ai sõ precisar dar print(nomedoobjeto)
#         return "Nome: " +self.nome + ", idade: " + str(self.idade)
# p = Pessoa("João")
# p.setaIdade(30)
# print(p.getIdade())
# print(p.nome)
# print(p)

# #parte 8 - Ler e escrever em arquivos
# arquivo = open("arquivo.txt", "a") #modo "w" sempre escreve o arquivo do inicio, deletando o que tinha, para escrever coisas a mais no arquivo usar "a"
# arquivo.write("\n Quarta linha")
# arquivo.close()

# outro = open("arquivo.txt", "r")
# for linha in outro:
#     print("Linha" + linha)
# outro.close()

#Parte 8 - Módulos

#essa abaixo chama o modulo e executa uma função dentro dele
# import conversor
# c = conversor.fahrentheit_para_celsius(100)
# print(c)

#desse jeito só chama a função
# from conversor import fahrentheit_para_celsius
# c = fahrentheit_para_celsius(88)
# print(c)