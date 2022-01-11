from flask import Flask ,render_template , url_for , Blueprint

home = Blueprint('home', __name__,static_folder="static", static_url_path='/Home/static',template_folder ="templates")
print('?*************************')
print(home.root_path)
@home.route("/")
@home.route("/Home")
def Home_def():
    return render_template("Home.html")

