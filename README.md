# perktree

Interactive DnD perktree written with django, vue and d3

## How to run

### Docker
The easiest way to run it is using docker-compose.

1. Create a `.env` file with the following entries
```
SECRET_KEY=[long random string]
DJANGO_ADMIN_USER=[username]
DJANGO_ADMIN_MAIL=[email]
DJANGO_ADMIN_PASS=[password]
DB_PASSWORD=[database-password]
```

2. Build the images with `docker-compose build`
3. Run it with `docker-compose up -d`
4. Set up a reverse proxy pointing to the port set in docker-compose.yml (8019 by default), or change the port to 80 (There is no ssl support inside the container as of now)

### Normal

1. Build the frontend
```
cd frontend
yarn/npm install
yarn/npm build
```

2. Install backend requirements from the pipfile using your python package manager of choice (though you should really use pipenv)
3. Set up a database (postgresql is recommended, though myql should work)
4. Edit thes entrypoint.sh script in the backend directory to add all the necessary env variables (you can find them in the docker-compose.yml file)
5. Run the backend using the entrypoint.sh script
6. Set up a web server to serve the frontend static files and proxy requests to the backend. A sample configuration can be found in nginx.conf

Though I do recommend running it with docker, as it's much easier to set up and maintain.

4.
