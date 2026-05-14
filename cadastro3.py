import os

while True:

    print("\n===== SISTEMA =====")
    print("1 - Escola")
    print("2 - Hospital")
    print("3 - Empresa")
    print("4 - Biblioteca")
    print("0 - Sair")

    escolha = input("Escolha um banco de dados: ")

    # ESCOLHA DO ARQUIVO

    if escolha == "1":
        arquivo = "escola.txt"
        tipo = "Aluno"

    elif escolha == "2":
        arquivo = "hospital.txt"
        tipo = "Paciente"

    elif escolha == "3":
        arquivo = "empresa.txt"
        tipo = "Funcionário"

    elif escolha == "4":
        arquivo = "biblioteca.txt"
        tipo = "Leitor"

    elif escolha == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")
        continue

    # MENU INTERNO

    while True:

        print(f"\n===== {tipo.upper()} =====")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Editar")
        print("5 - Excluir")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        # CADASTRAR

        if opcao == "1":

            id_pessoa = input(f"Digite o ID do {tipo}: ")
            nome = input(f"Digite o nome do {tipo}: ")

            telefone = input("Digite o telefone: ")

            with open(arquivo, "a") as arq:
                arq.write(f"{id_pessoa};{nome};{telefone}\n")

            print(f"{tipo} cadastrado com sucesso!")

        # LISTAR

        elif opcao == "2":

            print(f"\n===== LISTA DE {tipo.upper()}S =====")

            if not os.path.exists(arquivo):
                print("Nenhum cadastro encontrado.")

            else:

                with open(arquivo, "r") as arq:

                    linhas = arq.readlines()

                    if len(linhas) == 0:
                        print("Nenhum cadastro encontrado.")

                    else:

                        for linha in linhas:

                            dados = linha.strip().split(";")

                            if len(dados) == 3:

                                id_pessoa, nome, telefone = dados

                                print(f"""
ID: {id_pessoa}
Nome: {nome}
Telefone: {telefone}
-------------------------
""")

        # BUSCAR

        elif opcao == "3":

            busca = input("Digite o ID para buscar: ")

            encontrado = False

            if os.path.exists(arquivo):

                with open(arquivo, "r") as arq:

                    for linha in arq:

                        dados = linha.strip().split(";")

                        if len(dados) == 3:

                            id_pessoa, nome, telefone = dados

                            if id_pessoa == busca:

                                encontrado = True

                                print(f"""
ID: {id_pessoa}
Nome: {nome}
Telefone: {telefone}
""")

            if not encontrado:
                print("Cadastro não encontrado.")

        # EDITAR

        elif opcao == "4":

            busca = input("Digite o ID para editar: ")

            novas_linhas = []
            encontrado = False

            if os.path.exists(arquivo):

                with open(arquivo, "r") as arq:

                    linhas = arq.readlines()

                    for linha in linhas:

                        dados = linha.strip().split(";")

                        if len(dados) == 3:

                            id_pessoa, nome, telefone = dados

                            if id_pessoa == busca:

                                encontrado = True

                                print("Cadastro encontrado!")

                                nome = input("Novo nome: ")
                                telefone = input("Novo telefone: ")

                            novas_linhas.append(f"{id_pessoa};{nome};{telefone}\n")

                with open(arquivo, "w") as arq:
                    arq.writelines(novas_linhas)

            if encontrado:
                print("Cadastro atualizado!")
            else:
                print("Cadastro não encontrado.")

        # EXCLUIR

        elif opcao == "5":

            busca = input("Digite o ID para excluir: ")

            novas_linhas = []
            encontrado = False

            if os.path.exists(arquivo):

                with open(arquivo, "r") as arq:

                    linhas = arq.readlines()

                    for linha in linhas:

                        dados = linha.strip().split(";")

                        if len(dados) == 3:

                            id_pessoa, nome, telefone = dados

                            if id_pessoa != busca:
                                novas_linhas.append(linha)
                            else:
                                encontrado = True

                with open(arquivo, "w") as arq:
                    arq.writelines(novas_linhas)

            if encontrado:
                print("Cadastro excluído!")
            else:
                print("Cadastro não encontrado.")

        # VOLTAR

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")
