CAIXA = {
    "saldo": 0,
    "extrato": []
}
LIMITE_USO = 3
LIMITE_VALOR_SAQUE = 500

def extrato(operacao, valor):
    CAIXA["extrato"].append({
        "operacao": operacao,
        "valor": valor,
        "saldo": CAIXA["saldo"]
    })
    print(f"\nOperação: '{operacao}' realizada com sucesso!")

def deposito(valor):
    CAIXA["saldo"] += valor
    extrato("Depósito", valor)

def saque(valor):
    if valor < 0:
        print("Valor inválido")
        return
    
    if valor > LIMITE_VALOR_SAQUE:
        print("Valor máximo por saque é de R$ 500,00")
        return
    
    if CAIXA["saldo"] < valor:
        print("Saldo insuficiente")
        return
    
    CAIXA["saldo"] -= valor
    extrato("Saque", valor)

def get_extrato():
    mostrar_extrato(len(CAIXA["extrato"]) > 0)

def mostrar_extrato(tem_movimentacoes):
    print("\n------------------- EXTRATO -------------------")
    if not tem_movimentacoes:
        print("Nenhuma operação realizada")
    else:
        print(f"Saldo atual: R$ {CAIXA['saldo']:.2f}\n")
        for item in CAIXA["extrato"]:
            print(f"""
            Operação: {item["operacao"]}
            Valor: R$ {item["valor"]:.2f}
            Saldo: R$ {item["saldo"]:.2f}
            """)
    print("-----------------------------------------------")

cont = 0
while True:
    if(cont == LIMITE_USO):
        print("\nVocê excedeu o limite de saque diário!" +
              "Seu saldo final é de R$ {:.2f}".format(CAIXA["saldo"]))
        break

    print("""
    ----------------Menu----------------
      
    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Sair
        
    ------------------------------------
    """)

    opcao = input("Digite a opção desejada: ")
    
    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        deposito(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        saque(valor)
        cont += 1
    elif opcao == "3":
        get_extrato()
    elif opcao == "4":
        print("\nObrigado por usar o caixa eletrônico!")
        break
    else:
        print("Opção inválida")




