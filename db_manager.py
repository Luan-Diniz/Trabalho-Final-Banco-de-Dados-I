from enum import Enum
from crude_operator import CrudeOperator


class TableOption(Enum):
    TRANSMISSAO = 1
    CIRCUITO = 2
    PATROCINADORES = 3
    CAMPEONATO = 4
    EQUIPE = 5
    PILOTO = 6
    CARRO = 7
    TRANSMITE = 8
    PARTICIPA = 9
    POSSUI = 10


class UserOption(Enum):
    INSERT = 1
    UPDATE = 2
    DELETE = 3
    SELECT = 4


class DBManager:
    @staticmethod
    def execute_user_action(user_option, table_option, db_cursor, input_data):
        operator = CrudeOperator(db_cursor)
        action = DBManager.get_action(user_option)
        return (
            action(table_option, operator, input_data) if action else "Opção inválida"
        )

    @staticmethod
    def get_action(user_option):
        return {
            UserOption.INSERT: DBManager.perform_insert,
            UserOption.UPDATE: DBManager.perform_update,
            UserOption.DELETE: DBManager.perform_delete,
            UserOption.SELECT: DBManager.perform_select,
        }.get(user_option)

    @staticmethod
    def perform_insert(table_option, operator, input_data):
        table_name = DBManager.get_table_name(table_option)
        if table_name:
            match table_name:
                case "Transmissão":
                    return operator.create_transmissao()
                case "Circuito":
                    return operator.create_circuito()
                case "Patrocinadores":
                    return operator.create_patrocinadores()
                case "Campeonato":
                    return operator.create_campeonato()
                case "Equipe":
                    return operator.create_equipe()
                case "Piloto":
                    return operator.create_piloto()
                case "Carro":
                    return operator.create_carro()
                case "Transmite":
                    return operator.create_transmite()
                case "Participa":
                    return operator.create_participa()
                case "Possui":
                    return operator.create_possui()
        return "Opção inválida"

    @staticmethod
    def perform_update(table_option, operator):
        # Update logic
        ...

    @staticmethod
    def perform_delete(table_option, operator):
        # Delete logic
        ...

    @staticmethod
    def perform_select(table_option, operator):
        # Select logic
        ...

    @staticmethod
    def get_table_name(table_option):
        return {
            TableOption.TRANSMISSAO: "Transmissão",
            TableOption.CIRCUITO: "Circuito",
            TableOption.PATROCINADORES: "Patrocinadores",
            TableOption.CAMPEONATO: "Campeonato",
            TableOption.EQUIPE: "Equipe",
            TableOption.PILOTO: "Piloto",
            TableOption.CARRO: "Carro",
            TableOption.TRANSMITE: "Transmite",
            TableOption.PARTICIPA: "Participa",
            TableOption.POSSUI: "Possui",
        }.get(table_option)
