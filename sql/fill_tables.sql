-- Inserting data into the Patrocinadores table
INSERT INTO Patrocinadores (Marca, Valor_do_Patrocinio, id_patrocinador)
VALUES ('Oracle', 500000000, 1),
       ('Petronas', 75000000, 2),
       ('Santander', 50000000, 3),
       ('Google', 130000000, 4);
       
       
-- Inserting data into the Equipe table
INSERT INTO Equipe (Nome, Sede, id_equipe, Diretor, idPatrocinadores)
VALUES ('Redbull', 'UK', 1, 'Oliver Mintzlaff', 1),
       ('Mercedes', 'Germany', 2, 'Ola Kallenius', 2),
       ('Ferrari', 'Italy', 3, 'Benedetto Vigna', 3),
       ('McLaren', 'UK', 4, 'Zak Brown', 4);
       

-- Inserting data into the Piloto table
INSERT INTO Piloto (Numero_de_pole_positions, Id_Piloto, Número_de_Vitórias, Nome, Nacionalidade, Pontos_de_Corrida, Número_de_Pódios, idEquipe, Ano_Campeonato)
VALUES (31, 1, 53, 'Max Verstappen', 'Belgian', 549 ,97, 1, 2023),
       (3, 2, 6, 'Sergio Perez', 'Mexican', 273, 35, 1, 2023),		
       (104 , 3, 103, 'Lewis Hamilton', 'British', 232, 197, 2, 2023),
       (1, 4, 1, 'George Russel', 'British', 160, 10, 2, 2023),
       (23, 5, 5, 'Charles Leclerc', 'Monegasque', 188, 29, 3, 2023),
       (5, 6, 2, 'Carlos Sainz Jr.', 'Spanish', 200, 18, 3, 2023),
       (1, 7, 0,'Lando Norris', 'British', 195, 13, 4, 2023),
       (0, 8, 0, 'Oscar Piastri', 'Australian', 89, 2, 4, 2023);


-- Inserting data into the Campeonato table
INSERT INTO Campeonato (id_campeonato, Ano, Vencedor, Numero_de_Corridas)
VALUES (1, 2023, 'Max Verstappen', 5);


-- Inserting data into the Circuito table
INSERT INTO Circuito (Melhor_Tempo, Extensão, Nome, Local)
VALUES ('01:18.887', 5.8, 'Monza', 'Italy'),
       ('01:27.369', 5.9, 'Silverstone', 'UK'),
       ('01:47.176', 7, 'Spa-Francorchamps', 'Belgium'),
       ('01:10.540', 4.3, 'Interlagos', 'Brazil'),
       ('01:14.439', 3.3, 'Circuit de Monaco', 'Monaco'),
       ('01:28.139', 5.1, 'Nurburbring Strecke', 'Germany'),
       ('01:32.740', 5.8, 'Circuit Paul Ricard', 'France');
       

-- Inserting data into the Transmissão table
INSERT INTO Transmissão (Emissora, Ano, Comentaristas, Audiência)
VALUES ('Band', 2023, 'Sergio Mauricio, Reginaldo Leme, Felipe Giafone, Mariana Becker', 1800000);


-- Inserting data into the Carro table
INSERT INTO Carro (Trocas_MGU_K, Trocas_MGU_H, Numero_do_carro, idPiloto)
VALUES (3, 3, 1, 1),
       (3, 2, 11, 2),
       (2, 1, 44, 3),
       (2, 2, 63, 4),
       (1, 1, 16, 5),
       (0, 4, 55, 6),
       (3, 2 , 4, 7),
       (3, 1 , 81, 8);
       
    
-- Inserting data into the Transmite table
INSERT INTO Transmite (id_campeonato, Emissora)
VALUES (1, 'Band');


-- Inserting data into the Possui table
INSERT INTO Possui (id_campeonato, Nome)
VALUES (1, 'Monza'),
       (1, 'Silverstone'),
       (1, 'Spa-Francorchamps'),
       (1, 'Interlagos'),
       (1, 'Circuit de Monaco'); 
       

-- Inserting data into the Participa table
INSERT INTO Participa (id_equipe, id_campeonato)
VALUES (1, 1),
       (2, 1),
       (3, 1);
       
       

