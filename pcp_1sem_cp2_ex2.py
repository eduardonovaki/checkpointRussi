A= float(input("Digite um valor (maior valor): "))
B=float(input("Digite um valor: "))
C=float(input("Digite um valor: "))


#Ordem decrescente
lados= sorted([A,B,C],reverse=True)
A,B,C=lados


#Condição dos triângulos
if A>= B + C:
    print("Não forma Triângulo")
else:
 if A**2 == B**2 + C**2:
    print("Triangulo Retangulo")


 elif A**2 > B**2 + C**2:
   print("Triangulo Obtusângulo")
 elif A**2< B**2 + C**2:
    print("Triângulo Equilatero")


#Três ângulos iguais
if A==B==C:
 print("Triângulo equilatero")
# Dois ângulos iguais
elif A == B or B == C or A==C:
  print("Triângulo isosceles")
