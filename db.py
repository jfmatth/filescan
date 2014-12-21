###
### db.py - This file maintains all DB functions to Initialize and open the tables and databases.    
###
import peewee
import argparse
from argparse import Action

db = peewee.SqliteDatabase('files.db')

class File(peewee.Model):
    host = peewee.CharField()
    file = peewee.CharField()
    hash = peewee.CharField(unique=True)
    
    class Meta:
        database = db

def Init():
        print("Initializing Database") 
        db.connect()
        db.create_tables([File], safe=True)
        
if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-I", "--init", help="Initialize the database", action="store_true")
    args = parser.parse_args()

    if args.init:   
        Init()
