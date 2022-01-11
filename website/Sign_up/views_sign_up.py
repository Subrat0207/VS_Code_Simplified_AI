from flask import Flask , render_template, Blueprint ,url_for, redirect, request , flash

Sign_Up = Blueprint("sign_up",__name__,static_folder = "static", static_url_path='/Sign_up/static',template_folder="templates")

@Sign_Up.route("/", methods=['GET','POST'])

def Sign_up_def():
    print("am in sign_uo")

    return render_template("Sign_up.html")
