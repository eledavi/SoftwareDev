'''

groups.py
API endpoint for groups.

GET
/api/groups
returns an array of all of the groups in database.
returns error if no groups currently exist

/api/groups?group_name="group_name"
returns: all the information of a group
returns: error if group doesn't exist.

POST
/api/group
Used to create new groups.
preconditions: 'groupDescription' of group. NOTE: not uet implemented.
optional arguments: 'meetDay', 'meetLocation' NOTE: not uet implemented.
returns: a group object
returns: error if group already exists.
NOTE: another way to implement this could be /api/groups?group_name="group_name"
    kind of like the GET method, matter of preference but might be
    good just to differenciate between POST and PUT.

PUT
/api/group
Used to update groups.
preconditions: 'groupDescription' of group. NOTE: not uet implemented.
optional arguments: 'meetDay', 'meetLocation' NOTE: not uet implemented.
returns: a group object
returns: error if group doesn't exists.

'''
import json
import cherrypy
import logging
import random
import string

from sessionManager import sessionScope
from models import Group, User


class Groups:
    logging.basicConfig(format='%(levelname)s:%(asctime)s %(message)s', level=logging.INFO)
    exposed = True

    def GET(self, id=None, group_description=None, meet_time=None, meet_location=None, user_id=None, myLeader=None):
        logging.info('GET request to groups.')

        cherrypy.response.headers['Content-Type'] = 'application/json'

        with sessionScope() as session:
            data = {
                "group_list": []
            }
            query = session.query(Group)
            if group_description is not None:
                query.filter_by(group_description=group_description)
            if meet_time is not None:
                query.filter_by(meet_time=meet_time)
            if meet_location is not None:
                query.filter_by(meet_location=meet_location)
            if user_id is not None:
                query.filter_by(user_id=user_id)
            if myLeader is not None:
                query.filter_by(myLeader=myLeader)
            try:
                for i in query:
                    data['group_list'].append(i.toDict())
            except Exception, e:
                data = {
                    "error": e,
                    "note": "err in query"
                }
                logging.error('Group not found.')
            return json.dumps(data)

    def POST(self):
        logging.info("POST request to groups.")

        cherrypy.response.headers['Content-Type'] = 'application/json'

        try:
            data = json.loads(cherrypy.request.body.read())
        except ValueError:
            logging.error('Json data could not be read.')
            return {"error": "Data could not be read."}

        if "groupDescription" not in data:
            logging.error('group description not found.')
            return {"error": "You must provide a group description."}

        if "myLeader" not in data:
            logging.error('group leader not found.')
            return {"error": "You must provide a group leader."}

        # TODO: Ensure all other fields exist

        with sessionScope() as session:
            # We try to find the group to see if it already exists. If it does, we continue
            # but quit early, if it doesn't, then we 'throw an error', so that we can create
            # a new group.
            try:
                group = session.query(Group).filter_by(group_description=data['groupDescription']).one()
                logging.error("Group already exists!.")
                data = {
                    "error": "Group already exists!",
                    "group": group.toDict()
                }
            except Exception:
                logging.info("Group doesn't yet exist. Creating new one.")
                data = CreateGroup(data, session).toDict()

        return json.dumps(data)

    def PUT(self):
        logging.info("PUT request to groups.")

        cherrypy.response.headers['Content-Type'] = 'application/json'

        try:
            data = json.loads(cherrypy.request.body.read())
        except ValueError:
            logging.error('Json data could not be read.')
            return {"error": "Data could not be read."}

        if "groupDescription" not in data:
            logging.error('group description not found.')
            return {"error": "You must provide a group description."}

        # NOTE: We actually don't care if all of the fields are here
        # because maybe we just want to update ex: meeting time?

        with sessionScope() as session:
            # We try to find the group to see if it already exists. If it does, we continue
            # but quit early, if it doesn't, then we 'throw an error', so that we can create
            # a new group.
            try:
                group = session.query(Group).filter_by(group_description=data['groupDescription']).one()
                logging.info("Group found.")
                updatedGroup = UpdateGroup(group, data, session)
                data = {
                    "oldGroup": group,
                    "updatedGroup": updatedGroup
                }
            except Exception, e:
                logging.error("Group doesn't exist.")
                data = {
                    "error": e,
                    "note": "Group already exists."
                }
        return json.dumps(data)


def CreateGroup(data, session):
    group = Group(id=GenerateId())
    # TODO: These should be validated...
    if "groupDescription" in data:
        setattr(group, "group_description", data["groupDescription"])
    if "meet_time" in data:
        setattr(group, "meet_time", data['meet_time'])
    if "meetLoc" in data:
        setattr(group, "meet_location", data['meetLoc'])

    user = session.query(User).filter_by(id=data['myLeader']).one()
    if "myLeader" in data:
        setattr(group, "myLeader", user)
        group.myMembers = []
        group.myMembers.append(user)

    session.add(group)
    session.commit()
    logging.info("Group created.")
    return group


def UpdateGroup(group, data, session):
    # TODO: These should be validated...
    if "groupDescription" in data:
        setattr(group, "group_description", data["groupDescription"])
    if "meet_time" in data:
        setattr(group, "meet_time", data['meet_time'])
    # TODO: finish other parameters.

    session.add(group)
    session.commit()
    logging.info("Group updated")
    return group


def GenerateId():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(17))
