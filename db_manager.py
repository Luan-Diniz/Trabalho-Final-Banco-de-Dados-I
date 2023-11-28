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


class Constant:
    default_answer = "Opção inválida"


class DBManager:
    @staticmethod
    def execute_user_action(user_option, table_option, db_cursor, input_data):
        """
        Executa uma ação de usuário no banco de dados.

        Args:
            user_option (UserOption): A opção escolhida pelo usuário (INSERT, UPDATE, DELETE ou SELECT).
            table_option (TableOption): A tabela na qual a ação será realizada.
            db_cursor: O cursor do banco de dados.
            input_data: Dados de entrada para a ação.

        Returns:
            str: O resultado da ação do usuário.
        """
        operator = CrudeOperator(db_cursor)
        action = DBManager.get_action(user_option)
        return (
            action(table_option, operator, input_data)
            if action
            else Constant.default_answer
        )

    @staticmethod
    def get_action(user_option):
        """
        Obtém a função de ação correspondente com base na opção do usuário.

        Args:
            user_option (UserOption): A opção escolhida pelo usuário (INSERT, UPDATE, DELETE ou SELECT).

        Returns:
            function: A função de ação correspondente.
        """
        return {
            UserOption.INSERT: DBManager.perform_insert,
            UserOption.UPDATE: DBManager.perform_update,
            UserOption.DELETE: DBManager.perform_delete,
            UserOption.SELECT: DBManager.perform_select,
        }.get(user_option)

    @staticmethod
    def perform_insert(table_option, operator, input_data):
        """
        Executa uma inserção de dados na tabela especificada.

        Args:
            table_option (TableOption): A tabela na qual os dados serão inseridos.
            operator: O operador CRUD para interagir com o banco de dados.
            input_data: Dados a serem inseridos.

        Returns:
            str: O resultado da inserção.
        """
        table_name = DBManager.get_table_name(table_option)
        if table_name:
            match table_name:
                case "Transmissão":
                    return operator.create_transmissao(input_data)
                case "Circuito":
                    return operator.create_circuito(input_data)
                case "Patrocinadores":
                    return operator.create_patrocinadores(input_data)
                case "Campeonato":
                    return operator.create_campeonato(input_data)
                case "Equipe":
                    return operator.create_equipe(input_data)
                case "Piloto":
                    return operator.create_piloto(input_data)
                case "Carro":
                    return operator.create_carro(input_data)
                case "Transmite":
                    return operator.create_transmite(input_data)
                case "Participa":
                    return operator.create_participa(input_data)
                case "Possui":
                    return operator.create_possui(input_data)
        return Constant.default_answer

    @staticmethod
    def perform_update(table_option, operator, input_data):
        """
        Executa uma atualização de dados na tabela especificada.

        Args:
            table_option (TableOption): A tabela na qual os dados serão atualizados.
            operator: O operador CRUD para interagir com o banco de dados.
            input_data: Dados para atualização.

        Returns:
            str: O resultado da atualização.
        """
        table_name = DBManager.get_table_name(table_option)
        if table_name:
            match table_name:
                case "Transmissão":
                    return operator.update_transmissao(input_data)
                case "Circuito":
                    return operator.update_circuito(input_data)
                case "Patrocinadores":
                    return operator.update_patrocinadores(input_data)
                case "Campeonato":
                    return operator.update_campeonato(input_data)
                case "Equipe":
                    return operator.update_equipe(input_data)
                case "Piloto":
                    return operator.update_piloto(input_data)
                case "Carro":
                    return operator.update_carro(input_data)
                case "Transmite":
                    return operator.update_transmite(input_data)
                case "Participa":
                    return operator.update_participa(input_data)
                case "Possui":
                    return operator.update_possui(input_data)
        return Constant.default_answer

    @staticmethod
    def perform_delete(table_option, operator, input_data):
        """
        Executa uma exclusão de dados na tabela especificada.

        Args:
            table_option (TableOption): A tabela da qual os dados serão excluídos.
            operator: O operador CRUD para interagir com o banco de dados.
            input_data: Dados para exclusão.

        Returns:
            str: O resultado da exclusão.
        """
        table_name = DBManager.get_table_name(table_option)
        if table_name:
            match table_name:
                case "Transmissão":
                    return operator.delete_transmissao(input_data)
                case "Circuito":
                    return operator.delete_circuito(input_data)
                case "Patrocinadores":
                    return operator.delete_patrocinadores(input_data)
                case "Campeonato":
                    return operator.delete_campeonato(input_data)
                case "Equipe":
                    return operator.delete_equipe(input_data)
                case "Piloto":
                    return operator.delete_piloto(input_data)
                case "Carro":
                    return operator.delete_carro(input_data)
                case "Transmite":
                    return operator.delete_transmite(input_data)
                case "Participa":
                    return operator.delete_participa(input_data)
                case "Possui":
                    return operator.delete_possui(input_data)
        return Constant.default_answer

    @staticmethod
    def perform_select(table_option, operator, input_data):
        """
        Executa uma consulta na tabela especificada.

        Args:
            table_option (TableOption): A tabela na qual a consulta será realizada.
            operator: O operador CRUD para interagir com o banco de dados.
            input_data: Dados para a consulta.

        Returns:
            str: O resultado da consulta.
        """
        table_name = DBManager.get_table_name(table_option)
        if table_name:
            match table_name:
                case "Transmissão":
                    return operator.read_transmissao(input_data)
                case "Circuito":
                    return operator.read_circuito(input_data)
                case "Patrocinadores":
                    return operator.read_patrocinadores(input_data)
                case "Campeonato":
                    return operator.read_campeonato(input_data)
                case "Equipe":
                    return operator.read_equipe(input_data)
                case "Piloto":
                    return operator.read_piloto(input_data)
                case "Carro":
                    return operator.read_carro(input_data)
                case "Transmite":
                    return operator.read_transmite(input_data)
                case "Participa":
                    return operator.read_participa(input_data)
                case "Possui":
                    return operator.read_possui(input_data)
        return Constant.default_answer

    @staticmethod
    def get_table_name(table_option):
        """
        Obtém o nome da tabela com base na opção de tabela.

        Args:
            table_option (TableOption): A opção de tabela.

        Returns:
            str: O nome da tabela.
        """
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
