s = 0
soma = 0
while True:
 v = float(input("Digite um número a somar ou -0 para sair: "))
 if v %2 == 0:
     soma = soma + v
 elif v < 0:
   break
print (soma)
