import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')
import csv

def plot(date,axis):
    data_frame = pd.read_csv("static/assets/data1.csv")

    dataToInterpret1 = analyzeData(data_frame,date,axis)
    print(dataToInterpret1)

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
    return(dataToInterpret1)

def plotall(date,axis):
    print("GOING HERE")
    data_frame = pd.read_csv("static/assets/data1.csv")
    data_frame1 = pd.read_csv("static/assets/data2.csv")
    data_frame2 = pd.read_csv("static/assets/data3.csv")

    dataToInterpret1 = analyzeData(data_frame,date,"x")
    dataToInterpret2 = analyzeData(data_frame1,date,"y")
    dataToInterpret3 = analyzeData(data_frame2,date,"z")
    print(dataToInterpret1)
    print(dataToInterpret2)
    print(dataToInterpret3)

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
    return(dataToInterpret1,dataToInterpret2,dataToInterpret3)

def analyzeData(data_frame,date,axis):
    df1 = pd.DataFrame(data_frame,columns=[date,"Time"])

    mini = df1.sort_values(by=[date,'Time'],ascending=True)
    minF = (mini[0:1])

    maxi = df1.sort_values(by=[date,'Time'],ascending=False)
    maxiF = (maxi[0:1])

    df = pd.DataFrame(data_frame,columns=[date])
    df = pd.DataFrame(data_frame,columns=[date])
    num=0       

    for i in range (1,288):
        num = num + df.iloc[i][date]    
        
    ave = num/i;
    # print("Average:", ave)

    lowData = str(minF).split()
    currentDate = lowData[0]
    # print("Date is ",currentDate)
    lowTime= " ".join((lowData[4],lowData[5]))
    lowAcce = lowData[3]
    # print("Lowest Acceleration:" , lowAcce)
    # print("Time of Low Acceleration",lowTime )
    highData = str(maxiF).split()
    highTime = " ".join((highData[4],highData[5]))
    highAcce = highData[3]
    # print("Peak Acceleration:" , highAcce)
    # print("Time of Peak Acceleration",highAcce )

    dataToInterpret = axis,currentDate,ave,lowAcce,lowTime,highAcce,highTime
    return dataToInterpret
    

def caller(x,axis):
    dataToInterpret = ''
    with open('static/assets/data1.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        row1 = next(csv_reader)
        row1.remove('Time')
        available_dates=row1
        # print(available_dates[0])
        
    date = available_dates[0]
    print("NUMMBER OF FILES SENT IS"+str(x-1))
    if((x-1)==3):
        dataToInterpret = plotall(date,axis)
    else:
        dataToInterpret = plot(date,axis)
    
    return(available_dates,dataToInterpret)

def refresh(date,axis,numberOfFiles):
    dataToInterpret = ''
    with open('static/assets/data1.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        row1 = next(csv_reader)
        row1.remove('Time')
        available_dates=row1
        # print(available_dates[0])

    if(numberOfFiles==1):
        dataToInterpret = plot(date,axis)
    else:
        dataToInterpret = plotall(date, axis)

    return(available_dates,dataToInterpret)
    