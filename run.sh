docker rm hf-api-pod
docker rmi hf-api
docker build --no-cache -t hf-api .
docker run -dit --name hf-api-pod -p 8000:8000 hf-api
