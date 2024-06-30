menu = """

    [d] Deposito
    [s] Saque
    [e] Extrato
    [q] Sair

=> """

continuar = """

Deseja continuar?

    [s] Sim
    [n] Não

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = str(input(menu))

    if opcao == "d":
        status = True
        while status:
            deposito = float(input("Informe o valor desejado para deposito: "))
            if deposito > 0:
                saldo += deposito
                extrato += f"Deposito: RS {deposito:.2f}\n"
                print(f"operação realizado com êxito, seu saldo atual é de R$ {saldo:.2f}")
                status = False
            else:
                print("Transação inválida, informe novamente o valor desejado para depoisto.")
                

    elif opcao == "s":
        status = True
        while status:
            saque = float(input("Informe o valor desejado para saque: "))
            if saque > limite:
                print("O valor desejado excede o limente de R$ 500 por saque, por gentileza, tente novamente.")
                resposta = str(input(continuar))
                if resposta == "s":
                    continue
                else:
                    status = False
            else:
                if numero_saques > LIMITE_SAQUES:
                    print("Você só pode realizar 3 saque por dia.")
                    status = False
                else:
                    if saque > saldo:
                        print("Saldo insuficiente")
                        resposta = str(input(continuar))
                        if resposta == "s":
                            continue
                        else:
                            status = False
                    else:
                        saldo -= saque
                        extrato += print(f"Saque: R$ {saque:.2f}\n")
                        print(f"Saldo atual R$: {saldo}")
                        status = False

    elif opcao == "e":
        print("\n *************** Extrato ***************")
        print("Não foram realizadas movimentações em sua conta." if not extrato else extrato)
        print(f"\n Saldo: {saldo:.2f}")
        print("\n ***************************************")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente uma operação desejada.")