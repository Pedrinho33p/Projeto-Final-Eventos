
def entrar():
    while True:
        print("-" * 30)
        print("        *** ENTRAR ***")
        print("-" * 30)
        escolha = input("\n--- Cadastrar-se ou Fazer Login ---\n[1] Para fazer Login\n[2] Para se cadastrar\n------> ").strip()

        if escolha == "1":
            fazer_login()
            break  
        elif escolha == "2":
            cadastrado = cadastrar_usuario()
            if cadastrado:
                inicio()
                break  
        else:
            print("Número inválido! Tente novamente.")


def inicio():
    print()
    print("-"*30)
    print("*** Bem Vindo a JG Eventos ***")
    print("-"*30)
    home = input("\nO que você deseja?\n[1] Para ver a Lista de eventos!\n[2] Para Procurar por um evento!\n[3] Para comprar um ingresso! \n------> ").lower()
    if home == "1":
        lista(eventos)
    elif home == "2":
        procurar(eventos)
    elif home == "3":
        fazer_reserva()
    else:
        print("Opção Invalida!")



def fazer_login():
    while True:
        print()
        print("-" * 30)
        print("        *** Login ***")
        print("-" * 30)
        email_login = input("\nDigite seu email: ").strip().lower()

        if email_login in usuario:
            senha_login = input("Digite sua senha: ").strip()
            if usuario[email_login]["senha"] == senha_login:
                print("Login realizado com sucesso!")
                inicio()
                return True
            else:
                print("Senha incorreta. Tente novamente.\n")
        else:
            print("\nERRO: \nEmail não cadastrado. Tente novamente.\n")


def validar_senha(senha):
    if len(senha) <= 7:
        print("Senha deve ter pelo menos 8 caracteres.")
        return False

    tem_letra = any(c.isalpha() for c in senha)
    if not tem_letra:
        print("Senha deve conter pelo menos uma letra.")
        return False

    tem_numero = any(c.isdigit() for c in senha)
    if not tem_numero:
        print("Senha deve conter pelo menos um número.")
        return False
    
    return True


def cadastrar_usuario():
    print()
    nome = input("Digite seu nome: ").strip()
    email = input("Digite seu email: ").strip().lower()
    
    if email in usuario:
        print("Este email já está cadastrado.")
        return False
    
    while True:
        senha = input("Digite sua senha: ").strip()
        if validar_senha(senha):
            break
        else:
            print("Tente novamente.")
    
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            break
        except ValueError:
            print("Por favor, digite um número válido para a idade.")
    
    usuario[email] = {
        "nome": nome,
        "senha": senha,
        "idade": idade
    }
    print("\nUsuário cadastrado com sucesso!")
    return True


def lista(eventos):
    print()
    print("-" * 31)
    print("*** Lista de Eventos ***")
    print("-" * 31)
    for nome, detalhes in eventos.items():
        print()
        print("-" * 31)
        print("*** Evento ***")
        print("-" * 31)
        print("Informações do Evento:")
        print(f"Nome: {nome}")
        print(f"Data: {detalhes['data']}")
        print(f"Hora: {detalhes['hora']}")
        print(f"Local: {detalhes['local']}")
        print(f"Descrição: {detalhes['desc']}")
        print(f"Idade mínima: {detalhes['idade_minima']}")
        print(f"Preço: {detalhes['preço_mostrar']}")
        print("-" * 40)
        fazer_reserva()


def procurar(eventos):
    search = input("Como você deseja procurar por um evento? \n[1] Para procurara pelo NOME \n[2] Para procurara pela DATA  \n[3] Para procurara pela HORA  \n[4] Para procurara pelo LOCAL  \n[5] Para procurar pela IDADE\n[6] Para procurar por um PREÇO\n[7] Para VOLTAR \n------> ").lower()
    if search == "1":
        info_evento_nome()
    if search == "2":
        info_evento_data()
    if search == "3":
        info_evento_hora()
    if search == "4":
        info_evento_local()
    if search == "5":
        info_evento_idade()
    if search == "6":
        info_evento_preco()
    if search == "7":
        inicio()


