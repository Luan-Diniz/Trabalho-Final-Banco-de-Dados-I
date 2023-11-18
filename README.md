# Trabalho-Final-Banco-de-Dados-I
Trabalho final para a matéria Banco de Dados I (UFSC)

Como rodar:
    Para rodar pela primeira vez é necessário:
        1- Construir a imagem Docker:
            docker build -t postgres-formula1 ./

        2- Rodar o container Docker:
            docker run -d --name postgres-formula1-container -p 2023:5432 postgres-formula1
        (A port do container será mapeada para a 2023)

    Um volume é criado, ou seja, as alterações realizadas no BD continuam salvas localmente.

    Alguns comandos úteis:
        docker ps -a    (Lista os containers docker)

    Para parar a execução de um container:
        docker stop id_container
    Para iniciar a execução de um container:
        docker start id_container
    

Para executar a aplicação python:
    1- Esteja com o container docker rodando.
    2- Tenha os requirements.txt instalados.
        (POR COMANDO PARA INSTALAR OS requirements.txt)
    
    3- Executar a aplicação python
        (POR COMANDO PARA EXECUTAR O .py)






Para remover imagens docker:
    docker image rm 'nameOfTheImage'



Para deletar containers, imagens e volumes docker:
    POR COMANDOS AQUI