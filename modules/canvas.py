import strings
import config
import requests


BASE_URL = strings.URLS["canvas"]
courses = {}
assignments = {}

def populateCourses():
    url = BASE_URL + "?access_token=" + config.APIKEYS["canvas"]
    response = requests.get(url).json()

    for c in response:
        if "name" in c and "id" in c:
            if "Fall 2022" in c["name"]:
                courses[str(c["id"])] = c["name"]

def populateAssignments():
    if not courses:
        populateCourses()
    for key, value in courses.items():
        url = BASE_URL + "/" + key + "/assignments?access_token=" + config.APIKEYS["canvas"]
        response = requests.get(url).json()
        
        for assignment in response:
            if assignment["locked_for_user"] or "Roll Call" in assignment["name"]:
                continue
            if value not in assignments.keys():
                assignments[value] = []
            assignments[value].append(assignment["name"])

def getAssignments():
    if not assignments:
        populateAssignments()
    return assignments

def getCourses():
    if not courses:
        populateCourses()
    return courses.values()

populateAssignments()