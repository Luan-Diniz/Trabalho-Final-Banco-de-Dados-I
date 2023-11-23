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

    Para parar a execução de um container:
        docker stop id_container
    Para iniciar a execução de um container:
        docker start id_container
    

Para executar a aplicação python:
    1- Esteja com o container docker rodando.
    2- Tenha os requirements.txt instalados:          (É aconselhável o uso de um Virtual Environment, embora não necessário)
        pip install -r requirements.txt               (Qualquer erro consulte a documentação oficial das bibliotecas)
    
    3- Executar a aplicação python
        python3 app.py



Para deletar containers, imagens e volumes docker:
    docker ps -a                       (Lista todos os containers)
    docker rm "ID_container"           (Remove o container em específico)

    docker volume ls                   (Lista os volumes docker existentes)
    docker volume rm "nome_volume"     (Remove o volume em específico)

    docker images                      (Lista todas as imagens docker existentes)
    docker image rm "nomeImagem_ou_ID" (Remove a imagem em específico)
