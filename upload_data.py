from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb://guptalaksh8:abcd@ac-89qss6f-shard-00-00.qrrmr5y.mongodb.net:27017,ac-89qss6f-shard-00-01.qrrmr5y.mongodb.net:27017,ac-89qss6f-shard-00-02.qrrmr5y.mongodb.net:27017/?ssl=true&replicaSet=atlas-rwdh1c-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"


# Create a new client and connect to the server
client = MongoClient(uri)

# create database name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault"

# read the data as a dataframe
df=pd.read_csv(r"/Users/gupta/Desktop/sensor2-main/notebooks/wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)

# Convert the data into json
json_record=list(json.loads(df.T.to_json()).values())

#now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
