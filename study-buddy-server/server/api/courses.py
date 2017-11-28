# '''
#
# courses.py
# API endpoint for courses.
#
# GET
# /api/courses
# returns an array of all of the courses in database.
# returns error if no courses currently exist
#
# /api/courses?course_name="course_name"
# returns: all the information of a course
# returns: error if course doesn't exist.
#
# POST
# /api/courses
# Used to create new courses.
# preconditions: 'courseDescription' of course. NOTE: not yet implemented.
# returns: a course object
# returns: error if course already exists.
# NOTE: another way to implement this could be /api/courses?course_name="course_name"
#     kind of like the GET method, matter of preference but might be
#     good just to differenciate between POST and PUT.
#
# PUT
# /api/courses
# Used to update courses.
# preconditions: 'courseDescription' of course. NOTE: not yet implemented.
# returns: a course object
# returns: error if course doesn't exists.
#
# '''
# import json
# import cherrypy
# import logging
# import random
# import string
#
# from sessionManager import sessionScope
# # from models import Course
#
#
# class Courses:
#     logging.basicConfig(format='%(levelname)s:%(asctime)s %(message)s', level=logging.INFO)
#     # this just means this is open to the public
#     exposed = True
#
#     def GET(self, course_name=None):
#         logging.info('GET request to courses.')
#
#         cherrypy.response.headers['Content-Type'] = 'application/json'
#
#         with sessionScope() as session:
#             if course_name is None:
#                 data = {
#                     "course_list": []
#                 }
#                 try:
#                     objs = session.query(course)
#                 except Exception, e:
#                     data = {
#                         "error": e,
#                         "note": "No courses currently exist in database."
#                     }
#                     logging.error('No courses exist.')
#                 for i in objs:
#                     data['course_list'].append(i.toDict())
#             else:
#                 try:
#                     course = session.query(course).filter_by(name=course_name).one()
#                     data = course.toDict()
#                 except Exception, e:
#                     data = {
#                         "error": e,
#                         "note": "course not found."
#                     }
#                     logging.error('course not found.')
#             return json.dumps(data)
#
#     def POST(self):
#         logging.info("POST request to courses.")
#
#         cherrypy.response.headers['Content-Type'] = 'application/json'
#
#         try:
#             data = json.loads(cherrypy.request.body.read())
#         except ValueError:
#             logging.error('Json data could not be read.')
#             return {"error": "Data could not be read."}
#
#         if "courseDescription" not in data:
#             logging.error('course description not found.')
#             return {"error": "You must provide a course description."}
#
#         # TODO: Ensure all other fields exist
#
#         with sessionScope() as session:
#             # We try to find the course to see if it already exists. If it does, we continue
#             # but quit early, if it doesn't, then we 'throw an error', so that we can create
#             # a new course.
#             try:
#                 course = session.query(course).filter_by(course_description=data['courseDescription']).one()
#                 logging.error("course already exists!.")
#                 data = {
#                     "error": "course already exists!",
#                     "course": course.toDict()
#                 }
#             except Exception:
#                 logging.info("course doesn't yet exist. Creating new one.")
#                 data = Createcourse(data, session).toDict()
#         return json.dumps(data)
#
#     def PUT(self):
#         logging.info("PUT request to courses.")
#
#         cherrypy.response.headers['Content-Type'] = 'application/json'
#
#         try:
#             data = json.loads(cherrypy.request.body.read())
#         except ValueError:
#             logging.error('Json data could not be read.')
#             return {"error": "Data could not be read."}
#
#         if "courseDescription" not in data:
#             logging.error('course description not found.')
#             return {"error": "You must provide a course description."}
#
#         # NOTE: We actually don't care if all of the fields are here
#         # because maybe we just want to update ex: meeting time?
#
#         with sessionScope() as session:
#             # We try to find the course to see if it already exists. If it does, we continue
#             # but quit early, if it doesn't, then we 'throw an error', so that we can create
#             # a new course.
#             try:
#                 course = session.query(course).filter_by(course_description=data['courseDescription']).one()
#                 logging.info("course found.")
#                 updatedcourse = Updatecourse(course, data, session)
#                 data = {
#                     "oldcourse": course,
#                     "updatedcourse": updatedcourse
#                 }
#             except Exception, e:
#                 logging.error("course doesn't exist.")
#                 data = {
#                     "error": e,
#                     "note": "course already exists."
#                 }
#         return json.dumps(data)
#
#
# def Createcourse(data, session):
#     course = course(course_id=GenerateId())
#     # TODO: These should be validated...
#     if "courseDescription" in data:
#         setattr(course, "course_description", data["courseDescription"])
#     if "meetDate" in data:
#         setattr(course, "meet_date", data['meetDate'])
#     # TODO: finish other parameters.
#
#     session.add(course)
#     session.commit()
#     logging.info("course created.")
#     return course
#
#
# def Updatecourse(course, data, session):
#     # TODO: These should be validated...
#     if "courseDescription" in data:
#         setattr(course, "course_description", data["courseDescription"])
#     if "meetDate" in data:
#         setattr(course, "meet_date", data['meetDate'])
#     # TODO: finish other parameters.
#
#     session.add(course)
#     session.commit()
#     logging.info("course updated")
#     return course
#
#
# def GenerateId():
#     return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(17))
