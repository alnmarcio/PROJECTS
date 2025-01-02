opcao = 1

while opcao != 0 :
    
    print("\n~~~~~MENU OPÇÕES ~~~~~~\n") # OPÇOES DE ACESSO
    print("(0)  - SAIR")
    print("(1)  - CADASTRO DE HÓSPEDES")
    print("(2)  - CONSULTA DE QUARTOS DISPONIVEIS")
    print("(3)  - REGISTRO DE ENTRADA DE HÓSPEDES")
    print("(4)  - REGISTRO DE SAÍDA DE HÓSPEDES")
    print("(5)  - LISTAGEM DE HÓSPEDES CADASTRADOS\n")
 
    opcao = int(input("\nDIGITE O NÚMERO DA OPÇÃO QUE DESEJA ACESSAR: ")) 
    
    match opcao :
        
        case 1 : # Aqui é onde será feito o cadastro dos hóspedes
            print(" ")
            
            nome1 = str (input ("DIGITE O NOME DO HÓSPEDE: "))
            numeroquarto1 = int (input ("DIGITE O NÚMERO DO QUARTO DO HÓSPEDE: "))
            dataentrada1 = (input ("DIGITE A DATA DE ENTRADA DO HÓSPEDE: "))
            datasaida1 = (input ("DIGITE A DATA DE ENTRADA DO HÓSPEDE: "))
            hospede1 = 0
            
            print(" ")
            
            nome2 = str (input ("DIGITE O NOME DO HÓSPEDE: "))
            numeroquarto2 = int (input ("DIGITE O NÚMERO DO QUARTO DO HÓSPEDE: "))
            dataentrada2 =  (input ("DIGITE A DATA DE ENTRADA DO HÓSPEDE: "))
            datasaida2 =  (input ("DIGITE A DATA DE ENTRADA DO HÓSPEDE: "))
            hospede2 = 0
            
            print(" ")
            
            nome3 = str (input ("DIGITE O NOME DO HÓSPEDE: "))
            numeroquarto3 = int (input ("DIGITE O NÚMERO DO QUARTO DO HÓSPEDE: "))
            dataentrada3 =  (input ("DIGITE A DATA DE ENTRADA DO HÓSPEDE: "))
            datasaida3 =  (input ("DIGITE A DATA DE ENTRADA DO HÓSPEDE: "))
            hospede3 = 0

            print(" ")
            
            nome4 = str (input ("DIGITE O NOME DO HÓSPEDE: "))
            numeroquarto4 = int (input ("DIGITE O NÚMERO DO QUARTO DO HÓSPEDE: "))
            dataentrada4 =  (input ("DIGITE A DATA DE ENTRADA DO HÓSPEDE: "))
            datasaida4 =  (input ("DIGITE A DATA DE ENTRADA DO HÓSPEDE: "))
            hospede4 = 0

            print(" ")
            
            nome5 = str (input ("DIGITE O NOME DO HÓSPEDE: "))
            numeroquarto5 = int (input ("DIGITE O NÚMERO DO QUARTO DO HÓSPEDE: "))
            dataentrada5 =  (input ("DIGITE A DATA DE ENTRADA DO HÓSPEDE: "))
            datasaida5 =  (input ("DIGITE A DATA DE ENTRADA DO HÓSPEDE: "))
            hospede5 = 0
            
            
            
        case 2 : # AQUI É ONDE IRA MOSTRAR A DISPONIBILIDADE DE TODOS OS QUARTOS, SE ESTAO OU NAO DISPONIVEIS
            
            if hospede1 == 1 :
                print(f"\nO QUARTO [{numeroquarto1}] NÃO ESTÁ DISPONÍVEL.")
                
            else :
                print(f"O QUARTO [{numeroquarto1}] ESTÁ DISPONÍVEL.")
                
            
            
            if hospede2 == 1 :
                print(f"O QUARTO [{numeroquarto2}] NÃO ESTÁ DISPONÍVEL.")
                
            else :
                print(f"O QUARTO [{numeroquarto2}] ESTÁ DISPONÍVEL.")


            
            if hospede3 == 1 :
                print(f"O QUARTO [{numeroquarto3}] NÃO ESTÁ DISPONÍVEL.")
                
            else :
                print(f"O QUARTO [{numeroquarto3}] ESTÁ DISPONÍVEL.")



            if hospede4 == 1 :
                print(f"O QUARTO [{numeroquarto4}] NÃO ESTÁ DISPONÍVEL.")
                
            else :
                print(f"O QUARTO [{numeroquarto4}] ESTÁ DISPONÍVEL.")



            if hospede5 == 1 :
                print(f"O QUARTO [{numeroquarto5}] NÃO ESTÁ DISPONÍVEL.")
                
            else :
                print(f"O QUARTO [{numeroquarto5}] ESTÁ DISPONÍVEL.")
                
                
                
                
                
        case 3 : # Aqui é onde será feito o check-in do cliente cadastrado
            print("\n~~~~~~ CHECK-IN ~~~~~~\n")
            
            quartocheckin = int (input ("DIGITE O NUMERO DO QUARTO DO HÓSPEDE QUE DESEJA REALIZAR O CHECK-IN: "))
            
            if quartocheckin == numeroquarto1 :
                hospede1 = 1
                print(f"\nCHECK-IN DO HÓSPEDE [{nome1}] REALIZADO COM SUCESSO.")
                
                
                
            elif quartocheckin == numeroquarto2 :
                hospede2 = 1
                print(f"\nCHECK-IN DO HÓSPEDE [{nome2}] REALIZADO COM SUCESSO.")



            elif quartocheckin == numeroquarto3 :
                hospede3 = 1
                print(f"\nCHECK-IN DO HÓSPEDE [{nome3}] REALIZADO COM SUCESSO.")



            elif quartocheckin == numeroquarto4 :
                hospede4 = 1
                print(f"\nCHECK-IN DO HÓSPEDE [{nome4}] REALIZADO COM SUCESSO.")


            elif quartocheckin == numeroquarto5 :
                hospede5 = 1
                print(f"\nCHECK-IN DO HÓSPEDE [{nome5}] REALIZADO COM SUCESSO.")


            else :
                print("[ERRO]")
            
            
  
            
            
        case 4 : # AQUI É ONDE SERA FEITO O CHECKOUT DO CLIENTE CASO ELE ESTEJA DE SAÍDA 
            print("\n~~~~~~ CHECK-OUT ~~~~~~\n")
            
            quartocheckout = int (input("DIGITE O NUMERO DO QUARTO DO HÓSPEDE QUE DESEJA REALIZAR O CHECK-OUT: "))
            
            if quartocheckout == numeroquarto1 :
                hospede1 = 0
                print(f"\nCHECK-OUT DO HÓSPEDE [{nome1}] REALIZADO COM SUCESSO.")
                
                
                
            elif quartocheckout == numeroquarto2 :
                hospede2 = 0
                print(f"\nCHECK-OUT DO HÓSPEDE [{nome2}] REALIZADO COM SUCESSO.")


            elif quartocheckout == numeroquarto3 :
                hospede2 = 0
                print(f"\nCHECK-OUT DO HÓSPEDE [{nome3}] REALIZADO COM SUCESSO.")


            elif quartocheckout == numeroquarto4 :
                hospede2 = 0
                print(f"\nCHECK-OUT DO HÓSPEDE [{nome4}] REALIZADO COM SUCESSO.")


            elif quartocheckout == numeroquarto5 :
                hospede2 = 0
                print(f"\nCHECK-OUT DO HÓSPEDE [{nome5}] REALIZADO COM SUCESSO.")


            else :
                print("[ERRO]")
            
            
            
            
        case 5 : # TODOS OS HOSPEDES CADASTTRADOS NO SISTEMA
            print("\n~~~~~~ HÓSPEDES CADASTRADOS NO SISTEMA ~~~~~~\n")
            
            print(f"NÚMERO DO QUARTO: [{numeroquarto1}]")
            print(f"NOME DO HÓSPEDE: [{nome1}]")
            print(f"DATA DE ENTRADA DO HÓSPEDE: [{dataentrada1}]")
            print(f"DATA DE ENTRADA DO SAÍDA DO HÓSPEDE: [{dataentrada1}]")
            
            print(" ")
            
            print(f"NÚMERO DO QUARTO: [{numeroquarto2}]")
            print(f"NOME DO HÓSPEDE: [{nome2}]")
            print(f"DATA DE ENTRADA DO HÓSPEDE: [{dataentrada2}]")
            print(f"DATA DE ENTRADA DO SAÍDA DO HÓSPEDE: [{dataentrada2}]")

            print(" ")
            
            print(f"NÚMERO DO QUARTO: [{numeroquarto3}]")
            print(f"NOME DO HÓSPEDE: [{nome3}]")
            print(f"DATA DE ENTRADA DO HÓSPEDE: [{dataentrada3}]")
            print(f"DATA DE ENTRADA DO SAÍDA DO HÓSPEDE: [{dataentrada3}]")

            print(" ")
            
            print(f"NÚMERO DO QUARTO: [{numeroquarto4}]")
            print(f"NOME DO HÓSPEDE: [{nome4}]")
            print(f"DATA DE ENTRADA DO HÓSPEDE: [{dataentrada4}]")
            print(f"DATA DE ENTRADA DO SAÍDA DO HÓSPEDE: [{dataentrada4}]")

            print(" ")
            
            print(f"NÚMERO DO QUARTO: [{numeroquarto5}]")
            print(f"NOME DO HÓSPEDE: [{nome5}]")
            print(f"DATA DE ENTRADA DO HÓSPEDE: [{dataentrada5}]")
            print(f"DATA DE ENTRADA DO SAÍDA DO HÓSPEDE: [{dataentrada5}]")
            
        case 0 : #ENCERRA O PROGRAMA
            print("\n[FIM PROGRAMA]")
            
            
            
            
        case _ : #Caso contrário, caso o usuario tente digitar um número diferente das opções.
            print("\n[ERRO]")
            break
            
                
            