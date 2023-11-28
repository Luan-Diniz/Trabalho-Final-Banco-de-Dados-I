from crude_operator import CrudeOperator


class Constant:
    default_answer = "Opção inválida"


class DBManager:
    table_names = {
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
    }

    @staticmethod
    def execute_user_action(user_option, table_option, db_cursor, connection):
        operator = CrudeOperator(db_cursor, connection)
        action = DBManager.get_action(user_option)
        table = DBManager.get_table_name(table_option)
        return action(table_option, operator)

    @staticmethod
    def get_action(user_option):
        return {
            "1": DBManager.perform_insert,
            "2": DBManager.perform_update,
            "3": DBManager.perform_delete,
            "4": DBManager.perform_select,
        }.get(user_option)

    @staticmethod
    def perform_insert(table_option, operator):
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
        return Constant.default_answer

    @staticmethod
    def perform_update(table_option, operator):
        table_name = DBManager.get_table_name(table_option)
        if table_name:
            match table_name:
                case "Transmissão":
                    return operator.update_transmissao()
                case "Circuito":
                    return operator.update_circuito()
                case "Patrocinadores":
                    return operator.update_patrocinadores()
                case "Campeonato":
                    return operator.update_campeonato()
                case "Equipe":
                    return operator.update_equipe()
                case "Piloto":
                    return operator.update_piloto()
                case "Carro":
                    return operator.update_carro()
                case "Transmite":
                    return operator.update_transmite()
                case "Participa":
                    return operator.update_participa()
                case "Possui":
                    return operator.update_possui()
        return Constant.default_answer

    @staticmethod
    def perform_delete(table_option, operator):
        table_name = DBManager.get_table_name(table_option)
        if table_name:
            match table_name:
                case "Transmissão":
                    return operator.delete_transmissao()
                case "Circuito":
                    return operator.delete_circuito()
                case "Patrocinadores":
                    return operator.delete_patrocinadores()
                case "Campeonato":
                    return operator.delete_campeonato()
                case "Equipe":
                    return operator.delete_equipe()
                case "Piloto":
                    return operator.delete_piloto()
                case "Carro":
                    return operator.delete_carro()
                case "Transmite":
                    return operator.delete_transmite()
                case "Participa":
                    return operator.delete_participa()
                case "Possui":
                    return operator.delete_possui()
        return Constant.default_answer

    @staticmethod
    def perform_select(table_option, operator):
        table_name = DBManager.get_table_name(table_option)
        if table_name:
            match table_name:
                case "Transmissão":
                    return operator.read_transmissao()
                case "Circuito":
                    return operator.read_circuito()
                case "Patrocinadores":
                    return operator.read_patrocinadores()
                case "Campeonato":
                    return operator.read_campeonato()
                case "Equipe":
                    return operator.read_equipe()
                case "Piloto":
                    return operator.read_piloto()
                case "Carro":
                    return operator.read_carro()
                case "Transmite":
                    return operator.read_transmite()
                case "Participa":
                    return operator.read_participa()
                case "Possui":
                    return operator.read_possui()
        return Constant.default_answer

    @staticmethod
    def get_table_name(table_option):
        return DBManager.table_names.get(table_option)
