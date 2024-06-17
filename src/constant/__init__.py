import os


AWS_S3_BUCKET_NAME = "wafer-fault"
MONGO_DATABASE_NAME = "pwskills"
MONGO_COLLECTION_NAME = "waferfault"

TARGET_COLUMN = "quality"
MONGO_DB_URL= "mongodb://guptalaksh8:abcd@ac-89qss6f-shard-00-00.qrrmr5y.mongodb.net:27017,ac-89qss6f-shard-00-01.qrrmr5y.mongodb.net:27017,ac-89qss6f-shard-00-02.qrrmr5y.mongodb.net:27017/?ssl=true&replicaSet=atlas-rwdh1c-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder =  "artifacts"