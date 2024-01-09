Создание образов:
```
docker build -t flask-server server/
docker build -t flask-client client/
```
Запуск контейнеров, связанных по созданной виртуальной сети:
```
docker network create my_network
docker run -d -p 1200:1200 --network=my_network --name server flask-server
docker run -it --network=my_network --name client flask-client
```
Запуск контейнеров с установкой соединения с помощью --link:
```
docker run -d -p 1200:1200 --name server flask-server
docker run -it --link server:server --name client flask-client
```
