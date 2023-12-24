# Service

## Code environment
- Python 3.11.2
- PostgreSQL 14

## Migration

```
$ cd devops/docker
$ docker compose up -d db
```

Run 2 file in these DB
- `devops/db_migration/1_create_table.sql` to create table
- `devops/db_seeds/1_seed_data.sql` to populate data (10M employees)

## Build docker image for service
```
$ docker build -f devops/docker/Dockerfile -t service:latest .
```

## Run
```
$ cd devops/docker
$ docker compose up -d service
```

- Go to `http://localhost:8000/docs` to check Open API docs and test API

## Dynamic columns
- In `devops/docker/docker-compose.yml`, uncomment `SERVICE_EXCLUDE_EMPLOYEE_FIELDS=email,phone_number` to exclude 2 field email and phone_number
- Run below commands again and test with open api
```
$ cd devops/docker
$ docker compose up -d service
```

## Rate-limitting
- Install and use [wrk](https://github.com/wg/wrk) to test, only 2 api success, other would be failed
```
$ wrk -t 3 -c 3 -d 2s http://localhost:8000/health
```