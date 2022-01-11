# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, url_for
from website.Home.views import home
from website.Login.views1 import login
from website.Sign_up.views_sign_up import Sign_Up
app = Flask(__name__)
app.register_blueprint(home)
#print(app.url_map)
app.register_blueprint(login,url_prefix="/Login1")
app.register_blueprint(Sign_Up,url_prefix="/Sign_Up")
print(app.root_path)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug= True)