def info_evento_nome():
    nome_evento = input("Digite o nome do evento (Sair para voltar): ").strip()
    if nome_evento == "sair":
        procurar(eventos)
    encontrados = False
    
    if nome_evento in eventos:
        evento = eventos[nome_evento]
        print()
        print("-"*31)
        print("*** Evento ***")
        print("-"*31)
        print("\nInformações do Evento:")
        print(f"Nome: {nome_evento}")
        print(f"Data: {'data'}")
        print(f"Hora: {'hora'}")
        print(f"Local: {'local'}")
        print(f"Descrição: {'desc'}")
        print(f"Idade mínima: {'idade_minima'}")
        print(f"Preço: {'preço_mostrar'}")
        encontrados = True
    else:
        print("Evento não encontrado.")


def info_evento_data():
    data_evento = input("Digite a data do evento (dd/mm/aaaa) (Sair para voltar): ").strip()
    if data_evento == "sair":
        procurar(eventos)
    encontrados = False
    
    for nome_evento, info in eventos.items():
        if info["data"] == data_evento:
            print()
            print("-"*31)
            print("*** Evento ***")
            print("-"*31)
            print("\nInformações do Evento:")
            print(f"Nome: {nome_evento}")
            print(f"Data: {info['data']}")
            print(f"Hora: {info['hora']}")
            print(f"Local: {info['local']}")
            print(f"Descrição: {info['desc']}")
            print(f"Idade mínima: {info['idade_minima']}")
            print(f"Preço: {info['preço_mostrar']}")
            encontrados = True
    
    if not encontrados:
        print("Nenhum evento encontrado para essa data.")


def info_evento_hora():
    hora_evento = input("Digite a hora do evento (hh:mm) (Sair para voltar): ").strip()
    if hora_evento == "sair":
        procurar(eventos)
    encontrados = False

    for nome_evento, info in eventos.items():
        if info["hora"] == hora_evento:
            print()
            print("-"*31)
            print("*** Evento ***")
            print("-"*31)
            print("\nInformações do Evento:")
            print(f"Nome: {nome_evento}")
            print(f"Data: {info['data']}")
            print(f"Hora: {info['hora']}")
            print(f"Local: {info['local']}")
            print(f"Descrição: {info['desc']}")
            print(f"Idade mínima: {info['idade_minima']}")
            print(f"Preço: {info['preço_mostrar']}")
            encontrados = True

    if not encontrados:
        print("Nenhum evento encontrado para essa hora.")


def info_evento_local():
    local_evento = input("Digite o local do evento (Sair para voltar): ").strip()
    if local_evento == "sair":
        procurar(eventos)
    encontrados = False

    for nome_evento, info in eventos.items():
        if info["local"] == local_evento:
            print()
            print("-"*31)
            print("*** Evento ***")
            print("-"*31)
            print("\nInformações do Evento:")
            print(f"Nome: {nome_evento}")
            print(f"Data: {info['data']}")
            print(f"Hora: {info['hora']}")
            print(f"Local: {info['local']}")
            print(f"Descrição: {info['desc']}")
            print(f"Idade mínima: {info['idade_minima']}")
            print(f"Preço: {info['preço_mostrar']}")
            encontrados = True

    if not encontrados:
        print("Nenhum evento encontrado para essa hora.")


def info_evento_idade():
    idade_evento = input("Digite a idade minima do evento (Sair para voltar): ").strip()
    if idade_evento == "sair":
        procurar(eventos)
    encontrados = False

    for nome_evento, info in eventos.items():
        if info["idade_minima"] == idade_evento:
            print()
            print("-"*31)
            print("*** Evento ***")
            print("-"*31)
            print("\nInformações do Evento:")
            print(f"Nome: {nome_evento}")
            print(f"Data: {info['data']}")
            print(f"Hora: {info['hora']}")
            print(f"Local: {info['local']}")
            print(f"Descrição: {info['desc']}")
            print(f"Idade mínima: {info['idade_minima']}")
            print(f"Preço: {info['preço_mostrar']}")
            encontrados = True

    if not encontrados:
        print("Nenhum evento encontrado para essa idade.")


