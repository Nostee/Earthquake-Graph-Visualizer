from flask import Flask, render_template,request, url_for
from werkzeug.utils import secure_filename
import os
from os.path import join, dirname, realpath
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

UPLOAD_FOLDER = '/static/assets/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from functions import visualizing_the_data as gg

axis = ''
numberOfFiles = 0

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
    global axis
    global numberOfFiles
    if request.method == 'POST':
        f = request.files['file']
        files = request.files.getlist("file")
        print("HMMMM")
        if(f.filename==''):
            print("EMPTY FILE")
            return render_template("home-choose-data.html")
        else:
            x = 1
            
            for file in files:
                print(file.filename)
                axis = file.filename[-5]
                print("AXIS IS "+axis)
                file.filename = f"data{x}.csv"
                try:
                    file.save("./static/assets/"+file.filename)
                except:
                    pass
                x+=1
            # f.filename = "data.csv"
            # f.save("./static/assets/"+f.filename)

            numberOfFiles = x-1
            date = gg.caller(x,axis)
            print("SUCCESSS")
            return render_template("home-graph.html",given_dates=date)

@app.route('/select_date',methods=['GET', 'POST'])
def selectDate():
    print("Current axis is"+axis)
    print("Current no. of files is"+str(numberOfFiles))
    select = request.form.get('select_dates')
    date = gg.refresh(select,axis,numberOfFiles)
    return render_template("home-graph.html",given_dates=date)


