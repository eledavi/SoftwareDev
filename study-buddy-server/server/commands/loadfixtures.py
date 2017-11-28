'''
Cyrille Gindreau
2017

loadfixtures.py

Sends test data to api.
'''
import requests
import json
import logging

logging.basicConfig(format='%(levelname)s:%(asctime)s %(message)s', level=logging.INFO)

baseUrl = "http://localhost:5000/api/"


def loadfixtures():

    # Create test group
    testUser = {
        'email': "someone@something.com",
        'firstName': "John",
        'lastName': "Smith",
        'password': "ChangeMe",
        'university': "Life",
        'major': "Badassery",
        'rating': 5.0
    }

    # Make post
    logging.info("Sending put for testUser")
    response = requests.post("{}user".format(baseUrl), json.dumps(testUser))
    logging.debug("Response was: {}".format(response))

    users = requests.get("{}user".format(baseUrl)).json()
    logging.info(json.dumps(users, indent=4))

    # Create test group
    testGroup1 = {
        'groupDescription': "CS_498",
        'meet_time': "Mon6:00PM,Fri4:00PM",
        'meetLoc': "Zuhl_Library",
        'myLeader': users['user_list'][0]['userId']
    }
    # Create test group
    testGroup2 = {
        'groupDescription': "Math_191",
        'meet_time': "Mon6:00PM,Fri4:00PM",
        'meetLoc': "Zuhl_Library",
        'myLeader': users['user_list'][0]['userId']
    }

    # Make post
    logging.info("Sending post for testGroup")
    response = requests.post("{}group".format(baseUrl), json.dumps(testGroup1))
    logging.debug("Response was: {}".format(response))

    # Make post
    logging.info("Sending post for testGroup")
    response = requests.post("{}group".format(baseUrl), json.dumps(testGroup2))
    logging.debug("Response was: {}".format(response))

    # Get groups
    groups = requests.get("{}group".format(baseUrl)).json()
    logging.info(json.dumps(groups, indent=4))


    # updateUser = {
    #     'groups': []
    # }
    #
    # for i in groups:
    #     updateUser['groups'].append(i['groupId'])
    #
    # # update user with new groups
    # response = requests.put("{}user".format(baseUrl), json.dumps(updateUser))
    #
    # logging.debug("Response was: {}".format(response))
