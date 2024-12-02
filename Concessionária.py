print("~~~~~~ 𝓬𝓸𝓷𝓬𝓮𝓼𝓼𝓲𝓸𝓷𝓻𝓲𝓪 𝓭𝓸 𝓪𝓵𝓪𝓷𝔃𝓲𝓷 ~~~~~~")
print("\n~~~~~~ 𝓬𝓪𝓭𝓪𝓼𝓽𝓻𝓸 𝓭𝓸𝓼 𝓬𝓵𝓲𝓮𝓷𝓽𝓮𝓼 ~~~~~~\n")

#CADASTRO DOS CLIENTES
nome = str (input("DIGITE O NOME DO CLIENTE: "))
tel = int (input("DIGITE O NÚMERO DO TELEFONE DO CLIENTE: "))
saldo = float (input("DIGITE O SALDO TOTAL DO CLIENTE: "))


#DICIONARIOS DE CARROS DISPONIVEIS NA CONCESSIONARIA
carros = {
    "Mitsubish":["Lancer","Galant","Eclipse"],
    "BMW":["X6","X5","M4"],
    "Audi":["Q6","RS6","A4"],
    "Jaguar":["F-TYPE COUPÉ","F-PACE","I-PACE"],
    "Ferrari":["Purosangue","Roma","296-GTS"],
}


#TABELA FIPE DOS CARROS DENTRO DO DICIONARIO (CARROS).
fipe = {
   "Lancer": 69556, "Galant": 28483, "Eclipse": 134371,        #MISTSUBISHI
    "X6": 897168, "X5":551697, "M4":429961,                    #BMW
    "Q6":529990, "RS6": 830772, "A4": 223538,                  #AUDI
    "F-TYPE COUPÉ": 2000, "F-PACE":520909, "I-PACE":497556,    #JAGUAR
    "Purosangue": 7090301, "Roma":3278578, "296-GTS":3810648,   #FERRARI
}


