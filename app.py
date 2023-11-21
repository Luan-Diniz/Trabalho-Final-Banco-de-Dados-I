import psycopg2

connection = psycopg2.connect(host="localhost", dbname="formula1",
        user="postgres", password="postgres", port=2023)
    
cursor = connection.cursor()



isRunning = True

'''
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
		continue
	elif user_input == '1':
		pass
	elif user_input == '2':
		pass
	else:
		print("OPERAÇÃO INVÁLIDA!")
'''


'''
teste = input("Type 0 to create a table Ararangua")

if teste == "0":
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Ararangua(
            name VARCHAR(255)
        );
    """)
'''

connection.commit()
connection.close()
