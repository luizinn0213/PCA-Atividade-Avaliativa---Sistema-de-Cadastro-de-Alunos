import pandas as pd
import os

ARQUIVO = "alunos.csv"

# Criar arquivo csv
def carregar_dados():
    if os.path.exists(ARQUIVO):
        return pd.read_csv(ARQUIVO)
    else:
        return pd.DataFrame(columns=[
            "matricula", "nome", "rua", "numero", "bairro",
            "cidade", "uf", "telefone", "email"
        ])

#  Main
def menu():
    df = carregar_dados()

    while True:
        print("\n==== SISTEMA DE ALUNOS ====")
        print("1 - Inserir")
        print("2 - Pesquisar")
        print("3 - Sair")

        opc = input("Escolha a opção: ")

        if opc == "1":
            df = inserir_aluno(df)

        elif opc == "2":
            aluno = pesquisar_aluno(df)
            if aluno is not None:
                print("\nDeseja:")
                print("1 - Editar")
                print("2 - Remover")
                print("3 - Voltar")
                acao = input("Escolha: ")

                if acao == "1":
                    df = editar_aluno(df, aluno)
                elif acao == "2":
                    df = remover_aluno(df, aluno)
                else:
                    print("Voltando ao menu...")

        elif opc == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

# Executa o menu
menu()
