import psycopg2
import pandas as pd
from specific_queries import SpecificQueries
from db_manager import DBManager


def connect_to_db():
    return psycopg2.connect(
        host="localhost",
        dbname="formula1",
        user="postgres",
        password="postgres",
        port=2023,
    )


def get_user_choice(prompt, options):
    while True:
        print(prompt)
        for option, description in options.items():
            print(f"\t{description}: Digite {option}")
        choice = input()
        if choice in options:
            return choice
        else:
            print("Opção inválida. Tente novamente.\n")


def main():
    connection = connect_to_db()
    cursor = connection.cursor()
    queries = SpecificQueries(cursor)

    while True:
        main_choice = get_user_choice(
            "----------BANCO DE DADOS DA FORMULA1 ---------------\nSelecione o que você quer fazer:",
            {"1": "CONSULTA", "2": "OPERAÇÃO EM UMA TABELA", "0": "SAIR DO PROGRAMA"},
        )

        if main_choice == "0":
            print("Fechando o programa...")
            break

        elif main_choice == "1":
            query_choice = get_user_choice(
                "Qual das seguintes consultas você quer fazer?",
                {
                    "1": "CLASSIFICAÇÃO PILOTOS",
                    "2": "PATROCINADORES DAS EQUIPES",
                    "3": "CIRCUITOS NÃO USADOS",
                },
            )

            if query_choice == "1":
                ano_consulta = input("De qual ano? ")
                queries.show_pontuation(ano_consulta)

            elif query_choice == "2":
                queries.not_in_team()

            elif query_choice == "3":
                queries.not_used_tracks()

        elif main_choice == "2":
            user_choice = get_user_choice(
                "O que você quer fazer?",
                {
                    "1": "INSERIR",
                    "2": "ATUALIZAR",
                    "3": "DELETAR",
                    "4": "CONSULTAR",
                },
            )
            table_choice = get_user_choice(
                "Escolha a tabela para operar:",
                {
                    "1": "Transmissão",
                    "2": "Circuito",
                    "3": "Patrocinadores",
                    "4": "Campeonato",
                    "5": "Equipe",
                    "6": "Piloto",
                    "7": "Carro",
                    "8": "Transmite",
                    "9": "Participa",
                    "10": "Possui",
                },
            )
            print(DBManager.execute_user_action(user_choice, table_choice, cursor))
    connection.commit()
    connection.close()


if __name__ == "__main__":
    main()
