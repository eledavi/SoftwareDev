'''
Cyrille Gindreau
2017

__init__.py

Setup for api

'''
from groups import Groups
from users import Users
from courses import Courses


class ResourceApi:
    course = Courses()
    group = Groups()
    user = Users()
