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

#  Salvar no csv
def salvar_dados(df):
    df.to_csv(ARQUIVO, index=False)

# Gerar matrícula para o aluno
def gerar_matricula(df):
    if df.empty:
        return 1
    else:
        return df["matricula"].max() + 1

#  Inserir aluno
def inserir_aluno(df):
    print("\n=== INSERIR ALUNO ===")

    matricula = gerar_matricula(df)

    aluno = {
        "matricula": matricula,
        "nome": input("Nome: "),
        "rua": input("Rua: "),
        "numero": input("Número: "),
        "bairro": input("Bairro: "),
        "cidade": input("Cidade: "),
        "uf": input("UF: "),
        "telefone": input("Telefone: "),
        "email": input("Email: ")
    }

    df = pd.concat([df, pd.DataFrame([aluno])], ignore_index=True)
    salvar_dados(df)

    print("\nAluno cadastrado com sucesso! Matrícula:", matricula)
    return df

#  Pesquisar aluno
def pesquisar_aluno(df):
    print("\n=== PESQUISAR ALUNO ===")
    print("1 - Por matrícula")
    print("2 - Por nome")
    opc = input("Escolha a opção: ")

    if opc == "1":
        mat = input("Digite a matrícula: ")
        if not mat.isdigit():
            print("Matrícula inválida!")
            return None

        resultado = df[df["matricula"] == int(mat)]

    elif opc == "2":
        nome = input("Digite o nome: ")
        resultado = df[df["nome"].str.contains(nome, case=False, na=False)]
    else:
        print("Opção inválida!")
        return None

    if resultado.empty:
        print("\nAluno NÃO encontrado!")
        return None

    print("\n--- ALUNO ENCONTRADO ---")
    print(resultado.to_string(index=False))

    return resultado.iloc[0]

#  Editar aluno
def editar_aluno(df, aluno):
    print("\n=== EDITAR ALUNO ===")
    print("Quais dados deseja editar?")
    print("1 - Nome")
    print("2 - Rua")
    print("3 - Número")
    print("4 - Bairro")
    print("5 - Cidade")
    print("6 - UF")
    print("7 - Telefone")
    print("8 - Email")
    print("9 - Cancelar")

    opc = input("Escolha a opção: ")

    campos = {
        "1": "nome",
        "2": "rua",
        "3": "numero",
        "4": "bairro",
        "5": "cidade",
        "6": "uf",
        "7": "telefone",
        "8": "email"
    }

    if opc == "9":
        print("Edição cancelada.")
        return df

    if opc not in campos:
        print("Opção inválida!")
        return df

    campo = campos[opc]
    novo_valor = input(f"Digite o novo valor para {campo}: ")

    df.loc[df["matricula"] == aluno["matricula"], campo] = novo_valor
    salvar_dados(df)

    print("\nDados atualizados com sucesso!")
    return df

#  Remover aluno
def remover_aluno(df, aluno):
    print("\n=== REMOVER ALUNO ===")
    confirma = input(f"Deseja realmente remover o aluno {aluno['nome']}? (s/n): ")

    if confirma.lower() == "s":
        df = df[df["matricula"] != aluno["matricula"]]
        salvar_dados(df)
        print("\nAluno removido com sucesso!")
    else:
        print("Remoção cancelada.")

    return df


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
