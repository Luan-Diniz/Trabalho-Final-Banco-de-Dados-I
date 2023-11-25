import psycopg2
import pandas as pd
class SpecificQueries:
    def __init__(self, db_cursor):
        self.cursor = db_cursor
        
    def show_pontuation(self, year):
        column_names = ['Piloto', 'Equipe', 'Pontuação', 'Posição']

        self.cursor.execute(f"""
            SELECT Piloto.Nome, Equipe.Nome, Piloto.Pontos_de_Corrida,
                ROW_NUMBER() OVER (ORDER BY Piloto.Pontos_de_Corrida DESC) AS Position
            FROM Piloto
            JOIN Equipe ON Piloto.idEquipe = Equipe.id_equipe
            WHERE Piloto.Ano_Campeonato = {year}
            GROUP BY Piloto.Nome, Piloto.Pontos_de_Corrida, Equipe.Nome;
            """)

        data = self.cursor.fetchall()
        df = pd.DataFrame(data, columns=column_names)
        print(df.to_string(index=False))
        var = input("---------Aperte ENTER para prosseguir---------")
        print()

    def run_querry2(self):
        #LEFT JOIN AQUI
        #CIRCUITOS QUE NÃO ESTÃO NO CAMPEONATO
        pass
        
    
    def not_in_team(self):
        column_names = ['Equipe', 'Patrocinadores', 'Valor', 'TOTAL FORMULA1']
        
        self.cursor.execute(f"""
            SELECT Equipe.Nome, Patrocinadores.Marca, Patrocinadores.Valor_do_Patrocinio,
            Total_Geral.Total_Patrocinio
            FROM Equipe
            JOIN Patrocinadores ON Equipe.idPatrocinadores = Patrocinadores.id_patrocinador
            CROSS JOIN (
            SELECT SUM(Valor_do_Patrocinio) AS Total_Patrocinio
            FROM Patrocinadores
            ) AS Total_Geral;
           
        """)

        data = self.cursor.fetchall()
        df = pd.DataFrame(data, columns=column_names)
        print(df.to_string(index=False))
        var = input("---------Aperte ENTER para prosseguir---------")
        print()


'''
-3 Consultas envolvendo 2 ou + tabelas. (Devem projetar no mínimo 2 colunas)
-Duas consultas devem ter uma das colunas com uma função de agregação.
-A última deve usar left ou right join


!!! Por amostras dos resultados no relatório

'''
