docker build -t microservice .
docker run --env-file .env -p 3000:3000 -it microservice
