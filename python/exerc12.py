#operaçao

#entrada
n1 = int(input('qual e o seu numero '))
n2 = int(input('qual e o numero'))
op =  str(input('qual e a operacao'))
#processamento
if op == '+':
    res = n1 + n2
if op == '-':
    res = n1 - n2
if op == '*':
    res = n1 * n2
if op == '/':
    res = n1 / n2
print('a resposta e',res)

