# Development Environment

## Basic Usage
1. First run **`make build`** inside root directory.
2. Then run **`make up`** to start up the project for first time.
3. Use/update environment variables from [**`.envs`**](https://github.com/ruddra/docker-django/blob/master/.envs) folder.

Checkout the [commands](#commands) section for more usage.

## Commands
To use this project, run this commands:

1. `make up` to build the project and starting containers.
2. `make build` to build the project.
3. `make start` to start containers if project has been up already.
4. `make stop` to stop containers.
5. `make shell-web` to shell access web container.
6. `make shell-db` to shell access db container.
7. `make shell-nginx` to shell access nginx container.
8. `make logs-web` to log access web container.
9. `make logs-db` to log access db container.
10. `make logs-nginx` to log access nginx container.
11. `make collectstatic` to put static files in static directory.
12. `make log-web` to log access web container.
13. `make log-db` to log access db container.
14. `make log-nginx` to log access nginx container.
15. `make restart` to restart containers.

 docker-compose build --force --no-cache
 
## Create Admin Django
make shell-web
python manage.py createsuperuser


python manage.py dbshell
DROP SCHEMA public CASCADE; CREATE SCHEMA public; GRANT ALL ON SCHEMA public TO public;

python manage.py migrate sessions

# Technical Document

## DB Diagrams

## Architecture

### Session Management

### Poll

### BackChannel


