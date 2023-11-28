menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    print(menu)
    opcao = int(input("O que deseja fazer? "))
    if opcao == 1:
        valor = float(input("Quanto quer depositar? "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: {valor:.2f}\n"
        else:
            print("Operação inválida, tente novamente")
    elif opcao == 2:
        valor = float(input("Quanto quer sacar? "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES
        if excedeu_saldo:
            print("Operação inválida, tente novamente")
        elif excedeu_limite:
            print("Operação inválida, tente novamente")
        elif excedeu_saques:
            print("Operação inválida, tente novamente")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: {valor:.2f}\n"
            numero_de_saques += 1
        else:
            print("Operação inválida, tente novamente")
    elif opcao == 3:
        print("\nExtrato:")
        print(f"\nSaldo: {saldo:.2f}")
        print("")
        print(extrato)
       
        print("Não foram feitas movimentações este mes:" if not  extrato else extrato)
    else:
        print("Saindo................................................................")
        break