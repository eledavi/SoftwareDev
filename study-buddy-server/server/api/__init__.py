'''

__init__.py

Setup for api

'''
from groups import Groups
from users import Users
from courses import Courses


class ResourceApi:
    # course = Courses()
    groups = Groups()
    users = Users()
    courses = Courses()
