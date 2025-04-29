# Web-game
Reading club web game 

# Run local development server
run_server.bat

## Run docker on Linux core

Run docker database localy:

1. Download Docker from https://www.docker.com (NOTE: to run Docker on Windows you have to have WSL2)
2. Open console in the folder where is `docker-compose.yaml`
3. Run `docker compose up -d`


Add credentials to the postgre 
`echo "postgres:5432:*:admin:admin" > pgpass`

Change permission to pgpass
`chmod 600 pgpass`


## API requests - where to write

New api requests: 

`flask_app/server/api/routes.py`
