opcao = 1

while opcao != 0 :
    
    print("\n~~~~~MENU OPÇÕES ~~~~~~\n")
    print("(0)  - SAIR")
    print("(1)  - CADASTRO DE LIVROS")
    print("(2)  - CONSULTA DE LIVROS DISPONIVEIS")
    print("(3)  - EMPRÉSTIMO DE LIVROS")
    print("(4)  - DEVOLUÇÃO DE LIVROS")
    print("(5)  - LIVROS CADASTRADOS NO SISTEMA\n")
 
    opcao = int(input("\nDIGITE O NÚMERO DA OPÇÃO QUE DESEJA ACESSAR: ")) 


    match opcao :
        
        case 1 : #Aqui será feito o cadastro dos livros no sistema.
            print(" ")

            titulo1 = str (input ("INFORME O TÍTULO DO LIVRO QUE DESEJA CADASTRAR: "))
            autor1 = str (input ("INFORME O NOME DO AUTOR DO LIVRO: "))
            anopublicacao1 = int (input ("DIGITE O ANO DE PUBLICAÇÂO DO LIVRO: "))
            livro1 = 1

            print(" ")

            titulo2 = str (input ("INFORME O TÍTULO DO LIVRO QUE DESEJA CADASTRAR: "))
            autor2 = str (input ("INFORME O NOME DO AUTOR DO LIVRO: "))
            anopublicacao2 = int (input ("DIGITE O ANO DE PUBLICAÇÂO DO LIVRO: "))
            livro2 = 1
            
            print(" ")

            titulo3 = str (input ("INFORME O TÍTULO DO LIVRO QUE DESEJA CADASTRAR: "))
            autor3 = str (input ("INFORME O NOME DO AUTOR DO LIVRO: "))
            anopublicacao3 = int (input ("DIGITE O ANO DE PUBLICAÇÂO DO LIVRO: "))
            livro3 = 1
            
            print(" ")

            titulo4 = str (input ("INFORME O TÍTULO DO LIVRO QUE DESEJA CADASTRAR: "))
            autor4 = str (input ("INFORME O NOME DO AUTOR DO LIVRO: "))
            anopublicacao4 = int (input ("DIGITE O ANO DE PUBLICAÇÂO DO LIVRO: "))
            livro4 = 1
            
            print(" ")

            titulo5 = str (input ("INFORME O TÍTULO DO LIVRO QUE DESEJA CADASTRAR: "))
            autor5 = str (input ("INFORME O NOME DO AUTOR DO LIVRO: "))
            anopublicacao5 = int (input ("DIGITE O ANO DE PUBLICAÇÂO DO LIVRO: "))
            livro5 = 1



        case 2 : # Mostra todos os livros disponíveis e indisponíveis cadastrados no sistema.
            
            print("\n~~~~~~ LIVROS DISPONIVEIS/INDISPONIVEIS NO SISTEMA ~~~~~~\n")

            if livro1 == 0 :
                print(f"O LIVRO [{titulo1}] NÃO ESTÁ DISPONÍVEL PARA EMPRÉSTIMO")
                
                
            else :
                print(f"O LIVRO [{titulo1}] ESTÁ DISPONÍVEL PARA EMPRÉSTIMO")
                
                
                
                
            if livro2 == 0 :
                print(f"O LIVRO [{titulo2}] NÃO ESTÁ DISPONÍVEL PARA EMPRÉSTIMO")

                
            else :
                print(f"O LIVRO [{titulo2}] ESTÁ DISPONÍVEL PARA EMPRÉSTIMO")
                
                
                
                
            if livro3 == 0 :
                print(f"O LIVRO [{titulo3}] NÃO ESTÁ DISPONÍVEL PARA EMPRÉSTIMO")
                
                                       
            else :
                print(f"O LIVRO [{titulo3}] ESTÁ DISPONÍVEL PARA EMPRÉSTIMO")
                
                
                    
                
            if livro4 == 0 :
                print(f"O LIVRO [{titulo4}] NÃO ESTÁ DISPONÍVEL PARA EMPRÉSTIMO")
                
                
            else :
                print(f"O LIVRO [{titulo4}] ESTÁ DISPONÍVEL PARA EMPRÉSTIMO")
                
                
                
                
            if livro5 == 0 :
                print(f"O LIVRO [{titulo5}] NÃO ESTÁ DISPONÍVEL PARA EMPRÉSTIMO")
                
                
            else :
                print(f"O LIVRO [{titulo5}] ESTÁ DISPONÍVEL PARA EMPRÉSTIMO")
                
                
            
        case 3 : # Aqui o usuário poderá solicitar um livro para pegar emprestado.
            
            print(" ")

            emprestimo = str (input ("INFORME O NOME DO LIVRO QUE DESEJA PEGAR EMPRESTADO: "))

            if emprestimo == titulo1 :
                livro1 = 0
                print(f"VOCÊ ESCOLHEU O LIVRO: [{titulo1}] PARA PEGAR EMPRESTADO.")
            
            

            elif emprestimo == titulo2 :
                livro2 =  0
                print(f"VOCÊ ESCOLHEU O LIVRO: [{titulo2}] PARA PEGAR EMPRESTADO.")
                
                
                
            elif emprestimo == titulo3 :
                livro3 =  0
                print(f"VOCÊ ESCOLHEU O LIVRO: [{titulo3}] PARA PEGAR EMPRESTADO.")
                
                
                
            elif emprestimo == titulo4 :
                livro4 =  0
                print(f"VOCÊ ESCOLHEU O LIVRO: [{titulo4}] PARA PEGAR EMPRESTADO.")
                
                
                
            elif emprestimo == titulo5 :
                livro5 =  0
                print(f"VOCÊ ESCOLHEU O LIVRO: [{titulo5}] PARA PEGAR EMPRESTADO.")
                
                

            else :
                print("ERRO, NÃO POSSUIMOS ESTE LIVRO EM NOSSA BIBLIOTECA.")

            

        case 4 : # Aqui é onde o usuário poderá deolver os livros que pegou emprestado no sistema.
            print(" ")

            devolucao = str (input ("INFORME O NOME DO LIVRO QUE DESEJA DEVOLVER: "))

            if devolucao == titulo1 :
                livro1 = 1
                print(f"LIVRO DEVOLVIDO: [{titulo1}]")
                
            elif devolucao == titulo2 :
                livro2 = 1
                print(f"LIVRO DEVOLVIDO: [{titulo1}]")
                
            elif devolucao == titulo3 :
                livro3 = 1
                print(f"LIVRO DEVOLVIDO: [{titulo1}]")
                
            elif devolucao == titulo4 :
                livro4 = 1
                print(f"LIVRO DEVOLVIDO: [{titulo1}]")
                
            elif devolucao == titulo5 :
                livro5 = 1
                print(f"LIVRO DEVOLVIDO: [{titulo1}]")
                
            else :
                print("ERRO, NÃO IDENTIFICAMOS O LIVRO QUE DESEJA DEVOLVER.")

            
                
        case 5 : # Aqui é onde será listado todos os livros cadastrados no sistema
            
            print(" ")
            print("~~~~ LIVROS CADASTRADOS EM NOSSO SISTEMA ~~~~")
            print(" ")
            
            print(f"LIVRO: {titulo1}")
            print(f"AUTOR: {autor1}")
            print(f"ANO DE PUBLICAÇÂO: {anopublicacao1}")

            print(" ")

            print(f"LIVRO: {titulo2}")
            print(f"AUTOR: {autor2}")
            print(f"ANO DE PUBLICAÇÂO: {anopublicacao2}")
            
            print(" ")

            print(f"LIVRO: {titulo3}")
            print(f"AUTOR: {autor3}")
            print(f"ANO DE PUBLICAÇÂO: {anopublicacao3}")
            
            print(" ")

            print(f"LIVRO: {titulo4}")
            print(f"AUTOR: {autor4}")
            print(f"ANO DE PUBLICAÇÂO: {anopublicacao4}")
            
            print(" ")

            print(f"LIVRO: {titulo5}")
            print(f"AUTOR: {autor5}")
            print(f"ANO DE PUBLICAÇÂO: {anopublicacao5}")

        case 0 : # Aqui é onde usuário finaliza o programa

            print("\n[PROGRAMA ENCERRADO]\n")
            
        case _ : # Caso contrário, caso o usuario tente digitar um número diferente das opções.
            print("\n[ERRO, NUMBER NOT FOUND!]\n")
            break