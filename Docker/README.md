Crear contenedor docker

En carpeta docker
    docker build -t mi_project1:v1 . 
En carpeta code
    docker volume create webapp
    docker volume ls
    docker volume inspect webapp
    docker container run -d -it -v "$PWD":/home/code --net=host --name school -h oscarrdz --mount source=webapp,target=/app mi_project1:v1

Correr docker
    docker start -i school

