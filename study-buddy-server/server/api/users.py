'''

users.py
API endpoint for users.

GET
/api/users
returns an array of all of the users in database.
returns error if no users currently exist

/api/users?user_name="user_name"
returns: all the information of a user
returns: error if user doesn't exist.

POST
/api/users
Used to create new users.
preconditions: 'userDescription' of user. NOTE: not uet implemented.
optional arguments: 'meetDay', 'meetLocation' NOTE: not uet implemented.
returns: a user object
returns: error if user already exists.
NOTE: another way to implement this could be /api/users?user_name="user_name"
    kind of like the GET method, matter of preference but might be
    good just to differenciate between POST and PUT.

PUT
/api/users
Used to update users.
preconditions: 'userDescription' of user. NOTE: not uet implemented.
optional arguments: 'meetDay', 'meetLocation' NOTE: not uet implemented.
returns: a user object
returns: error if user doesn't exists.

'''
import json
import cherrypy
import logging
import random
import string

from sessionManager import sessionScope
from models import User, Group


class Users:
    logging.basicConfig(format='%(levelname)s:%(asctime)s %(message)s', level=logging.INFO)
    exposed = True

    def GET(self, user_name=None):
        logging.info('GET request to users.')

        cherrypy.response.headers['Content-Type'] = 'application/json'

        with sessionScope() as session:
            if user_name is None:
                data = {
                    "user_list": []
                }

                objs = session.query(User)
                for i in objs:
                    data['user_list'].append(i.toDict())
            else:
                try:
                    user = session.query(User).filter_by(firstName=user_name).one()
                    data = user.toDict()
                except Exception, e:
                    data = {
                        "error": e,
                        "note": "user not found."
                    }
                    logging.error('user not found.')
            return json.dumps(data)

    def POST(self):
        logging.info("POST request to users.")

        cherrypy.response.headers['Content-Type'] = 'application/json'

        try:
            data = json.loads(cherrypy.request.body.read())
        except ValueError:
            logging.error('Json data could not be read.')
            return {"error": "Data could not be read."}

        if "firstName" not in data:
            logging.error('user first name not found.')
            return {"error": "You must provide a user firstName."}

        if "lastName" not in data:
            logging.error('user last name not found.')
            return{"error": "You must provide a user lastName."}

        if "email" not in data:
            logging.error('user email not found.')
            return{"error": "You must provide a user email."}

        if "password" not in data:
            logging.error('user password not found.')
            return{"error": "You must provide a user password."}

        if "university" not in data:
            logging.error('user university not found.')
            return{"error": "You must provide a user university."}

        if "major" not in data:
            logging.error('user major not found.')
            return{"error": "You must provide a user major."}




        with sessionScope() as session:
            # We try to find the user to see if it already exists. If it does, we continue
            # but quit early, if it doesn't, then we 'throw an error', so that we can create
            # a new user.
            try:
                user = session.query(User).filter_by(first_name=data['firstName']).one()
                logging.error("user already exists!.")
                data = {
                    "error": "user already exists!",
                    "user": user.toDict()
                }
            except Exception:
                logging.info("user doesn't yet exist. Creating new one.")
                data = CreateUser(data, session).toDict()
        return json.dumps(data)

    def PUT(self):
        logging.info("PUT request to users.")

        cherrypy.response.headers['Content-Type'] = 'application/json'

        try:
            data = json.loads(cherrypy.request.body.read())
        except ValueError:
            logging.error('Json data could not be read.')
            return {"error": "Data could not be read."}

        if "firstName" not in data:
            logging.error('user firstName not found.')
            return {"error": "You must provide a user firstName."}

        # NOTE: We actually don't care if all of the fields are here
        # because maybe we just want to update ex: meeting time?

        with sessionScope() as session:
            # We try to find the user to see if it already exists. If it does, we continue
            # but quit early, if it doesn't, then we 'throw an error', so that we can create
            # a new user.
            try:
                user = session.query(User).filter_by(first_name=data['firstName']).one()
                logging.info("user found.")
                updatedUser = UpdateUser(user, data, session)
                data = {
                    "olduser": user,
                    "updateduser": updatedUser
                }
            except Exception, e:
                logging.error("user doesn't exist.")
                data = {
                    "error": e,
                    "note": "user already exists."
                }
        return json.dumps(data)


def CreateUser(data, session):
    user = User(id=GenerateId())
    # TODO: These should be validated...
    if "firstName" in data:
        setattr(user, "first_name", data["firstName"])
    if "lastName" in data:
        setattr(user, "last_name", data['lastName'])
    if "email" in data:
        setattr(user, "email", data['email'])
    if "password" in data:
        setattr(user, "password", data['password'])
    if "university" in data:
        setattr(user, "university", data['university'])
    if "major" in data:
        setattr(user, "major", data['major'])
    if "rating" in data:
        setattr(user, "rating", data['rating'])


    session.add(user)
    session.commit()
    logging.info("user created.")
    return user


def UpdateUser(user, data, session):
    # TODO: These should be validated...
    if "firstName" in data:
        setattr(user, "first_name", data["firstName"])
    if "lastName" in data:
        setattr(user, "last_name", data['lastName'])
    # if "groups" in data:
    #     for i in data['groups']:
    #         try:
    #             group = session.query(Group).filter_by(group_description=i)
    #             user.groups.append(group)
    #         except Exception, e:
    #             logging.error(e)
    # TODO: finish other parameters.

    session.add(user)
    session.commit()
    logging.info("user updated")
    return user


def GenerateId():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(17))
