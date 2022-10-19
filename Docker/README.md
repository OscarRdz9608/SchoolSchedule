Crear contenedor docker

En carpeta docker
    docker build -t mi_project1:v1 . 
En carpeta code
    docker volume create webapp
    docker volume ls
    docker volume inspect webapp
    docker container run -d -it -v "$PWD":/home/code --net=host --name project_1 -h oscarrdz --mount source=webapp,target=/app mi_project1:v1

Correr docker
    docker start -i project_1


Create a virtual environment

This can be done with python -m venv env

activate the virtual environment with

env/bin/activate

or

env\Scripts\activate

Install the requirements

pip install -r requirements.txt

Create the database

python create_db.py


en archivo datebase cambiar credenciales

REPO REFERENCIA    https://github.com/jod35/Build-a-fastapi-and-postgreSQL-API-with-SQLAlchemy