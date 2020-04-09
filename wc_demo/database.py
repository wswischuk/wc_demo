from pymodm import connect, MongoModel, fields

class Person(MongoModel):
    first_name = fields.CharField()
    last_name = fields.CharField()
    age = fields.IntegerField()

