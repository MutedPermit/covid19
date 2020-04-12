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
We're opening the necessary ports as stated on the [documentation](https://docs.mongodb.com/manual/reference/default-mongodb-port/)

## The data
I use the data coming from [this](https://github.com/CSSEGISandData/COVID-19) github repository. Thanks to the Johns Hopkins CSSE.
The data is preprocessed and then stored into the mongo db, in the following format:
```json
{
    "_id" : ObjectId("XXXXXX"),
    "Date" : "1/22/20",
    "Afghanistan" : 0,
    "Albania" : 0,
// ....
    "Zimbabwe" : 0
}
```
## Updating data
To update the data in the mongoDB, do:
```shell script
cd COVID-19
python update_db.py #Please modify the script to update the DB you want
```