import psycopg2
class CrudeOperator:
    def __init__(db_cursor):
        self.con = db_cursor
        
    
    def create_transmissao(self, emissora, ano, comentaristas, audiencia):
        with self.con.cursor() as cur:
            cur.execute("""
                INSERT INTO Transmissão (Emissora, Ano, Comentaristas, Audiência)
                VALUES (%s, %s, %s, %s)
            """, (emissora, ano, comentaristas, audiencia))
            self.con.commit()

    def read_transmissao(self, emissora, ano):
        with self.con.cursor() as cur:
            cur.execute("""
                SELECT * FROM Transmissão WHERE Emissora = %s AND Ano = %s
            """, (emissora, ano))
            return cur.fetchall()

    def update_transmissao(self, emissora, ano, comentaristas, audiencia):
        with self.con.cursor() as cur:
            cur.execute("""
                UPDATE Transmissão
                SET Comentaristas = %s, Audiência = %s
                WHERE Emissora = %s AND Ano = %s
            """, (comentaristas, audiencia, emissora, ano))
            self.con.commit()

    def delete_transmissao(self, emissora, ano):
        with self.con.cursor() as cur:
            cur.execute("""
                DELETE FROM Transmissão WHERE Emissora = %s AND Ano = %s
            """, (emissora, ano))
            self.con.commit()
            
    def create_circuito(self, melhor_tempo, extensao, nome, local):
        with self.con.cursor() as cur:
            cur.execute("""
                INSERT INTO Circuito (Melhor_Tempo, Extensão, Nome, Local)
                VALUES (%s, %s, %s, %s)
            """, (melhor_tempo, extensao, nome, local))
            self.con.commit()

    def read_circuito(self, nome, local):
        with self.con.cursor() as cur:
            cur.execute("""
                SELECT * FROM Circuito WHERE Nome = %s AND Local = %s
            """, (nome, local))
            return cur.fetchall()

    def update_circuito(self, melhor_tempo, extensao, nome, local):
        with self.con.cursor() as cur:
            cur.execute("""
                UPDATE Circuito
                SET Melhor_Tempo = %s, Extensão = %s
                WHERE Nome = %s AND Local = %s
            """, (melhor_tempo, extensao, nome, local))
            self.con.commit()

    def delete_circuito(self, nome, local):
        with self.con.cursor() as cur:
            cur.execute("""
                DELETE FROM Circuito WHERE Nome = %s AND Local = %s
            """, (nome, local))
            self.con.commit()
