# Mongo DB
I'm using a mongoDB running in a Docker container.

## Set up of MongoDB
To set up the mongoDB running on a Docker container we use the docker image in docker hub.
```bash
docker pull mongo:4.0.4
```
And then we're running the image as follows:
```bash
docker run -d -p 27017-27019:27017-27019 --name mongodb-covid mongo:4.0.4
```
We're opening the necessary ports as stated on the [documentationn](https://docs.mongodb.com/manual/reference/default-mongodb-port/)
