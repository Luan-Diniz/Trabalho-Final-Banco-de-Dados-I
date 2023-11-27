CREATE TABLE Transmissão (
  Emissora VARCHAR(255),
  Ano INT,
  Comentaristas VARCHAR(255),
  Audiência INT,
  PRIMARY KEY (Emissora)
);
CREATE TABLE Campeonato (
  id_campeonato INT PRIMARY KEY,
  Ano INT,
  Vencedor VARCHAR(255),
  Numero_de_Corridas INT
);
CREATE TABLE Circuito (
  Melhor_Tempo TIME,
  Extensão FLOAT,
  Nome VARCHAR(255),
  Local VARCHAR(255),
  PRIMARY KEY (Nome)
);
CREATE TABLE Equipe (
  Nome VARCHAR(255),
  Sede VARCHAR(255),
  id_equipe INT PRIMARY KEY,
  Diretor VARCHAR(255),
  idPatrocinadores INT
);
CREATE TABLE Piloto (
  Numero_de_pole_positions INT,
  Id_Piloto INT PRIMARY KEY,
  Número_de_Vitórias INT,
  Nome VARCHAR(255),
  Nacionalidade VARCHAR(255),
  Pontos_de_Corrida INT,
  Número_de_Pódios INT,
  idEquipe INT,
  Ano_Campeonato INT
);
CREATE TABLE Carro (
  Trocas_MGU_K INT,
  Trocas_MGU_H INT,
  Numero_do_carro INT PRIMARY KEY,
  idPiloto INT
);
CREATE TABLE Patrocinadores (
  Marca VARCHAR(255),
  Valor_do_Patrocinio FLOAT,
  id_patrocinador INT PRIMARY KEY
);
CREATE TABLE Transmite (
  id_campeonato INT,
  Emissora VARCHAR(255),
  PRIMARY KEY (id_campeonato, Emissora)
);
CREATE TABLE Possui (
  id_campeonato INT,
  Nome VARCHAR(255),
  PRIMARY KEY (id_campeonato, Nome)
);
CREATE TABLE Participa (
  id_equipe INT,
  id_campeonato INT,
  PRIMARY KEY (id_equipe, id_campeonato)
);
-- Foreign Key Constraints
ALTER TABLE Equipe
ADD FOREIGN KEY(idPatrocinadores) REFERENCES Patrocinadores(id_patrocinador);
ALTER TABLE Equipe
ADD UNIQUE (idPatrocinadores);
ALTER TABLE Piloto
ADD FOREIGN KEY(idEquipe) REFERENCES Equipe(id_equipe);
ALTER TABLE Carro
ADD FOREIGN KEY(idPiloto) REFERENCES Piloto(Id_Piloto);
ALTER TABLE Transmite
ADD FOREIGN KEY(id_campeonato) REFERENCES Campeonato(id_campeonato);
ALTER TABLE Transmite
ADD FOREIGN KEY(Emissora) REFERENCES Transmissão(Emissora);
ALTER TABLE Possui
ADD FOREIGN KEY(id_campeonato) REFERENCES Campeonato(id_campeonato);
ALTER TABLE Possui
ADD FOREIGN KEY(Nome) REFERENCES Circuito(Nome);
ALTER TABLE Participa
ADD FOREIGN KEY(id_equipe) REFERENCES Equipe(id_equipe);
ALTER TABLE Participa
ADD FOREIGN KEY(id_campeonato) REFERENCES Campeonato(id_campeonato);
