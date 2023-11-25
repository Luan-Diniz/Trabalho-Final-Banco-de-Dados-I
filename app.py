import psycopg2
import pandas as pd
from specific_queries import SpecificQueries

connection = psycopg2.connect(host="localhost", dbname="formula1",
		user="postgres", password="postgres", port=2023)

cursor = connection.cursor()
our_queries = SpecificQueries(cursor)


isRunning = True

while isRunning:
	#CODE HERE
	print("----------BANCO DE DADOS DA FORMULA1 ---------------")
	print("Selecione o que você quer fazer: ")
	print("\tCONSULTA: Digite 1")
	print("\tOPERAÇÃO EM UMA TABELA: Digite 2")
	print("\tSAIR DO PROGRAMA: Digite 0")
	print()

	user_input = input()
	if user_input == '0':
		isRunning = False
		print("Fechando o programa...")
		continue

	elif user_input == '1':
		print("Qual das seguintes consultas você quer fazer?")
		print("\t CLASSIFICAÇÃO PILOTOS: Digite 1")
		print("\t PATROCINADORES DAS EQUIPES: Digite 2")
		user_input = input()

		if user_input == '1':
			ano_consulta = input("De qual ano?")
			print()
			our_queries.show_pontuation(ano_consulta)

		elif user_input == '2':
			our_queries.not_in_team()
                

	elif user_input == '2':
		pass
	else:
		print("OPERAÇÃO INVÁLIDA!")




connection.commit()
connection.close()
