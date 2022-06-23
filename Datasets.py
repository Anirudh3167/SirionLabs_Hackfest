import random
import datetime as dt
import csv

def minutes(hours):
    return hours*60

def hours(minutes):
    rem = minutes%60
    time = str(int(minutes/60))+":"+str((minutes-rem)/60)
    return time

def random_generator(first_limit,last_limit):
    return random.randint(first_limit,last_limit)

def csv_converter(data,fields):
    filename = input("Enter the name of the csv file you want to create:")
    if filename[-4:] != '.csv':
        filename = filename+".csv"
    with open(filename,'w') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(fields)
        csvwriter.writerows(data)
    return

def datasets_for_hours(datasets_needed):                                                                 #this is for 24hrs(i.e. tasks for one single day)
    i = 1
    print("===================================================================")
    print("DATASETS IN HOURS FORMAT FOR ONE DAY")
    print("===================================================================")
    fields = ['s_no','job','value','capacity','frequency','start_time','end_time','execution_time','desired_time']
    data   = []
    while (i<datasets_needed+1):
        job='job '+str(i)
        frequency = random_generator(1,10)
        start_time = random_generator(0,minutes(23))
        end_time = random_generator(120,minutes(24))
        execution_time = random_generator(60,360)
        desired_start_time = random_generator(120,minutes(21))
        value = random_generator(1,100)
        capacity = random_generator(1,80)
        s_no = i
        
        if (start_time + execution_time > end_time):   i = i-1
        elif (start_time>desired_start_time):   i = i-1
        elif (desired_start_time+2+execution_time>end_time):  i = i-1
        else:
          print("s.no:-"+str(s_no))
          print("job:-"+job)
          print("start_time:-"+hours(start_time))
          print("end_time:-"+hours(end_time))
          print("execution_time:-"+hours(execution_time))
          print("desired_start_time:-"+hours(desired_start_time))
          print("frequency:-"+str(frequency))
          print("value:-"+str(value))
          print("capacity:-"+str(capacity))
          starttime = dt.time(int(start_time/60),(start_time%60))
          endtime = dt.time(int(end_time/60),(endt_time%60))
          executiontime = dt.time(int(execution_time/60),(execution_time%60))
          desiredtime = dt.time(int(desired_time/60),(desired_time%60))
          data.append([s_no,job,value,capacity,frequency,starttime,endtime,executiontime,desiredtime])
        i = i+1
    return  data,fields



#main program
datasets = int(input("enter the number of datasets needed:"))
result = datasets_for_hours(datasets)
csv_converter(result[0],result[1])
