# Build and Run Docker App Locally

A small Flask web application packaged into a Docker image and run locally.

## Requirements
- Docker Desktop installed and running

## Build the image
```bash
docker build -t docker-local-app:1.0 .
```

## Run the container
```bash
docker run -d --name docker-local-app -p 5000:5000 docker-local-app:1.0
```

Open http://localhost:5000 in your browser.

## Verify
```bash
docker ps
docker logs docker-local-app
```

## Stop and remove the container
```bash
docker stop docker-local-app
docker rm docker-local-app
```

## Deliverable
Capture a screenshot showing the application open at http://localhost:5000 and, ideally, the running container in Docker Desktop or the output of `docker ps`.
