docker stop counselor-api-prod counselor-nginx-prod counselor-ssl-prod
docker rm counselor-api-prod counselor-nginx-prod counselor-ssl-prod
docker rmi -f `docker images chat-councelor_counselor-api-prod`
docker rmi -f `docker images chat-councelor_counselor-nginx-prod`
docker rmi -f `docker images steveltn/https-portal`
docker-compose up -d 
