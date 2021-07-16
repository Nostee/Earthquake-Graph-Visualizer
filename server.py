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
            date,dataToInterpret = gg.caller(x,axis)
            print("SUCCESSS")
            if(len(dataToInterpret)==7):
                axis = dataToInterpret[0]
                currentDate = dataToInterpret[1]
                ave = dataToInterpret[2]
                lowAcce = dataToInterpret[3]
                lowTime = dataToInterpret[4]
                highAcce = dataToInterpret[5]
                highTime = dataToInterpret[6]


                return render_template("home-graph.html",given_dates=date,
                axis=axis,
                currentDate=currentDate,
                ave=ave,
                lowAcce=lowAcce,
                lowTime=lowTime,
                highAcce=highAcce,
                highTime=highTime
                )
            else:
                # For X
                axisX = dataToInterpret[0][0]
                currentDateX = dataToInterpret[0][1]
                aveX = dataToInterpret[0][2]
                lowAcceX = dataToInterpret[0][3]
                lowTimeX = dataToInterpret[0][4]
                highAcceX = dataToInterpret[0][5]
                highTimeX = dataToInterpret[0][6]
                # For Y
                axisY = dataToInterpret[1][0]
                currentDateY = dataToInterpret[1][1]
                aveY = dataToInterpret[1][2]
                lowAcceY = dataToInterpret[1][3]
                lowTimeY = dataToInterpret[1][4]
                highAcceY = dataToInterpret[1][5]
                highTimeY = dataToInterpret[1][6]
                # For Z
                axisZ = dataToInterpret[2][0]
                currentDateZ = dataToInterpret[2][1]
                aveZ = dataToInterpret[2][2]
                lowAcceZ = dataToInterpret[2][3]
                lowTimeZ = dataToInterpret[2][4]
                highAcceZ = dataToInterpret[2][5]
                highTimeZ = dataToInterpret[2][6]

                pga = (float(highAcceX)+float(highAcceY))/2
                print("PGA IS "+str(pga))
                if(pga<0.0017):
                    perSha = "Not Felt"
                    poDa = "None"
                elif(0.0017<pga and pga<0.014):
                    perSha = "Weak"
                    poDa = "None"
                elif(0.014<pga and pga<0.039):
                    perSha = "Light"
                    poDa = "None"
                elif(0.039<pga and pga<0.092):
                    perSha = "Moderate"
                    poDa = "Very Light"
                elif(0.092<pga and pga<0.18):
                    perSha = "Strong"
                    poDa = "Light"
                elif(0.18<pga and pga<0.34):
                    perSha = "Very Strong"
                    poDa = "Moderate"
                elif(0.34<pga and pga<0.65):
                    perSha = "Severe"
                    poDa = "Moderate to Heavy"
                elif(0.65<pga and pga<1.24):
                    perSha = "Violent"
                    poDa = "Heavy"
                elif(1.24<pga):
                    perSha = "Extreme"
                    poDa = "Very Heavy"
                

                return render_template("home-graph-trio.html",given_dates=date,
                axisX=axisX,
                currentDateX=currentDateX,
                aveX=aveX,
                lowAcceX=lowAcceX,
                lowTimeX=lowTimeX,
                highAcceX=highAcceX,
                highTimeX=highTimeX,

                axisY=axisY,
                currentDateY=currentDateY,
                aveY=aveY,
                lowAcceY=lowAcceY,
                lowTimeY=lowTimeY,
                highAcceY=highAcceY,
                highTimeY=highTimeY,

                axisZ=axisZ,
                currentDateZ=currentDateZ,
                aveZ=aveZ,
                lowAcceZ=lowAcceZ,
                lowTimeZ=lowTimeZ,
                highAcceZ=highAcceZ,
                highTimeZ=highTimeZ,

                perSha=perSha,
                poDa=poDa
                )

@app.route('/select_date',methods=['GET', 'POST'])
def selectDate():
    print("Current axis is"+axis)
    print("Current no. of files is"+str(numberOfFiles))
    select = request.form.get('select_dates')
    date,dataToInterpret = gg.refresh(select,axis,numberOfFiles)
    if(len(dataToInterpret)==7):
        axisR = dataToInterpret[0]
        currentDate = dataToInterpret[1]
        ave = dataToInterpret[2]
        lowAcce = dataToInterpret[3]
        lowTime = dataToInterpret[4]
        highAcce = dataToInterpret[5]
        highTime = dataToInterpret[6]
        return render_template("home-graph.html",given_dates=date,
        axis=axisR,
        currentDate=currentDate,
        ave=ave,
        lowAcce=lowAcce,
        lowTime=lowTime,
        highAcce=highAcce,
        highTime=highTime
        )
    else:
        # For X
        axisX = dataToInterpret[0][0]
        currentDateX = dataToInterpret[0][1]
        aveX = dataToInterpret[0][2]
        lowAcceX = dataToInterpret[0][3]
        lowTimeX = dataToInterpret[0][4]
        highAcceX = dataToInterpret[0][5]
        highTimeX = dataToInterpret[0][6]
        # For Y
        axisY = dataToInterpret[1][0]
        currentDateY = dataToInterpret[1][1]
        aveY = dataToInterpret[1][2]
        lowAcceY = dataToInterpret[1][3]
        lowTimeY = dataToInterpret[1][4]
        highAcceY = dataToInterpret[1][5]
        highTimeY = dataToInterpret[1][6]
        # For Z
        axisZ = dataToInterpret[2][0]
        currentDateZ = dataToInterpret[2][1]
        aveZ = dataToInterpret[2][2]
        lowAcceZ = dataToInterpret[2][3]
        lowTimeZ = dataToInterpret[2][4]
        highAcceZ = dataToInterpret[2][5]
        highTimeZ = dataToInterpret[2][6]

        pga = (float(highAcceX)+float(highAcceY))/2
        print("PGA IS "+str(pga))
        if(pga<0.0017):
            perSha = "Not Felt"
            poDa = "None"
        elif(0.0017<pga and pga<0.014):
            perSha = "Weak"
            poDa = "None"
        elif(0.014<pga and pga<0.039):
            perSha = "Light"
            poDa = "None"
        elif(0.039<pga and pga<0.092):
            perSha = "Moderate"
            poDa = "Very Light"
        elif(0.092<pga and pga<0.18):
            perSha = "Strong"
            poDa = "Light"
        elif(0.18<pga and pga<0.34):
            perSha = "Very Strong"
            poDa = "Moderate"
        elif(0.34<pga and pga<0.65):
            perSha = "Severe"
            poDa = "Moderate to Heavy"
        elif(0.65<pga and pga<1.24):
            perSha = "Violent"
            poDa = "Heavy"
        elif(1.24<pga):
            perSha = "Extreme"
            poDa = "Very Heavy"

        return render_template("home-graph-trio.html",given_dates=date,
            axisX=axisX,
            currentDateX=currentDateX,
            aveX=aveX,
            lowAcceX=lowAcceX,
            lowTimeX=lowTimeX,
            highAcceX=highAcceX,
            highTimeX=highTimeX,

            axisY=axisY,
            currentDateY=currentDateY,
            aveY=aveY,
            lowAcceY=lowAcceY,
            lowTime=lowTimeY,
            highAcceY=highAcceY,
            highTimeY=highTimeY,

            axisZ=axisZ,
            currentDateZ=currentDateZ,
            aveZ=aveZ,
            lowAcceZ=lowAcceZ,
            lowTimeZ=lowTimeZ,
            highAcceZ=highAcceZ,
            highTimeZ=highTimeZ,

            perSha=perSha,
            poDa=poDa
            )


