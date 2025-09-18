matriz= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
totalizador = 0
for linha in matriz:
    print('linha : ', linha[0])
    for item in linha :
        print('item:',item)
        totalizador += item  
print(totalizador)


