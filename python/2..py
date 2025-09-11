#2
estoque = {
"mouse": 50,
"teclado": 30,
"monitor": 15,
"fone": 20
}
produto=input('digite o produto ' )

if produto in estoque :
    print(f"seu produto existe : {estoque[produto]}")

elif produto :
    input('produto não encontado!')
