#include <stdio.h>

int main() {
    int id, opcao;
    char nome[50];
    char matricula[20];

    FILE *arquivo;

    // Abre (ou cria) o arquivo em modo de anexar ("a")
    arquivo = fopen("alunos.txt", "a");

    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo!\n");
        return 1;
    }

    do {
        // Entrada de dados
        printf("\nDigite o ID do aluno: ");
        scanf("%d", &id);

        printf("Digite o nome do aluno: ");
        scanf(" %[^\n]", nome);

        printf("Digite a matricula do aluno: ");
        scanf("%s", matricula);

        fprintf(arquivo, "ID: %d\n", id);
        fprintf(arquivo, "Nome: %s\n", nome);
        fprintf(arquivo, "Matricula: %s\n", matricula);
        fprintf(arquivo, "--------------------------\n");

        printf("\nDados salvos no arquivo com sucesso!\n");

        printf("\nDeseja cadastrar outro aluno? (1 = Sim / 0 = Nao): ");
        scanf("%d", &opcao);

    } while (opcao == 1);

    fclose(arquivo);

    printf("\nPrograma encerrado.\n");

    return 0;
}

