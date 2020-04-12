from pymongo import MongoClient
import pandas as pd

HOST = 'localhost'
PORT = 27017
DB_NAME = 'covid19'


def _connect_mongo(host=HOST, port=PORT, username=None, password=None, db=DB_NAME):
    """ A util for making a connection to mongo """

    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)

    return conn[db]


def get_dataframe(collection, db=DB_NAME, query={}, host=HOST, port=PORT, username=None, password=None):
    """
    Connects to mongo database and returns a dataframe
    :param collection: "confirmed", "deaths" or "recovered"
    :param db: name of the database in mongoDB, defaults to 'covid-19'
    :param query: query to perform in mongoDB, defaults to {}
    :param host: host of mongoDB, defaults to localhost
    :param port: port of mongoDB, defaults to 27017
    :param username: username for mongoDB, defaults to None
    :param password: password for mongoDB, defaults to None
    :return:
    """

    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query)

    # Expand the cursor and construct the DataFrame
    df = pd.DataFrame(list(cursor))

    # Delete the _id
    del df['_id']

    # Set date as index
    df.set_index("Date")

    return df
