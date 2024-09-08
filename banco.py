import textwrap


def menu():
    menu = """\n
    ======= MENU =======
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q]  Sair
    >>> """
    return input(textwrap.dedent(menu))


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("\nOperação falhou! O valor do saque excedeu o limite.")
    elif numero_saques >= limite_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    print("-----------------------------------")
    return saldo, extrato


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    print("-----------------------------------")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n==================== EXTRATO ====================")
    print("Não foram realizados movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=================================================")


def criar_usuario(usuarios):
    cpf = input("\nInforme o CPF (comente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        print("-----------------------------------")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\nUsuário criado com sucesso!")
    print("-----------------------------------")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\nInforme o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        print("-----------------------------------")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, o fluxo de criação de conta encerrado!")
    print("-----------------------------------")


def listar_contas(contas):
    for conta in contas:
        linha = f"""        
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print()
        print("=" * 60)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("\nInforme o valor do depósito: ")) 
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("\nInforme o valor do saque: "))
            valor, extrato = sacar(saldo=saldo,
                                   valor=valor,
                                   extrato=extrato,
                                   limite=limite,
                                   numero_saques=numero_saques,
                                   limite_saques=LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")


main()