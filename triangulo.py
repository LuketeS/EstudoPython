"""
Escreveremos nossa própria função que testa se um triângulo de 3 lados é um triângulo retângulo. 
Como não podemos controlar a ordem dos lados que o usuário nos dá (de tal forma que C é o comprimento mais longo), 
precisamos verificar manualmente se C é o comprimento mais longo (os comprimentos A e B podem estar em qualquer ordem). 
Caso contrário, nosso teorema de Pitágoras falhará. 
"""

def isRightTriangle(a, b, c):

  # Reatribuir valores variáveis para garantir que C seja o comprimento mais longo
  if (max(a,b,c) != c):

    # tmp armazena os valores anteriores de C, que não é o comprimento mais longo
    tmp = c
    c = max(a,b,c)

    if a == c:
      a = tmp
    elif b == c:
      b = tmp
    

  # Aplicar a fórmula
  if a**2 + b**2 == c**2:
    print("Right Triangle")

    # Se o programa vê uma declaração Return, este é o FIM do programa/função
    return True
  
  # Estas duas linhas funcionarão SOMENTE quando a condição IF for falsa
  print("NOT a right triangle")
  return False


# Solicite ao usuário que insira 3 comprimentos
def main():
  a = input("Enter the length for the first edge of the triangle:")
  b = input("Enter the length for the second edge of the triangle:")
  c = input("Enter the length for the last edge of the triangle:")

  # As entradas do usuário são armazenadas como uma string, então nós as computamos para ser int
  return isRightTriangle(int(a), int(b), int(c))

if __name__ == "__main__":
    main()