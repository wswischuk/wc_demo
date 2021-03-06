from flask import Flask, jsonify, request

db = []

app = Flask(__name__)


def add_patient_to_db(name, id, age):
    new_patient = {"name": name, "id": id, "age": age, "tests": []}
    db.append(new_patient)
    print("db is {}".format(db)) #normally print to log file
    return True


def init_database():
    add_patient_to_db("Ann Ables", 101, 35)
    add_patient_to_db("Bob Boyles", 102, 40)
    # Add code to start the logging


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    """
    Receive the posting json
    Verify the json contains the correct keys and data
    If data is bad, reject request with bad status to client
    If data is good, add patient to data base
    Return good status to client
    """
    in_dict = request.get_json()
    check_result = verify_new_patient_information(in_dict)
    if check_result is not True:
        return check_result, 400
    add_patient_to_db(in_dict["name"], in_dict["id"], in_dict["age"])
    return "Patient added", 200


def verify_new_patient_information(in_dict):
    expected_keys = ("name", "id", "age")
    expected_types = (str, int, int)
    for i, key in enumerate(expected_keys):
        if key not in in_dict.keys():
            return "{} key not found".format(key)
        if type(in_dict[key]) is not expected_types[i]:
            return "{} value not correct type".format(key)
    return True


@app.route("/add_test", methods=["POST"])
def post_add_test():
    """
    Receive the posting json
    Verify the json contains the correct keys and data
    Verify that the patient ID exists in database
    If data is bad, reject request with bad status to client
    If data is good, add test results to indicated patient
    Return good status to client
    """
    in_dict = request.get_json()
    check_result = verify_add_test_information(in_dict)
    if check_result is not True:
        return check_result, 400
    if is_patient_in_database(in_dict["id"]) is False:
        return "Patient {} is not found on server".format(in_dict["id"]), 400
    add_result = add_test_to_patient(in_dict)
    if add_result:
        return "Test added to patient id {}".format(in_dict["id"]), 200
    else:
        return "Unknown Problem", 400

def verify_add_test_information(in_dict):
    expected_keys = ("id", "test_name", "test_result")
    expected_types = (int, str, int)
    for i, key in enumerate(expected_keys):
        if key not in in_dict.keys():
            return "{} key not found".format(key)
        if type(in_dict[key]) is not expected_types[i]:
            return "{} value not correct type".format(key)
    return True


def is_patient_in_database(id):
    for patient in db:
        if patient["id"] == id:
            return True
    return False


def add_test_to_patient(in_dict):
    for patient in db:
        if patient["id"] == in_dict["id"]:
            patient["tests"].append((in_dict["test_name"],
                                     in_dict["test_result"]))
            print("db is {}".format(db))
            return True
    return False


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_get_results(patient_id):
    check_result = verify_get_results_input(patient_id)
    if type(check_result) is str:
        return check_result, 400
    answer = generate_test_results_string(check_result)
    if answer is False:
        return "Unknown Error", 400
    else:
        return answer, 200


def verify_get_results_input(patient_id):
    try:
        id = int(patient_id)
    except ValueError:
        return "Bad patient id in URL"
    if is_patient_in_database(id) is False:
        return "Patient id {} does not exist in database".format(id)
    return id


def generate_test_results_string(patient_id):
    for patient in db:
        if patient["id"] == patient_id:
            if len(patient["tests"]) == 0:
                return "No test results available."
            out_string = ""
            for test_results in patient["tests"]:
                out_string += "{}: {}".format(test_results[0],
                                              test_results[1])
            return out_string
    return False


if __name__ == '__main__':
    init_database()
    app.run()


