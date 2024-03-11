# docker-compose up -d  --установить и запустить
# docker-compose stop -- остановить

# подсоединиться к БД внутри контейнера:
docker-compose exec db mysql -u root -p

docker-compose exec db /bin/bash