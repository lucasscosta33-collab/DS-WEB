#3
agenda={}

while True:
    print("\n--- LISTA DE contato ---")
    print("1. Adicionar contato")
    print("2. buscar")
    print("3. Remover contato")
    print("4. lista")
    print('5 sair')
    opcao = input("Escolha a opção desejada:")

    if opcao =='1':
       contato=input('adicionar nome  contato novo ')
       numero=input('escreva o numero de telefone')
       agenda.update({ contato :numero})
       print('contato adicionado')
    elif opcao =='2':
        if contato in agenda:
         input('escreva o nome ') 
         print(agenda.get(contato))
    elif opcao=='3':
        print(agenda)
        input('quem voce quer remover')
        del agenda[contato],[numero]
        print(agenda)
        elif opcao ==100
          print('hehheheheheh')
    else:
         print("")
         break
