
## Running from docker-compose

```shell
# Choose btw rabbit or redis as a celery broker:
export COMPOSE_FILE=docker-compose-rabbit.yaml
export COMPOSE_FILE=docker-compose-redis.yaml
docker compose up -d
docker compose exec celery python /app/celery_broken_multiprocessing_repro.py
```
