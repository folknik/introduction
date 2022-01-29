# Docker

Собрать образ на основе файла Dockerfile
```
docker build -t part_03:v1 .
```

Показать все доступные образы
```
docker images
```

Удалить образ
```
docker rmi IMAGE_ID
```

Удалить образы без имени
```
docker image prune
```

Запустить контейнер на основе образа
```
docker run -d --name first_container part_03:v1
```

Показать все запущенные контейнеры
```
docker ps -a
```

Вывести логи запущенного контейнера
```
docker logs CONTAINER_ID 
```

Остановить и сразу удалить запущенный контейнер
```
docker rm -f CONTAINER_ID
```

Исполнить команду внутри работающего контейнера
```
docker exec -it CONTAINER_ID pwd
```

Зайти внутрь работающего контейнера
```
docker exec -it CONTAINER_ID bash
```