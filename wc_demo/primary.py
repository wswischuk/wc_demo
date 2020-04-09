from pymodm import connect, MongoModel, fields


class Person(MongoModel):
    first_name = fields.CharField()
    last_name = fields.CharField()
    age = fields.IntegerField()


def init_db():
    print("Connecting to database...")
    connect("mongodb+srv://wswischuk:germanyowns90@bme547nws-wp54a.mongodb"
            ".net"
            "/test?retryWrites=true&w=majority")
    print("Connected to database.")


def add_person_to_database(first_name_arg, last_name_arg, age_arg):
    new_person = Person(first_name=first_name_arg,
                        last_name=last_name_arg,
                        age=age_arg)
    new_person.save()
    return


if __name__ == '__main__':
    init_db()
    add_person_to_database("Ann", "Ables", 35)