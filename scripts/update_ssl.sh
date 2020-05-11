docker stop counselor-ssl-prod
docker rm counselor-ssl-prod
docker rmi -f `docker images steveltn/https-portal`
sudo docker-compose up -d
