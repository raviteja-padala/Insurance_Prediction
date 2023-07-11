import pymongo
from pymongo.mongo_client import MongoClient
import pandas as pd
import json


uri = "mongodb+srv://raviteja-padala:KING8king@clusterrt.t9f1wi8.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


DATA_FILE_PATH = (r"C:\Users\Lenovo\Desktop\Insurance_Prediction\insurance.csv")

DATABASE_NAME = "INSURANCE"

COLLECTION_NAME = "INSURANCE_PREDICTION_PROJECT"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Shape of df:{df.shape}")

    #Dropping index of DF
    df.reset_index(drop=True, inplace=True)

    #transpose data to key value pair so that it can be inserted to mongo DB
    json_record_insurance = list(json.loads(df.T.to_json()).values())
    print(json_record_insurance[0])

    #inserting data to mongo client
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record_insurance)
    print("DB inserted to MOngoDB")


