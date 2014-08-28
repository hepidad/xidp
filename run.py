import os, sys, sqlite3
from flask import Flask, g

from flask.ext import restful
from flask.ext.restful import reqparse, abort, Api, Resource

app = Flask(__name__)

api = restful.Api(app)

DATABASE = os.path.join(os.path.dirname( __file__ ), 'xlmsmeDB1.0.db')

@app.route('/')
def homepage():
    return 'Hello, This is xIDP'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

    



@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()




class CourseREST(restful.Resource):
    def get(self):
        db = get_db()
        cur = db.execute('select * from course') #where courseid == courseid order by desc
        entries = cur.fetchall()
        
        courselist={element[0] : element[2] for element in entries}
        
        return courselist 

api.add_resource(CourseREST, '/rest/course/') 
sys.stdout.write(DATABASE)
