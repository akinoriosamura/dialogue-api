docker stop dialogue-api
docker rm dialogue-api
docker rmi -f `docker images dialogue-api_dialogue-api`
docker-compose up -d 