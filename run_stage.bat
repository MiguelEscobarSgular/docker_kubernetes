docker stop api-rest || true && docker rm api-rest || true

docker run -itd --name api-rest -p 3000:3000 dockermigan/miappcdk-ago22:1.0