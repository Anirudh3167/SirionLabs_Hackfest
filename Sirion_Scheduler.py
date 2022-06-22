import csv
import schedule
import datetime as dt
import calendar

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
      row.append([s_no,job,value,capacity,frequency,start_time,end_time,execution_time,desired_time])
 return

def CSV Input(filename):
  fields = []
  data   = []
  with open(filename,'r') as file:                                                 #assuming the directory is same
       csvreader = csv.reader(file)
       fields = next(csvreader)
       for row in csvreader:
            data.append(row)
  return

#main program
print("****************************")
print("*  1. Manual Input         *")
print("*  2. CSV    Input         *")
print("****************************")
ask = input("Enter you choice:")
if ask == '1' or ask.upper() == 'MANUAL INPUT':
  Manual_Input()
elif ask == '2' or ask.upper() == 'CSV INPUT':
  filename = input("enter the file name:")
  CSV_Input(filename)
else:
  print("Invalid option")
  exit()
