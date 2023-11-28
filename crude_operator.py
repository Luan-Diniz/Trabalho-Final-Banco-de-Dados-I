class CrudeOperator:
    def __init__(self, db_cursor):
        self.con = db_cursor

    def create_transmissao(self, emissora, ano, comentaristas, audiencia):
        with self.con.cursor() as cur:
            cur.execute(
                """
                INSERT INTO Transmissão (Emissora, Ano, Comentaristas, Audiência)
                VALUES (%s, %s, %s, %s)
            """,
                (emissora, ano, comentaristas, audiencia),
            )
            self.con.commit()

    def read_transmissao(self, emissora, ano):
        with self.con.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM Transmissão WHERE Emissora = %s AND Ano = %s
            """,
                (emissora, ano),
            )
            return cur.fetchall()

    def update_transmissao(self, emissora, ano, comentaristas, audiencia):
        with self.con.cursor() as cur:
            cur.execute(
                """
                UPDATE Transmissão
                SET Comentaristas = %s, Audiência = %s
                WHERE Emissora = %s AND Ano = %s
            """,
                (comentaristas, audiencia, emissora, ano),
            )
            self.con.commit()

    def delete_transmissao(self, emissora, ano):
        with self.con.cursor() as cur:
            cur.execute(
                """
                DELETE FROM Transmissão WHERE Emissora = %s AND Ano = %s
            """,
                (emissora, ano),
            )
            self.con.commit()

    def create_circuito(self, melhor_tempo, extensao, nome, local):
        with self.con.cursor() as cur:
            cur.execute(
                """
                INSERT INTO Circuito (Melhor_Tempo, Extensão, Nome, Local)
                VALUES (%s, %s, %s, %s)
            """,
                (melhor_tempo, extensao, nome, local),
            )
            self.con.commit()

    def read_circuito(self, nome, local):
        with self.con.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM Circuito WHERE Nome = %s AND Local = %s
            """,
                (nome, local),
            )
            return cur.fetchall()

    def update_circuito(self, melhor_tempo, extensao, nome, local):
        with self.con.cursor() as cur:
            cur.execute(
                """
                UPDATE Circuito
                SET Melhor_Tempo = %s, Extensão = %s
                WHERE Nome = %s AND Local = %s
            """,
                (melhor_tempo, extensao, nome, local),
            )
            self.con.commit()

    def delete_circuito(self, nome, local):
        with self.con.cursor() as cur:
            cur.execute(
                """
                DELETE FROM Circuito WHERE Nome = %s AND Local = %s
            """,
                (nome, local),
            )
            self.con.commit()

    def create_patrocinador(self, marca, valor_do_patrocinio, id_patrocinador):
        with self.con.cursor() as cur:
            cur.execute(
                """
                INSERT INTO Patrocinadores (Marca, Valor_do_Patrocinio, id_patrocinador)
                VALUES (%s, %s, %s)
            """,
                (marca, valor_do_patrocinio, id_patrocinador),
            )
            self.con.commit()

    def read_patrocinador(self, id_patrocinador):
        with self.con.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM Patrocinadores WHERE id_patrocinador = %s
            """,
                (id_patrocinador,),
            )
            return cur.fetchone()

    def update_patrocinador(self, marca, valor_do_patrocinio, id_patrocinador):
        with self.con.cursor() as cur:
            cur.execute(
                """
                UPDATE Patrocinadores
                SET Marca = %s, Valor_do_Patrocinio = %s
                WHERE id_patrocinador = %s
            """,
                (marca, valor_do_patrocinio, id_patrocinador),
            )
            self.con.commit()

    def delete_patrocinador(self, id_patrocinador):
        with self.con.cursor() as cur:
            cur.execute(
                """
                DELETE FROM Patrocinadores WHERE id_patrocinador = %s
            """,
                (id_patrocinador,),
            )
            self.con.commit()

    def create_campeonato(self, id_campeonato, ano, vencedor, numero_de_corridas):
        with self.con.cursor() as cur:
            cur.execute(
                """
                INSERT INTO Campeonato (id_campeonato, Ano, Vencedor, Numero_de_Corridas)
                VALUES (%s, %s, %s, %s)
                """,
                (id_campeonato, ano, vencedor, numero_de_corridas),
            )
            self.con.commit()

    def read_campeonato(self, id_campeonato):
        with self.con.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM Campeonato WHERE id_campeonato = %s
                """,
                (id_campeonato,),
            )
            return cur.fetchall()

    def update_campeonato(self, id_campeonato, ano, vencedor, numero_de_corridas):
        with self.con.cursor() as cur:
            cur.execute(
                """
                UPDATE Campeonato
                SET Ano = %s, Vencedor = %s, Numero_de_Corridas = %s
                WHERE id_campeonato = %s
                """,
                (ano, vencedor, numero_de_corridas, id_campeonato),
            )
            self.con.commit()

    def delete_campeonato(self, id_campeonato):
        with self.con.cursor() as cur:
            cur.execute(
                """
                DELETE FROM Campeonato WHERE id_campeonato = %s
                """,
                (id_campeonato,),
            )
            self.con.commit()

    def create_equipe(self, nome, sede, id_equipe, diretor, idPatrocinadores):
        with self.con.cursor() as cur:
            cur.execute(
                """
                INSERT INTO Equipe (Nome, Sede, id_equipe, Diretor, idPatrocinadores)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (nome, sede, id_equipe, diretor, idPatrocinadores),
            )
            self.con.commit()

    def read_equipe(self, id_equipe):
        with self.con.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM Equipe WHERE id_equipe = %s
                """,
                (id_equipe,),
            )
            return cur.fetchall()

    def update_equipe(self, nome, sede, id_equipe, diretor, idPatrocinadores):
        with self.con.cursor() as cur:
            cur.execute(
                """
                UPDATE Equipe
                SET Nome = %s, Sede = %s, Diretor = %s, idPatrocinadores = %s
                WHERE id_equipe = %s
                """,
                (nome, sede, diretor, idPatrocinadores, id_equipe),
            )
            self.con.commit()

    def delete_equipe(self, id_equipe):
        with self.con.cursor() as cur:
            cur.execute(
                """
                DELETE FROM Equipe WHERE id_equipe = %s
                """,
                (id_equipe,),
            )
            self.con.commit()

    def create_piloto(
        self,
        numero_de_pole_positions,
        id_piloto,
        numero_de_vitorias,
        nome,
        nacionalidade,
        pontos_de_corrida,
        numero_de_podios,
        id_equipe,
        ano_campeonato,
    ):
        with self.con.cursor() as cur:
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
            self.con.commit()

    def read_piloto(self, id_piloto):
        with self.con.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM Piloto WHERE Id_Piloto = %s
                """,
                (id_piloto,),
            )
            return cur.fetchall()

    def update_piloto(
        self,
        numero_de_pole_positions,
        id_piloto,
        numero_de_vitorias,
        nome,
        nacionalidade,
        pontos_de_corrida,
        numero_de_podios,
        id_equipe,
        ano_campeonato,
    ):
        with self.con.cursor() as cur:
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
            self.con.commit()

    def delete_piloto(self, id_piloto):
        with self.con.cursor() as cur:
            cur.execute(
                """
                DELETE FROM Piloto WHERE Id_Piloto = %s
                """,
                (id_piloto,),
            )
            self.con.commit()

    def create_carro(self, trocas_mgu_k, trocas_mgu_h, numero_do_carro, id_piloto):
        with self.con.cursor() as cur:
            cur.execute(
                """
                INSERT INTO Carro (Trocas_MGU_K, Trocas_MGU_H, Numero_do_carro, idPiloto)
                VALUES (%s, %s, %s, %s)
                """,
                (trocas_mgu_k, trocas_mgu_h, numero_do_carro, id_piloto),
            )
            self.con.commit()

    def read_carro(self, numero_do_carro):
        with self.con.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM Carro WHERE Numero_do_carro = %s
                """,
                (numero_do_carro,),
            )
            return cur.fetchall()

    def update_carro(self, trocas_mgu_k, trocas_mgu_h, numero_do_carro, id_piloto):
        with self.con.cursor() as cur:
            cur.execute(
                """
                UPDATE Carro
                SET Trocas_MGU_K = %s, Trocas_MGU_H = %s, idPiloto = %s
                WHERE Numero_do_carro = %s
                """,
                (trocas_mgu_k, trocas_mgu_h, id_piloto, numero_do_carro),
            )
            self.con.commit()

    def delete_carro(self, numero_do_carro):
        with self.con.cursor() as cur:
            cur.execute(
                """
                DELETE FROM Carro WHERE Numero_do_carro = %s
                """,
                (numero_do_carro,),
            )
            self.con.commit()

    def create_transmite(self, id_campeonato, emissora):
        with self.con.cursor() as cur:
            cur.execute(
                """
                INSERT INTO Transmite (id_campeonato, Emissora)
                VALUES (%s, %s)
                """,
                (id_campeonato, emissora),
            )
            self.con.commit()

    def read_transmite(self, id_campeonato, emissora):
        with self.con.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM Transmite WHERE id_campeonato = %s AND Emissora = %s
                """,
                (id_campeonato, emissora),
            )
            return cur.fetchall()

    def update_transmite(
        self, id_campeonato, emissora, new_id_campeonato, new_emissora
    ):
        with self.con.cursor() as cur:
            cur.execute(
                """
                UPDATE Transmite
                SET id_campeonato = %s, Emissora = %s
                WHERE id_campeonato = %s AND Emissora = %s
                """,
                (new_id_campeonato, new_emissora, id_campeonato, emissora),
            )
            self.con.commit()

    def delete_transmite(self, id_campeonato, emissora):
        with self.con.cursor() as cur:
            cur.execute(
                """
                DELETE FROM Transmite WHERE id_campeonato = %s AND Emissora = %s
                """,
                (id_campeonato, emissora),
            )
            self.con.commit()

    def create_participa(self, id_equipe, id_campeonato):
        with self.con.cursor() as cur:
            cur.execute(
                """
                INSERT INTO Participa (id_equipe, id_campeonato)
                VALUES (%s, %s)
                """,
                (id_equipe, id_campeonato),
            )
            self.con.commit()

    def read_participa(self, id_equipe, id_campeonato):
        with self.con.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM Participa WHERE id_equipe = %s AND id_campeonato = %s
                """,
                (id_equipe, id_campeonato),
            )
            return cur.fetchall()

    def update_participa(
        self, id_equipe, id_campeonato, new_id_equipe, new_id_campeonato
    ):
        with self.con.cursor() as cur:
            cur.execute(
                """
                UPDATE Participa
                SET id_equipe = %s, id_campeonato = %s
                WHERE id_equipe = %s AND id_campeonato = %s
                """,
                (new_id_equipe, new_id_campeonato, id_equipe, id_campeonato),
            )
            self.con.commit()

    def delete_participa(self, id_equipe, id_campeonato):
        with self.con.cursor() as cur:
            cur.execute(
                """
                DELETE FROM Participa WHERE id_equipe = %s AND id_campeonato = %s
                """,
                (id_equipe, id_campeonato),
            )
            self.con.commit()

    def create_possui(self, id_campeonato, nome):
        with self.con.cursor() as cur:
            cur.execute(
                """
                INSERT INTO Possui (id_campeonato, Nome)
                VALUES (%s, %s)
                """,
                (id_campeonato, nome),
            )
            self.con.commit()

    def read_possui(self, id_campeonato, nome):
        with self.con.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM Possui WHERE id_campeonato = %s AND Nome = %s
                """,
                (id_campeonato, nome),
            )
            return cur.fetchall()

    def update_possui(self, id_campeonato, nome, new_id_campeonato, new_nome):
        with self.con.cursor() as cur:
            cur.execute(
                """
                UPDATE Possui
                SET id_campeonato = %s, Nome = %s
                WHERE id_campeonato = %s AND Nome = %s
                """,
                (new_id_campeonato, new_nome, id_campeonato, nome),
            )
            self.con.commit()

    def delete_possui(self, id_campeonato, nome):
        with self.con.cursor() as cur:
            cur.execute(
                """
                DELETE FROM Possui WHERE id_campeonato = %s AND Nome = %s
                """,
                (id_campeonato, nome),
            )
            self.con.commit()
