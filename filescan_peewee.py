import peewee

db = peewee.SqliteDatabase('files.db')

class File(peewee.Model):
    host = peewee.CharField()
    file = peewee.CharField()
    hash = peewee.CharField(unique=True)
    
    class Meta:
        database = db

db.connect()    
db.create_tables([File], True)