class CrudeOperator:
    def __init__(self, db_cursor, connection):
        self.con = db_cursor
        self.connection = connection

    def create_transmissao(self):
        emissora = input("Emissora: ")
        ano = int(input("Ano: "))
        comentaristas = input("Comentaristas: ")
        audiencia = float(input("Audiência: "))
        with self.con as cur:
            cur.execute(
                """
                INSERT INTO Transmissão (Emissora, Ano, Comentaristas, Audiência)
                VALUES (%s, %s, %s, %s)
            """,
                (emissora, ano, comentaristas, audiencia),
            )
            self.connection.commit()

    def read_transmissao(self):
        emissora = input("Emissora: ")
        ano = int(input("Ano: "))
        with self.con as cur:
            cur.execute(
                """
                SELECT * FROM Transmissão WHERE Emissora = %s AND Ano = %s
            """,
                (emissora, ano),
            )
            return cur.fetchall()

    def update_transmissao(self):
        emissora = input("Emissora: ")
        ano = int(input("Ano: "))
        comentaristas = input("Comentaristas: ")
        audiencia = float(input("Audiência: "))
        with self.con as cur:
            cur.execute(
                """
                UPDATE Transmissão
                SET Comentaristas = %s, Audiência = %s
                WHERE Emissora = %s AND Ano = %s
            """,
                (comentaristas, audiencia, emissora, ano),
            )
            self.connection

    def delete_transmissao(self):
        emissora = input("Emissora: ")
        ano = int(input("Ano: "))
        with self.con as cur:
            cur.execute(
                """
                DELETE FROM Transmissão WHERE Emissora = %s AND Ano = %s
            """,
                (emissora, ano),
            )
            self.connection

    def create_circuito(self):
        nome = input("Nome do Circuito: ")
        local = input("Local do Circuito: ")
        melhor_tempo = input("Melhor Tempo: ")
        extensao = float(input("Extensão: "))
        with self.con as cur:
            cur.execute(
                """
                INSERT INTO Circuito (Nome, Local, Melhor_Tempo, Extensão)
                VALUES (%s, %s, %s, %s)
            """,
                (nome, local, melhor_tempo, extensao),
            )
            self.connection

    def read_circuito(self):
        nome = input("Nome do Circuito: ")
        local = input("Local do Circuito: ")
        with self.con as cur:
            cur.execute(
                """
                SELECT * FROM Circuito WHERE Nome = %s AND Local = %s
            """,
                (nome, local),
            )
            return cur.fetchall()

    def update_circuito(self):
        nome = input("Nome do Circuito: ")
        local = input("Local do Circuito: ")
        melhor_tempo = input("Melhor Tempo: ")
        extensao = float(input("Extensão: "))
        with self.con as cur:
            cur.execute(
                """
                UPDATE Circuito
                SET Melhor_Tempo = %s, Extensão = %s
                WHERE Nome = %s AND Local = %s
            """,
                (melhor_tempo, extensao, nome, local),
            )
            self.connection

    def delete_circuito(self):
        nome = input("Nome do Circuito: ")
        local = input("Local do Circuito: ")
        with self.con as cur:
            cur.execute(
                """
                DELETE FROM Circuito WHERE Nome = %s AND Local = %s
            """,
                (nome, local),
            )
            self.connection

    def create_patrocinador(self):
        marca = input("Marca: ")
        valor_do_patrocinio = input("Valor do Patrocínio: ")
        id_patrocinador = input("ID do Patrocinador: ")
        with self.con as cur:
            cur.execute(
                """
                INSERT INTO Patrocinadores (Marca, Valor_do_Patrocinio, id_patrocinador)
                VALUES (%s, %s, %s)
            """,
                (marca, valor_do_patrocinio, id_patrocinador),
            )
            self.connection

    def read_patrocinador(self):
        id_patrocinador = input("ID do Patrocinador: ")
        with self.con as cur:
            cur.execute(
                """
                SELECT * FROM Patrocinadores WHERE id_patrocinador = %s
            """,
                (id_patrocinador,),
            )
            return cur.fetchone()

    def update_patrocinador(self):
        marca = input("Marca: ")
        valor_do_patrocinio = input("Valor do Patrocínio: ")
        id_patrocinador = input("ID do Patrocinador: ")
        with self.con as cur:
            cur.execute(
                """
                UPDATE Patrocinadores
                SET Marca = %s, Valor_do_Patrocinio = %s
                WHERE id_patrocinador = %s
            """,
                (marca, valor_do_patrocinio, id_patrocinador),
            )
            self.connection

    def delete_patrocinador(self):
        id_patrocinador = input("ID do Patrocinador: ")
        with self.con as cur:
            cur.execute(
                """
                DELETE FROM Patrocinadores WHERE id_patrocinador = %s
            """,
                (id_patrocinador,),
            )
            self.connection

    def create_campeonato(self):
        id_campeonato = input("ID do Campeonato: ")
        ano = int(input("Ano do Campeonato: "))
        vencedor = input("Vencedor do Campeonato: ")
        numero_de_corridas = int(input("Número de Corridas: "))
        with self.con as cur:
            cur.execute(
                """
                INSERT INTO Campeonato (id_campeonato, Ano, Vencedor, Numero_de_Corridas)
                VALUES (%s, %s, %s, %s)
                """,
                (id_campeonato, ano, vencedor, numero_de_corridas),
            )
            self.connection

    def read_campeonato(self):
        id_campeonato = input("ID do Campeonato: ")
        with self.con as cur:
            cur.execute(
                """
                SELECT * FROM Campeonato WHERE id_campeonato = %s
                """,
                (id_campeonato,),
            )
            return cur.fetchall()

    def update_campeonato(self):
        id_campeonato = input("ID do Campeonato: ")
        ano = int(input("Novo Ano do Campeonato: "))
        vencedor = input("Novo Vencedor do Campeonato: ")
        numero_de_corridas = int(input("Novo Número de Corridas: "))
        with self.con as cur:
            cur.execute(
                """
                UPDATE Campeonato
                SET Ano = %s, Vencedor = %s, Numero_de_Corridas = %s
                WHERE id_campeonato = %s
                """,
                (ano, vencedor, numero_de_corridas, id_campeonato),
            )
            self.connection

    def delete_campeonato(self):
        id_campeonato = input("ID do Campeonato: ")
        with self.con as cur:
            cur.execute(
                """
                DELETE FROM Campeonato WHERE id_campeonato = %s
                """,
                (id_campeonato,),
            )
            self.connection

    def create_carro(self):
        trocas_mgu_k = int(input("Número de Trocas MGU-K: "))
        trocas_mgu_h = int(input("Número de Trocas MGU-H: "))
        numero_do_carro = input("Número do Carro: ")
        id_piloto = input("ID do Piloto Associado: ")
        with self.con as cur:
            cur.execute(
                """
                INSERT INTO Carro (Trocas_MGU_K, Trocas_MGU_H, Numero_do_carro, idPiloto)
                VALUES (%s, %s, %s, %s)
                """,
                (trocas_mgu_k, trocas_mgu_h, numero_do_carro, id_piloto),
            )
            self.connection

    def read_carro(self):
        numero_do_carro = input("Número do Carro: ")
        with self.con as cur:
            cur.execute(
                """
                SELECT * FROM Carro WHERE Numero_do_carro = %s
                """,
                (numero_do_carro,),
            )
            return cur.fetchall()

    def update_carro(self):
        numero_do_carro = input("Número do Carro: ")
        trocas_mgu_k = int(input("Novo Número de Trocas MGU-K: "))
        trocas_mgu_h = int(input("Novo Número de Trocas MGU-H: "))
        id_piloto = input("Novo ID do Piloto Associado: ")
        with self.con as cur:
            cur.execute(
                """
                UPDATE Carro
                SET Trocas_MGU_K = %s, Trocas_MGU_H = %s, idPiloto = %s
                WHERE Numero_do_carro = %s
                """,
                (trocas_mgu_k, trocas_mgu_h, id_piloto, numero_do_carro),
            )
            self.connection

    def delete_carro(self):
        numero_do_carro = input("Número do Carro: ")
        with self.con as cur:
            cur.execute(
                """
                DELETE FROM Carro WHERE Numero_do_carro = %s
                """,
                (numero_do_carro,),
            )
            self.connection

    def create_piloto(self):
        numero_de_pole_positions = int(input("Número de Pole Positions: "))
        id_piloto = input("ID do Piloto: ")
        numero_de_vitorias = int(input("Número de Vitórias: "))
        nome = input("Nome do Piloto: ")
        nacionalidade = input("Nacionalidade do Piloto: ")
        pontos_de_corrida = float(input("Pontos de Corrida: "))
        numero_de_podios = int(input("Número de Pódios: "))
        id_equipe = input("ID da Equipe: ")
        ano_campeonato = int(input("Ano do Campeonato: "))
        with self.con as cur:
            cur.execute(
                """
                INSERT INTO Piloto (Numero_de_pole_positions, Id_Piloto, Número_de_Vitórias, Nome, Nacionalidade, Pontos_de_Corrida, Número_de_Pódios, idEquipe, Ano_Campeonato)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    numero_de_pole_positions,
                    id_piloto,
                    numero_de_vitorias,
                    nome,
                    nacionalidade,
                    pontos_de_corrida,
                    numero_de_podios,
                    id_equipe,
                    ano_campeonato,
                ),
            )
            self.connection

    def read_piloto(self):
        id_piloto = input("ID do Piloto: ")
        with self.con as cur:
            cur.execute(
                """
                SELECT * FROM Piloto WHERE Id_Piloto = %s
                """,
                (id_piloto,),
            )
            return cur.fetchall()

    def update_piloto(self):
        id_piloto = input("ID do Piloto: ")
        numero_de_pole_positions = int(input("Novo Número de Pole Positions: "))
        numero_de_vitorias = int(input("Novo Número de Vitórias: "))
        nome = input("Novo Nome do Piloto: ")
        nacionalidade = input("Nova Nacionalidade do Piloto: ")
        pontos_de_corrida = float(input("Novos Pontos de Corrida: "))
        numero_de_podios = int(input("Novo Número de Pódios: "))
        id_equipe = input("Novo ID da Equipe: ")
        ano_campeonato = int(input("Novo Ano do Campeonato: "))
        with self.con as cur:
            cur.execute(
                """
                UPDATE Piloto
                SET Numero_de_pole_positions = %s, Número_de_Vitórias = %s, Nome = %s, Nacionalidade = %s, Pontos_de_Corrida = %s, Número_de_Pódios = %s, idEquipe = %s, Ano_Campeonato = %s
                WHERE Id_Piloto = %s
                """,
                (
                    numero_de_pole_positions,
                    numero_de_vitorias,
                    nome,
                    nacionalidade,
                    pontos_de_corrida,
                    numero_de_podios,
                    id_equipe,
                    ano_campeonato,
                    id_piloto,
                ),
            )
            self.connection

    def delete_piloto(self):
        id_piloto = input("ID do Piloto: ")
        with self.con as cur:
            cur.execute(
                """
                DELETE FROM Piloto WHERE Id_Piloto = %s
                """,
                (id_piloto,),
            )
            self.connection

    def create_equipe(self):
        nome = input("Nome da Equipe: ")
        sede = input("Sede da Equipe: ")
        id_equipe = input("ID da Equipe: ")
        diretor = input("Diretor da Equipe: ")
        idPatrocinadores = input("ID dos Patrocinadores: ")
        with self.con as cur:
            cur.execute(
                """
                INSERT INTO Equipe (Nome, Sede, id_equipe, Diretor, idPatrocinadores)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (nome, sede, id_equipe, diretor, idPatrocinadores),
            )
            self.connection

    def read_equipe(self):
        id_equipe = input("ID da Equipe: ")
        with self.con as cur:
            cur.execute(
                """
                SELECT * FROM Equipe WHERE id_equipe = %s
                """,
                (id_equipe,),
            )
            return cur.fetchall()

    def update_equipe(self):
        id_equipe = input("ID da Equipe: ")
        nome = input("Novo Nome da Equipe: ")
        sede = input("Nova Sede da Equipe: ")
        diretor = input("Novo Diretor da Equipe: ")
        idPatrocinadores = input("Novo ID dos Patrocinadores: ")
        with self.con as cur:
            cur.execute(
                """
                UPDATE Equipe
                SET Nome = %s, Sede = %s, Diretor = %s, idPatrocinadores = %s
                WHERE id_equipe = %s
                """,
                (nome, sede, diretor, idPatrocinadores, id_equipe),
            )
            self.connection

    def delete_equipe(self):
        id_equipe = input("ID da Equipe: ")
        with self.con as cur:
            cur.execute(
                """
                DELETE FROM Equipe WHERE id_equipe = %s
                """,
                (id_equipe,),
            )
            self.connection

    def create_participa(self):
        id_equipe = input("ID da Equipe: ")
        id_campeonato = input("ID do Campeonato: ")
        with self.con as cur:
            cur.execute(
                """
                INSERT INTO Participa (id_equipe, id_campeonato)
                VALUES (%s, %s)
                """,
                (id_equipe, id_campeonato),
            )
            self.connection

    def read_participa(self):
        id_equipe = input("ID da Equipe: ")
        id_campeonato = input("ID do Campeonato: ")
        with self.con as cur:
            cur.execute(
                """
                SELECT * FROM Participa WHERE id_equipe = %s AND id_campeonato = %s
                """,
                (id_equipe, id_campeonato),
            )
            return cur.fetchall()

    def update_participa(self):
        id_equipe = input("ID da Equipe: ")
        id_campeonato = input("ID do Campeonato: ")
        new_id_equipe = input("Novo ID da Equipe: ")
        new_id_campeonato = input("Novo ID do Campeonato: ")
        with self.con as cur:
            cur.execute(
                """
                UPDATE Participa
                SET id_equipe = %s, id_campeonato = %s
                WHERE id_equipe = %s AND id_campeonato = %s
                """,
                (new_id_equipe, new_id_campeonato, id_equipe, id_campeonato),
            )
            self.connection

    def delete_participa(self):
        id_equipe = input("ID da Equipe: ")
        id_campeonato = input("ID do Campeonato: ")
        with self.con as cur:
            cur.execute(
                """
                DELETE FROM Participa WHERE id_equipe = %s AND id_campeonato = %s
                """,
                (id_equipe, id_campeonato),
            )
            self.connection

    def create_possui(self):
        id_campeonato = input("ID do Campeonato: ")
        nome = input("Nome: ")
        with self.con as cur:
            cur.execute(
                """
                INSERT INTO Possui (id_campeonato, Nome)
                VALUES (%s, %s)
                """,
                (id_campeonato, nome),
            )
            self.connection

    def read_possui(self):
        id_campeonato = input("ID do Campeonato: ")
        nome = input("Nome: ")
        with self.con as cur:
            cur.execute(
                """
                SELECT * FROM Possui WHERE id_campeonato = %s AND Nome = %s
                """,
                (id_campeonato, nome),
            )
            return cur.fetchall()

    def update_possui(self):
        id_campeonato = input("ID do Campeonato: ")
        nome = input("Nome: ")
        new_id_campeonato = input("Novo ID do Campeonato: ")
        new_nome = input("Novo Nome: ")
        with self.con as cur:
            cur.execute(
                """
                UPDATE Possui
                SET id_campeonato = %s, Nome = %s
                WHERE id_campeonato = %s AND Nome = %s
                """,
                (new_id_campeonato, new_nome, id_campeonato, nome),
            )
            self.connection

    def delete_possui(self):
        id_campeonato = input("ID do Campeonato: ")
        nome = input("Nome: ")
        with self.con as cur:
            cur.execute(
                """
                DELETE FROM Possui WHERE id_campeonato = %s AND Nome = %s
                """,
                (id_campeonato, nome),
            )
            self.connection

    def create_transmite(self):
        id_campeonato = input("ID do Campeonato: ")
        emissora = input("Emissora: ")
        with self.con as cur:
            cur.execute(
                """
                INSERT INTO Transmite (id_campeonato, Emissora)
                VALUES (%s, %s)
                """,
                (id_campeonato, emissora),
            )
            self.connection

    def read_transmite(self):
        id_campeonato = input("ID do Campeonato: ")
        emissora = input("Emissora: ")
        with self.con as cur:
            cur.execute(
                """
                SELECT * FROM Transmite WHERE id_campeonato = %s AND Emissora = %s
                """,
                (id_campeonato, emissora),
            )
            return cur.fetchall()

    def update_transmite(self):
        id_campeonato = input("ID do Campeonato: ")
        emissora = input("Emissora: ")
        new_id_campeonato = input("Novo ID do Campeonato: ")
        new_emissora = input("Nova Emissora: ")
        with self.con as cur:
            cur.execute(
                """
                UPDATE Transmite
                SET id_campeonato = %s, Emissora = %s
                WHERE id_campeonato = %s AND Emissora = %s
                """,
                (new_id_campeonato, new_emissora, id_campeonato, emissora),
            )
            self.connection

    def delete_transmite(self):
        id_campeonato = input("ID do Campeonato: ")
        emissora = input("Emissora: ")
        with self.con as cur:
            cur.execute(
                """
                DELETE FROM Transmite WHERE id_campeonato = %s AND Emissora = %s
                """,
                (id_campeonato, emissora),
            )
            self.connection
