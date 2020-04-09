class Person:
    first_name = None
    last_name = None
    age = None
    minor = None

    """
    Add a function to print first and last name on the same line
    Add a function to return True/False if the person is a minor
    """
    def __init__(self, first_name_arg=None, last_name_arg=None, age_arg=None):
        self.first_name = first_name_arg
        self.last_name = last_name_arg
        self.age = age_arg
        self.minor = True if self.age < 18 else False
        self._weight = 0

    def print_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def increase_age(self, number_of_years=1):
        self.age = self.age + number_of_years

    def print_all_info(self):
        full_name = self.print_full_name()
        print("Patient name is {}".format(full_name))
        print("Age is {}".format(self.age))
        print("Is minor?: {}".format(self.minor))
        print("Weight is {}".format(self._weight))

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight_input):
        if weight_input < 0:
            weight_input = -weight_input
        self._weight = weight_input


def create_person(first, last, age):
    new_person = Person(first, last, age)
    # new_person.first_name = "Bob"
    # new_person.last_name = "Anderson"
    # new_person.age = 30
    return new_person


def print_patient_info(pat):
    print("First name is {}".format(pat.first_name))
    print("Last name is {}".format(pat.last_name))
    print("Age is {}".format(pat.age))


def age_patient(pat):
    pat.age = pat.age + 1
    return pat


def main():
    db = list()
    x = create_person("Bob", "Anderson", 30)
    x.weight = -150
    db.append(x)
    y = create_person("Jane", "Smith", 45)
    y.weight = 150
    db.append(y)
    z = create_person("Michael", "Wong", 10)
    z.weight = 60
    db.append(z)
    for patient in db:
        patient.print_all_info()
    x.weight = 140
    x.weight += 2
    print(x.weight)
#    print_patient_info(x)
#    x.increase_age(10)
#    print_patient_info(x)
#    print(dir(x))
#    y = Person()
#    print(y.first_name)


if __name__ == '__main__':
    main()