def info_evento_preco():
    try:
        preco_max = float(input("Digite o preço máximo que deseja pagar (0 para voltar): ").strip())
        if preco_max == 0:
                procurar(eventos)
    except ValueError:
        print("Por favor, digite um valor numérico válido.")
        return

    encontrados = False

    for nome_evento, info in eventos.items():
        preco_evento = float(info["preço"])
        if preco_evento == "sair":
            procurar(eventos)
        if preco_evento <= preco_max:
            print()
            print("-"*31)
            print("*** Evento ***")
            print("-"*31)
            print("\nInformações do Evento:")
            print(f"Nome: {nome_evento}")
            print(f"Data: {info['data']}")
            print(f"Hora: {info['hora']}")
            print(f"Local: {info['local']}")
            print(f"Descrição: {info['desc']}")
            print(f"Idade mínima: {info['idade_minima']}")
            print(f"Preço: {info['preço_mostrar']}")
            encontrados = True

    if not encontrados:
        print("Nenhum evento encontrado dentro do preço informado.")


#--------- Parte da RESERVA -------#


def fazer_reserva():
     while True:
        desejo = int(input("Deseja fazer uma reserva? \n[1] Para SIM \n[2] Para NÃO \n------>"))
        if desejo == '1':
            marcar()
            break
        elif desejo == '2':
            inicio()
            break
        else:
            print("Resposta inválida. Digite '1' para sim ou '2' para não.")


def marcar():
    marcar = input("Qual evento deseja reservar?: ")
    if marcar in eventos:
        evento = eventos[marcar]
        print()
        print("-" * 31)
        print(" *** Informações do Evento ***")
        print("-" * 31)
        print(f"\nNome: {marcar}")
        print(f"Data: {evento['data']}")
        print(f"Hora: {evento['hora']}")
        print(f"Local: {evento['local']}")
        print(f"Descrição: {evento['desc']}")
        print(f"Idade mínima: {evento['idade_minima']}")
        print(f"Preço dos ingressos: {evento['preço_mostrar']}")
        
        inteira = int(input("\nQuantidade de ingressos inteiros: "))
        meia = int(input("Quantidade de ingressos meia-entrada: "))
        
        preco_inteira = evento["preço"]
        preco_meia = preco_inteira / 2
        
        total = (inteira * preco_inteira) + (meia * preco_meia)
        print(f"\nPreço total: R${total:.2f}")
        finalizar_compra(total)
    else:
        print("Evento não encontrado.")


#--------- Parte do PAGAMENTO SIMULADO -------#


def finalizar_compra(total):
    print()
    print("-" * 31)
    print(" *** Finzalizar Pedido ***")
    print("-" * 31)
    print(f"Valor do pedido: {total}")
    finalizar = input("Finalizar o pedido? \n[1] Para SIM \n[2] Para NÃO\n------>")
    if finalizar == "1":
        forma_pagamento()
    elif finalizar == "2":
        print("Pedido CANCELADO!!!")
        inicio()
    else:
        print("Digite um número valido!")
        finalizar_compra(total)


def forma_pagamento():
    forma = input("Qual a forma de pagamento?\n[1] Cartão de CRÉDITO\n[2] Cartão de DÉBITO\n[3] Cartão PRESENTE\n[4] PIX\n[5] BOLETO\n[6] Para VOLTAR\n")
    if forma == "1":
        pass
    elif forma == "2":
        pass
    elif forma == "3":
        pass
    elif forma == "4":
        pass
    elif forma == "5":
        pass
    elif forma == "6":
        pass
    else:
        print("Digite um número valido!")
        forma_pagamento()


usuario = {
    "admin": {
        "nome": "admin",
        "senha": "1234567adm",
        "idade": 18
    }
}


eventos = {
    "PucPR": {
        "data": "12/12/2025",
        "hora": "20:20",
        "local": "PucPR",
        "desc": "Evento da PucPR",
        "idade_minima": "3 Períodos completos",
        "preço_mostrar": "0",
        "preço": 0,
        "meia": 0
    },
    "Jogo do Coritiba": {
        "data": "15/06/2025",
        "hora": "16:00",
        "local": "Coxa Sports Bar & Parrilla",
        "desc": "Jogo do Coritiba pela Série B 2025, contra o Cuiabá",
        "idade_minima": "5 anos",
        "preço_mostrar": "100 inteira - 50 meia",
        "preço": 100,
        "meia": "50"
    },
    "Jogo do Brasil": {
        "data": "10/06/2025",
        "hora": "21:45",
        "local": "Neo Quimica Arena",
        "desc": "Brasil x Paragaui nas eliminatórias da Copa do Mundo",
        "idade_minima": "Livre",
        "preço_mostrar": "400 inteira - 200 meia",
        "preço": 400,
        "meia": 200
    }
}


entrar()