#ESTRUTURA DE REPETIÇÃO PARA O SISTEMA DE COMPRA, VENDA E ALUGUEL DE VEICULOS
while True : #ESTRUTURA DE REPETIÇÃO PARA FICAR EM LOOPING ATÉ QUE O USUÁRIO DIGITE A OPÇÃO DE SAIR (4)

    print("\n~~~~~~ 𝓼𝓲𝓼𝓽𝓮𝓶𝓪 𝓭𝓮 𝓬𝓸𝓶𝓹𝓻𝓪, 𝓿𝓮𝓷𝓭𝓪 𝓮 𝓪𝓵𝓾𝓰𝓾𝓮𝓵 𝓭𝓮 𝓿𝓮𝓲𝓬𝓾𝓵𝓸𝓼 ~~~~~~\n")
    
    print("\n~~~~~~ 𝓶𝓮𝓷𝓾 𝓸𝓹𝓬𝓸𝓮𝓼 ~~~~~~\n")

    print("(1) - COMPRA DE VEÍCULOS")
    print("(2) - VENDA DE VEÍCULOS")
    print("(3) - ALUGUEL DE VEÍCULOS")
    print("(4) - SAIR")

    option = int (input ("DIGITE A OPÇÃO QUE DESEJA ACESSAR: "))

    if option == 1 : #OPÇÃO RESERVADA CASO O CLIENTE QUEIRA VENDER PARA LOJA
         
        print("\n~~~~~~ 𝓿𝓮𝓲𝓬𝓾𝓵𝓸𝓼 𝓺𝓾𝓮 𝓪𝓬𝓮𝓲𝓽𝓪𝓶𝓸𝓼 𝓹𝓻𝓸𝓹𝓸𝓼𝓽𝓪𝓼 ~~~~~~\n")

        for marca in carros: #IRÁ PERCORRER TODAS AS MARCAS DE CARROS DISPONIVEIS DENTRO DO DICIONARIO (CARROS) E PRINTAR ELAS
            print(marca)

        marca = input ("\nDIGITE QUAL A MARCA DO SEU VEÍCULO: ")

        for modelo in fipe: #IRÁ PERCORRER TODOS OS MODELOS DISPONIVEIS DENTRO DA MARCA SELECIONADA PELO USUÁRIO
            print(carros[marca])
            modelo = input ("\nESCOLHA O MODLEO REFERENTE AO DO SEU VEÍCULO: ")
            
            desconto = fipe[modelo] * 0.12
            proposta = fipe[modelo] - desconto
            
            print(f"\nNOSSA PROPOSTA DE VALOR PELO SEU VEÍCULO É DE R${proposta:.2f}")
            fecharnegocio = str (input ("DESEJA FECHAR NEGÓCIO? (S)/(N): ")).lower()
            
            if fecharnegocio == "s" : #CONDIÇÃO CASO O USUÁRIO ACEITE FECHAR NEGÓCIO
                saldocliente = proposta + saldo
                
                print(f"O saldo do cliente é de R${saldocliente}")
                break
                
                
            elif fecharnegocio == "n" : #CONDIÇÃO CASO O USUÁRIO NÃO ACEITE FECHAR NEGÓCIO
                print("Negócio cancelado.\nObrigado por usar nosso sistema.")
                break
                
                
            else : #CONDIÇÃO CASO O USUÁRIO DIGITE UMA LETRA DIFERENTE DE (S) OU (N)
                print("ERRO, NOT FOUND.")
                break
                
                
    elif option == 2 : #OPÇÃO RESERVADA PARA A LOJA VENDER PARA UM CLILENTE
        print("\n~~~~~~ 𝓬𝓪𝓻𝓻𝓸𝓼 𝓭𝓲𝓼𝓹𝓸𝓷𝓲𝓿𝓮𝓲𝓼 𝓮𝓶 𝓷𝓸𝓼𝓼𝓸 𝓼𝓲𝓼𝓽𝓮𝓶𝓪 ~~~~~~\n")
        
        print(carros)
        
        print("\n~~~~~~ 𝓬𝓪𝓻𝓻𝓸𝓼 𝓭𝓲𝓼𝓹𝓸𝓷𝓲𝓿𝓮𝓲𝓼 𝓮𝓶 𝓷𝓸𝓼𝓼𝓸 𝓼𝓲𝓼𝓽𝓮𝓶𝓪 ~~~~~~\n")
        
        for marca in carros: #IRÁ PERCORRER TODAS AS MARCAS DE CARROS DISPONIVEIS DENTRO DO DICIONARIO (CARROS) E PRINTAR ELAS
            print(marca)

        marca = input ("\nESCOLHA QUAL A MARCA DO  VEÍCULO QUE DESEJA ADQUIRIR: ")
        
        print(" ") #ESPAÇO

        print(carros[marca]) #IRÁ MOSTRAR TODOS OS CARROS DENTRO DA MARCA ESCOLHIDA PELO USUÁRIO
            
        escolha = str (input("\nAGORA DIGITE QUAL DOS MODELOS DESEJA ADQUIRIR: "))
        
        if escolha in carros[marca] : #FAZ A VERIFICAÇÃO SE O CARRO ESCOLHIDO PELO CLIENTE ESTÁ DISPONIVEL NO SISTEMA
            
           taxa = fipe[escolha] * 0.25
           valorvenda = fipe[escolha] + taxa
        
           print(f"O valor do carro {escolha} desejado é de R${valorvenda}")
        
           fecharnegocio = str (input ("DESEJA FECHAR NEGÓCIO? (S)/(N): ")).lower()
        
           if fecharnegocio == "s" : #CONDIÇÃO CASO O CLIENTE ACEITE FECHAR NEGÓCIO
              if saldo < valorvenda : #CONDIÇÃO DO SALDO DO CLIENTE PARA CASO ELE NÃO POSSUA O SUFICIENTE PARA ADQUIRIR O VEÍCULO
                 print("Negócio cancelado, saldo insuficiente.")
                
                 
                
              else : #CASO POSSUA SALDO
                  
                  x = saldo - valorvenda
                  print("Veículo vendido. \nParabéns ao cliente pela sua nova aquisição.")
                  print(f"O saldo do cliente é de R${x:.2f}")
                  carros[marca].remove(escolha) #REMOVE O INTEM ESCOLHIDO PELO CLIENTE DO SISTEMA
                
        
        
           elif fecharnegocio == "n" : #CONDIÇÃO CASO O USUÁRIO NÃO ACEITE FECHAR NEGÓCIO
                print("Negócio cancelado.\nObrigado por usar nosso sistema.")
             
                
                
           else : #CONDIÇÃO CASO O USUÁRIO DIGITE UMA LETRA DIFERENTE DE (S) OU (N)
               
                print("ERRO, NOT FOUND.")
               
               
        else : #CONDIÇÃO PARA CASO O CARRO ESCOLHIDO NÃO ESTEJA MAIS NO ESTOQUE
            print("\nCarro não está mais disponível em nossa concessionária.\n")
            
            continue
        
        
    elif option == 3 : #OPÇÃO RESERVADA PARA LOJA ALUGAR UM VEICULO A UM CLIENTE
         print("\n~~~~~~ 𝓐𝓵𝓾𝓰𝓾𝓮𝓲𝓼 𝓭𝓮 𝓬𝓪𝓻𝓻𝓸𝓼 ~~~~~~\n")
         
         print(carros)  
         
         print("\n~~~~~~ 𝓐𝓵𝓾𝓰𝓾𝓮𝓲𝓼 𝓭𝓮 𝓬𝓪𝓻𝓻𝓸𝓼 ~~~~~~\n")
         
         for marca in carros: #IRÁ PERCORRER TODAS AS MARCAS DE CARROS DISPONIVEIS DENTRO DO DICIONARIO (CARROS) E PRINTAR ELAS
            print(marca)

         marca = input ("\nESCOLHA QUAL A MARCA DO  VEÍCULO QUE DESEJA ALUGAR: ")
             
         print(" ")

         print(carros[marca]) #IRÁ MOSTRAR TODOS OS CARROS DENTRO DA MARCA ESCOLHIDA PELO USUÁRIO
            
         escolha = str (input("\nAGORA DIGITE QUAL DOS MODELOS DESEJA ADQUIRIR: "))   
             
         if escolha in carros[marca] : #FAZ A VERIFICAÇÃO SE O CARRO ESCOLHIDO PELO CLIENTE ESTÁ DISPONIVEL NO SISTEMA
             
             diaria = int (input ("\nDIGITE A QUANTIDADE DE DIAS QUE DESEJA ALUGAR O CARRO: "))
             
             aluguel = 1500 * diaria
             
             print(f"O valor do aluguel do {escolha} irá custar R${aluguel:.2f} durante {diaria} dias.")
             fecharnegocio = str (input ("DESEJA FECHAR NEGÓCIO? (S)/(N): ")).lower()
             
             if fecharnegocio == "s" : #CONDIÇÃO CASO O CLIENTE ACEITE FECHAR NEGÓCIO
                 
                if saldo < aluguel : #CONDIÇÃO DO SALDO DO CLIENTE PARA CASO ELE NÃO POSSUA O SUFICIENTE PARA ALUGAR O VEÍCULO
                   print("Negócio cancelado, saldo insuficiente.")
                 
                else : #CONDIÇÃO CASO ELE POSSUA SALDO
                    x = saldo - aluguel
                    print(f"{escolha} Alugado com sucesso. Parabéns!")
                    print(f"O saldo do cliente é de R${x:.2f}")
                    carros[marca].remove(escolha) #REMOVE O INTEM ESCOLHIDO PELO CLIENTE DO SISTEMA
                    
             elif fecharnegocio == "n" : #CONDIÇÃO CASO O USUÁRIO NÃO ACEITE FECHAR NEGÓCIO
                  print("Negócio cancelado.\nObrigado por usar nosso sistema.")
                    
             else : #CONDIÇÃO CASO O USUÁRIO DIGITE UMA LETRA DIFERENTE DE (S) OU (N)
                 
                 print("ERRO, NOT FOUND.")
                 
                 
    elif option == 4 : #ENCERRA O PROGRAMA
        print("Programa finalizado com sucesso.")
        break
    
    
    
    else : #CASO O USUARIO DIGITE UM NUMERO DIFERENTE DAS OPÇÕES
        print("ERRO, NOT FOUND.")
        
        break
