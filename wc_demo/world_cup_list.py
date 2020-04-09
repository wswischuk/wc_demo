from pymodm import connect, MongoModel, fields


class WC_Team(MongoModel):
    team_name = fields.CharField(primary_key=True)
    opponents = fields.ListField()


def init_db():
    print("Connecting to database...")
    connect("mongodb+srv://bme547student:xbzXZ35Y4&lP@bme547-ba348.mongodb.net"
            "/wc_team?retryWrites=true&w=majority")
    print("Connected to database.")


def add_country():
    new_country = WC_Team(team_name="Mexico")
    new_country.save()


def add_opponent(input_team_name, input_opponent):
    team = WC_Team.objects.raw({"_id": input_team_name}).first()
    team.opponents.append(input_opponent)
    team.save()


def get_opponents(input_team_name):
    team = WC_Team.objects.raw({"_id": input_team_name}).first()
    for opponent in team.opponents:
        print(opponent)
    print("Their second opponent was {}".format(team.opponents[1]))


if __name__ == '__main__':
    init_db()
    get_opponents("Canada")

