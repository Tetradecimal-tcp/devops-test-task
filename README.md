# Effective Mobile DevOps Test Task

A simple Docker Compose project with:

- Python HTTP backend on port `8080`
- Nginx reverse proxy on port `80`
- Internal Docker network between `nginx` and `backend`
- Only Nginx is published to the host

## Project structure

```text
.
├── backend/
│   ├── Dockerfile
│   ├── .dockerignore
│   └── app.py
├── nginx/
│   └── nginx.conf
├── docker-compose.yml
├── .gitignore
└── README.md
```

## How it works

```text
User -> localhost:80 -> nginx container -> backend:8080 -> Python HTTP server
```

The backend service is available only inside the Docker network.
The host machine can access only the Nginx container on port `80`.

## Requirements

- Docker
- Docker Compose

## Run

```bash
docker compose up -d --build
```

## Check

```bash
curl http://localhost
```

Expected response:

```text
Hello from Effective Mobile!
```

Optional backend health check through Nginx:

```bash
curl http://localhost/health
```

Expected response:

```text
OK
```

## View logs

```bash
docker compose logs -f
```

Or separately:

```bash
docker logs effective_mobile_backend
docker logs effective_mobile_nginx
```

## Stop

```bash
docker compose down
```

## Notes

- Backend uses a separate `Dockerfile`.
- Backend listens on port `8080`.
- Backend port is not published to the host.
- Nginx uses the official `nginx:1.27-alpine` image.
- Nginx configuration is mounted as a separate file.
- Services communicate by Docker Compose service name: `backend`.
- Backend container runs as a non-root user.
