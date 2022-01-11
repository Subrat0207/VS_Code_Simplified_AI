from flask import Flask , render_template, Blueprint ,url_for, redirect

login = Blueprint("login",__name__,static_folder = "static", static_url_path='/Login/static',template_folder="templates")

@login.route("/")

def login_def():
    return render_template("Login.html")
