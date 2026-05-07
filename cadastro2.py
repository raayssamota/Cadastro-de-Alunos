alunos = []

while True:

    print("\n===== SISTEMA DE ALUNOS =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Atualizar aluno")
    print("4 - Excluir aluno")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # ---------------- CADASTRAR ---------------- #

    if opcao == "1":

        id_aluno = input("Digite o ID: ")

        # Verificar ID repetido
        id_existe = False

        for aluno in alunos:
            if aluno["id"] == id_aluno:
                id_existe = True
                break

        if id_existe:
            print("Erro! ID já existe.")
            continue

        nome = input("Digite o nome: ")

        # Validar matrícula
        while True:

            matricula = input("Digite a matrícula (5 números): ")

            if not matricula.isdigit() or len(matricula) != 5:
                print("Erro! Digite exatamente 5 números.")
                continue

            matricula_existe = False

            for aluno in alunos:
                if aluno["matricula"] == matricula:
                    matricula_existe = True
                    break

            if matricula_existe:
                print("Erro! Matrícula já existe.")
            else:
                break

        turma = input("Digite a turma: ")

        aluno = {
            "id": id_aluno,
            "nome": nome,
            "matricula": matricula,
            "turma": turma
        }

        alunos.append(aluno)

        print("Aluno cadastrado com sucesso!")

    # ---------------- LISTAR ---------------- #

    elif opcao == "2":

        print("\n===== LISTA DE ALUNOS =====")

        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")

        else:

            for aluno in alunos:

                print(f"""
ID: {aluno["id"]}
Nome: {aluno["nome"]}
Matrícula: {aluno["matricula"]}
Turma: {aluno["turma"]}
-------------------------
""")

    # ---------------- ATUALIZAR ---------------- #

    elif opcao == "3":

        id_busca = input("Digite o ID do aluno: ")

        encontrado = False

        for aluno in alunos:

            if aluno["id"] == id_busca:

                encontrado = True

                print("Aluno encontrado!")

                aluno["nome"] = input("Novo nome: ")

                while True:

                    nova_matricula = input("Nova matrícula (5 números): ")

                    if nova_matricula.isdigit() and len(nova_matricula) == 5:
                        aluno["matricula"] = nova_matricula
                        break
                    else:
                        print("Erro! Digite exatamente 5 números.")

                aluno["turma"] = input("Nova turma: ")

                print("Aluno atualizado com sucesso!")
                break

        if not encontrado:
            print("Aluno não encontrado.")

    # ---------------- EXCLUIR ---------------- #

    elif opcao == "4":

        id_busca = input("Digite o ID do aluno que deseja excluir: ")

        encontrado = False

        for aluno in alunos:

            if aluno["id"] == id_busca:

                alunos.remove(aluno)

                encontrado = True

                print("Aluno excluído com sucesso!")
                break

        if not encontrado:
            print("Aluno não encontrado.")

    # ---------------- SAIR ---------------- #

    elif opcao == "0":

        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")
