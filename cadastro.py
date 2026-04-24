for i in range(3):
    print(f"\nCadastro do aluno {i+1}")

    id_aluno = input("Digite o ID do aluno: ")
    nome = input("Digite o nome do aluno: ")

    while True:
        matricula = input("Digite a matrícula (5 dígitos): ")
        if matricula.isdigit() and len(matricula) == 5:
            break
        else:
            print("Erro! A matrícula deve ter exatamente 5 números.")

    turma = input("Digite a turma: ")

    with open("alunos.txt", "a") as arquivo:
        arquivo.write(f"ID: {id_aluno} | ")
        arquivo.write(f"Nome: {nome} | ")
        arquivo.write(f"Matrícula: {matricula} | ")
        arquivo.write(f"Turma: {turma}\n")
        
print("\n Os 3 alunos foram cadastrados com sucesso!")
