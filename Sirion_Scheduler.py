import csv
import datetime as dt
  
def start_time_sorting(data,fields):
  new_data = []
  date_data = []
  for i in data:
     if i[5] not in date_data: date_data.append(i[5])
  date_data.sort()
  for l in date_data:
     for k in data:
        if (l == k[5]) and (k not in new_data):
            new_data.append(k)
  sorting_value(new_data,fields,date_data)
  return data,fields
      
def sorting_value(data,fields,date_data):     
  #sorting as per value.
  value_sorting = []
  for i in date_data:
    same_date=[]
    new_value=[]
    for j in data:
      if (i == j[5]):  same_date.append(j)
      value_list = []
    for j in same_date:
      if j[2] not in value_list:  value_list.append(j[2])
    value_list.sort(reverse=True)
    for j in value_list:
      for k in same_date:
        if (k[2] == j) and (k not in new_value): new_value.append(k)
    value_sorting.extend(new_value)
  analyzer_function(value_sorting,fields)
  return value_sorting,fields

def analyzer_function(value_sorting,fields):
    #delaying other tasks of low value at max capacity.
    analyzer_data = []
    discarded_data = []
    i = 1
    while (i>=1)and(i<25):
      total_capacity = 0
      for j in value_sorting:
        #considering hours only
        freq      = int(j[4])
        strt_time = int(j[5][0:2])
        end_time   = int(j[6][0:2])
        exec_time = int(j[7][0:2])
        des_time  = int(j[8][0:2])
        index_count = 0
        a = 0
        if (i-1>int(strt_time)):
           #derived from the execution_time <=i
           a=int((i-exec_time-strt_time)/(freq+exec_time))
        start_time = strt_time + (a*freq) + (a*exec_time)
        execution_time = strt_time + (a*freq) + ((a+1)*exec_time)
        if ((start_time>=i-1) and (execution_time>=i)      
            and (total_capacity<1000) and (end_time>=i)
            and (j not in analyzer_data)):
          total_capacity = total_capacity + int(j[3])
          analyzer_data.append(j)
        elif (total_capacity>1000):
          analyzer_data = []
          value_sorting[index_count][5] = value_sorting[index_count][5] + 1
          start_time_sorting(value_sorting,fields)
        elif (des_time + 2 < strt_time):
          #discarding tasks with more than desired_time to next schedule.
          discarded_data.append(j)
      i = i+1
    print("============================")
    print("TODAY'S("+str(dt.date.today())+") SCHEDULE IS")
    print("============================")
    print(fields)
    for i in analyzer_data:
        print(i)
      
    print("============================")
    print("TASKS SHIFTED TO NEXT SCHEDULE")
    print("============================")
    print(fields)
    for i in discarded_data:
      print(i)
    #discarding tasks with more than desired_time to next schedule.
    return value_sorting,discarded_data,fields

def Manual_Input():
  fields = ['s_no','job','value','capacity','frequency','start_time','end_time','execution_time','desired_time']
  data   = []
  datasets_number = int(input("Enter the number of datasets you want to enter:"))
  for i in range(datasets_number):
    s_no = str(i)
    job  = 'job:-'+str(i)
    print("=====================================================================")
    value= int(input("Enter the value:"))
    capacity=int(input("Enter the capacity:"))
    frequency = int(input("Enter the frequency in hours:"))
    print("Format:- HH MM")
    start_time_input = list(map(int,input("Enter the start time:").split()))
    end_time_input = list(map(int,input("Enter the end time:").split()))
    execution_time_input = list(map(int,input("Enter the execution time:").split()))
    desired_time_input = list(map(int,input("Enter the desired time:").split()))
    start_time=dt.time(start_time_input[0],start_time_input[1])
    end_time= dt.time(end_time_input[0],end_time_input[1])
    execution_time=dt.time(execution_time_input[0],execution_time_input[1])
    desired_time=dt.time(desired_time_input[0],desired_time_input[1])
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
  new_data = []
  print("============================")
  print("CSV DATA RECIEVED:-")
  print("============================")
  print(fields)
  for i in data:
      if i != []:
        new_data.append(i)
        print(i)
  print("csv input has been taken sucessfully")
  return   new_data,fields

#main program
print("****************************")
print("*  1. Manual Input         *")
print("*  2. CSV    Input         *")
print("****************************")
ask = input("Enter you choice:")
if ask == '1' or ask.upper() == 'MANUAL INPUT':
  result = Manual_Input()
  start_time_sorting(result[0],result[1])
elif ask == '2' or ask.upper() == 'CSV INPUT':
  filename = input("enter the file name:")
  result = CSV_Input(filename)
  start_time_sorting(result[0],result[1])
else:
  print("Invalid option")
  exit()
