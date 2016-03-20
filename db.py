# all of our DB stuff goes into this file.

import peewee

database = peewee.SqliteDatabase("sqlite3.db")

class basetable(peewee.Model):
    class Meta:
        database = database

class filescan(basetable):
    host = peewee.CharField()
    path = peewee.CharField()
    hash = peewee.CharField()

database.connect()
database.create_tables([filescan],    safe=True)
