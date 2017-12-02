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
    testGroup = {
        'groupDescription': "Math 191",
        'meetDay': "Mon 6:00PM, Fri 4:00PM",
        'meetLoc': "Zuhl Library",
    }

    # Make post
    logging.info("Sending put for testGroup")
    # "{}group".format(baseUrl) == "http://localhost:5000/api/group"
    response = requests.post("{}group".format(baseUrl), json.dumps(testGroup))
    logging.debug("Response was: {}".format(response))

    # Create test group
    testGroup = {
        'groupDescription': "CS 498",
        'meetDay': "Mon 6:00PM, Fri 4:00PM",
        'meetLoc': "Zuhl Library",
    }

    # Make post
    logging.info("Sending put for testGroup")
    response = requests.post("{}group".format(baseUrl), json.dumps(testGroup))
    logging.debug("Response was: {}".format(response))

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
