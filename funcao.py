
import textwrap




def criar_cliente(clientes):
    cpf = input("Digite seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print("Esse CPF já está sendo usado!")
        return

    nome = input("Digite seu nome: ")
    data_nasc = input("Digite sua data de nascimento (DD-MM-AA): ")
    endereco = input("Digite seu endereço: ")

    clientes.append({
        "nome": nome,
        "data_nasc": data_nasc,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Cliente criado com sucesso!")


    

def filtrar_cliente(cpf, cliente):
   def filtrar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return None



def criar_conta(AGENCIA, numero_conta, clientes):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Usuário não encontrado.")
        return None

    print("Conta criada com sucesso!")
    return {
        "agencia": AGENCIA,
        "numero_conta": numero_conta,
        "cliente": cliente
    }








def menu():
    menu = """

[d]\t Depositar
[s]\t Sacar
[e]\t Extrato
[CRU]\t Criar usuario
[CC]\t Criar conta
[q] \t Sair
=> 
"""
    return input(textwrap.dedent(menu))

def depositar(valor, saldo, extrato, /):

    if valor > 0:
            saldo += valor
            extrato += f"Depósito:\t R$ {valor:.2f}"
            print("Operação feita com sucesso !!")
    else:
            print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(saldo, valor, extrato,limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES
    if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques excedido.")

    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: \t R$ {valor:.2f}\n"
            numero_saques += 1

    else:
            print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def mostrar_extrato(saldo,/,*, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
       



          




def Codigo_Main():
    AGENCIA = "0001"
    saldo = 0
    extrato = ""
    numero_saques = 0
    limite = 500
    LIMITE_SAQUES = 3

    clientes = []
    contas = []

    while True:
        opcao = menu().lower()

        if opcao == "d":
            valor = float(input("Valor do depósito: "))
            saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao == "s":
            valor = float(input("Valor do saque: "))
            saldo, extrato = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "cru":
            criar_cliente(clientes)

        elif opcao == "cc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, clientes)
            if conta:
                contas.append(conta)

        elif opcao == "q":
            break

        else:
            print("Opção inválida!")


Codigo_Main()