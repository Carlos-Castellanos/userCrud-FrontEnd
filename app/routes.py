from urllib import request
from flask import (
    Flask,
    render_template,

)

import requests
from flask import request


URL = "http://127.0.0.1:5001/users"

app = Flask(__name__)

@app.get("/")
def get_index():
    return render_template("index.html")


@app.get("/users")
def display_users():
    user_list = requests.get(URL).json()["users"]
    return render_template("users.html",users=user_list)
#another form:
    # user_list = requests.get(URL).json()
    # return render_template("users.html",users=user_list.get("users"))

@app.get("/user/<int:pk>")
def display_user_profile(pk):
    url = "%s/%s" % (URL,pk)
    user_json = requests.get(url).json()["users"]
    return render_template("user.html", user=user_json)

@app.route('/fdelete')
def form_delete():
    return render_template("fdelete.html")

@app.post('/procesar')
def procesar():

    idUser = request.form.get("iduser")
    print(request.form.get("iduser"))
    url = "%s/%s" % (URL,idUser)
    requests.delete(url)
    return  render_template("index.html")

@app.route('/fcreate')
def form_create():
    return render_template("fcreate.html")

@app.post('/insert')
def insert():
    newUser = {
        "first_name" : request.form.get("first_name"),
        "last_name" : request.form.get("last_name"),
        "hobbies" : request.form.get("hobbies")
    }
    print(newUser)
    requests.post(URL, json=newUser)
    return render_template("index.html")


    