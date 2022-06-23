import csv
import schedule
import datetime as dt
import calendar

def task_scheduler(data,fields):
  #sorting as per start_datetime.
  new_data = []
  for i in data:
    a = i[5]
    for j in data:
      if (a >j[5]) and (j not in new_data):  a=j[5]
    for k in data:
      if k[5] == a:
        new_data.append(k)
        
  #sorting as per value.
  value_sorting = []
  for i in new_data:
    same_date = []
    date = i[5]
    for j in data:
      if (i[5] == j[5]) and (j not in value_sorting):  same_date.append(j)
    for j in same_date:
      a = j[2]
      for k in same_date:
        if (a>k[2]) and (k not in value_sorting): a=k[2]
      for l in same_date:
        if l[2] == a:
          value_sorting.append(l)
          
  #delaying other tasks of low value at max capacity.
  analyzer_data = []
  First_start_time = value_sorting[0][5]
  Last_start_time = value_sorting[-1][5]
  for i in value_sorting():
    if analyzer_data == []:
      analyzer_data.append(i)
  
  #discarding tasks with more than desired_time to next schedule.
  return value_sorting

def Manual_Input():
  fields = ['s_no','job','value','capacity','frequency','start_time','end_time','execution_time','desired_time']
  data   = []
  datasets_number = int(input("Enter the number of datasets you want to enter:"))
  for i in range(datasets_number):
    s_no = str(i)
    job  = 'job:-'+str(i)
    value= int(input("Enter the value:"))
    capacity=int(input("Enter the capacity:"))
    frequency = int(input("Enter the frequency in hours:"))
    print("Format:- YYYY,MM,DD,HH,MM")
    start_time=dt.datetime(input("Enter the start time:"))
    end_time= dt.datetime(input("Enter the end time:"))
    execution_time=dt.datetime(input("Enter the execution time:"))
    desired_time=dt.datetime(input("Enter the desired start time:"))
    if (capacity>80) or (value>100):
      print("This entry is invalid. please try again")
      i = i - 1
    else:
      data.append([s_no,job,value,capacity,frequency,start_time,end_time,execution_time,desired_time])
 return   data,fields

def CSV_Input(filename):
  fields = []
  data   = []
  with open(filename,'r') as file:                                                 #assuming the directory is same
       csvreader = csv.reader(file)
       fields = next(csvreader)
       for row in csvreader:
            data.append(row)
  return   data,fields

#main program
print("****************************")
print("*  1. Manual Input         *")
print("*  2. CSV    Input         *")
print("****************************")
ask = input("Enter you choice:")
if ask == '1' or ask.upper() == 'MANUAL INPUT':
  result = Manual_Input()
  task_scheduler(result[0],result[1])
elif ask == '2' or ask.upper() == 'CSV INPUT':
  filename = input("enter the file name:")
  result = CSV_Input(filename)
  task_scheduler(result[0],result[1])
else:
  print("Invalid option")
  exit()
