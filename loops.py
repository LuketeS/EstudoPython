#for i in range(10):
 # print(i)

#for x in range(2, 10):
 # print(i)
  
#for i in range(0, 10, 3):
#  print(i)
  
#for i in "hello!":
 # print(i)
  
#string = "hello world!"
#for i in range(0, len(string), 2):
#  print(str(i) + "th letter is "+ string[i])

#count = 0
#while (count <= 10):
#  print(count)
#  count += 1

#while True:
 # user = input("Enter something to be repeated: ")

  ## Quando o "break" é acionado, o print() abaixo NÃO será executado.
  ## O programa romperá o loop quando esta palavra-chave for lida.
  #if user=="end":
   # print("Terminate the program!!!")
    #break
  #print(user)



  
end = False
while end == False:
  user = input("Enter something to be repeated 2: ")
  if user=="end":
    print("Program Ended!!!")
    end = True
  else:
    print(user)

count = 1

# Implementação do loop WHILE
while count + 1 <= 20:
  if count % 5 == 0:
    print("SKIP")
    count += 1
    continue
  print(count)
  count += 1

for i in range (1, 20):
  if i % 5 == 0:
    print("SKIP")
    continue
  print(i)