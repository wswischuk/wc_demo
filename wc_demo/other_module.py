from database import Person


def add_another_person_to_database():
    another_person = Person(first_name="Bob",
                            last_name="Boynton",
                            age=35)
    another_person.save()


def get_all_people():
    all_people = Person.objects.raw({})
    for person in all_people:
        print("{} {}, Age: {}".format(person.first_name,
                                      person.last_name,
                                      person.age))
