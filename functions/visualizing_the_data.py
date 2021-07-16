import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')
import csv

def plot(date,axis):
    data_frame = pd.read_csv("static/assets/data1.csv")

    fig= plt.gcf()
    fig.set_size_inches(35,20)
    plt.plot(data_frame['Time'], data_frame[date], color = 'b',marker = 'o', label=axis)
    
    plt.xlabel('Specific Time', fontsize = 50)
    plt.ylabel('Acceleration', fontsize = 50)
    
    plt.legend(fontsize = 50)


    plt.xlim([0,50])
    plt.title(f"({date}) 12:00 AM - 4:00 AM", fontsize = 50)
    plt.savefig("static/assets/plot1.png")

    plt.xlim([50,100])
    plt.title(f"({date}) 4:00 AM - 8:00 AM", fontsize = 50)
    plt.savefig("static/assets/plot2.png")

    plt.xlim([100,150])
    plt.title(f"({date}) 8:00 AM - 12:00 PM", fontsize = 50)
    plt.savefig("static/assets/plot3.png")

    plt.xlim([150,200])
    plt.title(f"({date}) 12:00 PM - 4:00 PM", fontsize = 50)
    plt.savefig("static/assets/plot4.png")

    plt.xlim([200,250])
    plt.title(f"({date}) 4:00 PM - 8:00 PM", fontsize = 50)
    plt.savefig("static/assets/plot5.png")

    plt.xlim([250,289])
    plt.title(f"({date}) 8:00 PM - 12:00 AM", fontsize = 50)
    plt.savefig("static/assets/plot6.png")
    plt.clf()
    remember_axis = axis

def plotall(date,axis):
    print("GOING HERE")
    data_frame = pd.read_csv("static/assets/data1.csv")
    data_frame1 = pd.read_csv("static/assets/data2.csv")
    data_frame2 = pd.read_csv("static/assets/data3.csv")

    fig= plt.gcf()
    fig.set_size_inches(35,20)
    plt.plot(data_frame['Time'], data_frame[date], color = 'b',marker = 'o', label="X")
    plt.plot(data_frame['Time'], data_frame1[date], color = 'r',marker = 'o', label="Y")
    plt.plot(data_frame['Time'], data_frame2[date], color = 'y',marker = 'o', label="Z")

    plt.xlabel('Specific Time',fontsize = 50)
    plt.ylabel('Acceleration',fontsize = 50)
    plt.legend(fontsize = 50)

    plt.xlim([0,50])
    plt.title(f"({date}) 12:00 AM - 4:00 AM", fontsize = 50)
    plt.savefig("static/assets/plot1.png")

    plt.xlim([50,100])
    plt.title(f"({date}) 4:00 AM - 8:00 AM", fontsize = 50)
    plt.savefig("static/assets/plot2.png")

    plt.xlim([100,150])
    plt.title(f"({date}) 8:00 AM - 12:00 PM", fontsize = 50)
    plt.savefig("static/assets/plot3.png")

    plt.xlim([150,200])
    plt.title(f"({date}) 12:00 PM - 4:00 PM", fontsize = 50)
    plt.savefig("static/assets/plot4.png")

    plt.xlim([200,250])
    plt.title(f"({date}) 4:00 PM - 8:00 PM", fontsize = 50)
    plt.savefig("static/assets/plot5.png")

    plt.xlim([250,289])
    plt.title(f"({date}) 8:00 PM - 12:00 AM", fontsize = 50)
    plt.savefig("static/assets/plot6.png")
    plt.clf()

    remember_axis = axis

def caller(x,axis):
    with open('static/assets/data1.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        row1 = next(csv_reader)
        row1.remove('Time')
        available_dates=row1
        # print(available_dates[0])
        
    date = available_dates[0]
    print("NUMMBER OF FILES SENT IS"+str(x-1))
    if((x-1)==3):
        plotall(date,axis)
    else:
        plot(date,axis)
    
    return(available_dates)

def refresh(date,axis,numberOfFiles):
    with open('static/assets/data1.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        row1 = next(csv_reader)
        row1.remove('Time')
        available_dates=row1
        # print(available_dates[0])

    if(numberOfFiles==1):
        plot(date,axis)
    else:
        plotall(date, axis)

    return(available_dates)
    