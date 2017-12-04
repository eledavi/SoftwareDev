#!/usr/bin/env python
import cherrypy
import os
import sys
import jinja2
from sqlalchemy import create_engine

import models
from api import ResourceApi
# from commands import Command

# Handle cross platform system paths.
PATH = os.path.abspath(os.path.dirname(__file__))
STATIC = os.path.join(PATH, '../static')
sys.path.append(PATH)

# Point to the public directory of what can be served.
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(searchpath=os.path.join(PATH, '../static/')), )


def get_cp_config():
    # /: If we wanted to serve an html page, it would start from this location
    # /api: where all of our db hits will go through.
    config = {
        '/': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': STATIC,
            'tools.sessions.on': True
        },
        '/api': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        },
    }
    return config


class Root(object):
    # Point to our api.
    api = ResourceApi()

    # Expose our index for testing.
    @cherrypy.expose
    def index(self):
        # If we need to send extra data to our index, we could put it in context.
        context = {}
        t = env.get_template("index.html")
        return t.render(context)


def RunServer():
    # Create/open the database
    open('studyBuddyDB.db', 'a').close()
    print "db opened."
    dbURL = 'sqlite:///studyBuddyDB.db'
    # Use sqlalchemy engine.
    db = create_engine(dbURL)

    print "Initializing database tables..."
    models.Base.metadata.create_all(db)

    # Cherrypy setup.
    cherrypy.tree.mount(Root(), '/', config=get_cp_config())
    cherrypy.server.socket_host = "0.0.0.0"
    cherrypy.server.socket_port = int(os.environ.get('PORT', 5000))
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == "__main__":
    # run 'python server.py' to start the server.
    # run 'python server.py loadfixtures' to generate sample data.
    args = sys.argv
    if len(args) > 1:
        arg = "{}".format(args[1]).lower()
        if(arg == "loadfixtures"):
            print "loading fixtures"
            Command.LoadFixtures()
        else:
            print 'Did not understand the command, please try again.'
    else:
        print "starting server!"
        RunServer()
