from flask import Flask   # from the flask module import the flask class

app = Flask(__name__)   # create an instance of the flask class

@app.get("/")        #flask decorator that maps view functions to routes
def index():           #view function
    me = {              #python dictionary
        "first_name": "George",
        "last_name": "Dick",
        "hobbies": "DIY stuff",
        "is_online": True
    }
    return me   #when you return a dict from a view function,  it becomes JSON