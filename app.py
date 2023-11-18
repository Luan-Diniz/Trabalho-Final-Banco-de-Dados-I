import psycopg2

connection = psycopg2.connect(host="localhost", dbname="formula1",
        user="postgres", password="postgres", port=2023)
    
cursor = connection.cursor()


#CODE HERE
teste = input("Type 0 to create a table Ararangua")

if teste == "0":
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Ararangua(
            name VARCHAR(255)
        );
    """)

connection.commit()
connection.close()