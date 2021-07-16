from flask import Flask, render_template,request, url_for
from werkzeug.utils import secure_filename
import os
from os.path import join, dirname, realpath
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

UPLOAD_FOLDER = '/static/assets/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from functions import generate_graph as gg

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def default():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/uploader', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']
        print("HMMMM")
        if(f.filename==''):
            print("EMPTY FILE")
            return render_template("home-choose-data.html")
        else:
            f.filename = "data.csv"
            f.save("./static/assets/"+f.filename)
            gg.plot()
            print("SUCCESSS")
            return render_template("home-graph.html")


