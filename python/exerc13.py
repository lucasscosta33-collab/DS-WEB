#casa

#entrada
valordacasa = int(input('qual e o valor da casa'))
salario = int(input('qual e o seu salario'))
parcela = int(input('quantas parcelas voce quer'))
#porcessamento
porcem = 30 * salario / 100
parceladacasa = valordacasa / parcela
if porcem > parcela:
     print('voce pode comprar ')
if porcem < parcela:
    print('voce nao pode comprar')
     
