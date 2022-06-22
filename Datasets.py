import random
import datetime

def minutes(hours):
    return hours*60

def hours(minutes):
    return minutes*60

def datasets_for_hours(datasets_needed):                                                                 #this is for 24hrs(i.e. tasks for one single day)
    i = 1
    print(minutes)
    while (i<datasets_needed+1):
        job='job '+str(i)
        frequency = random.randint(1,10)
        start_time = random.randint(0,minutes(23))
        end_time = random.randint(120,minutes(24))
        execution_time = random.randint(60,360)
        desired_start_time = random.randint(120,minutes(21))
        value = random.randint(1,100)
        capacity = random.randint(1,80)
        s_no = i
        
        if (start_time + execution_time > end_time):   i = i-1
        elif (start_time>desired_start_time):   i = i-1
        elif (desired_start_time+2+execution_time>end_time):  i = i-1
        else:
          print("s.no:-"+str(s_no))
          print("job:-"+job)
          print("start_time:-"+str(start_time))
          print("end_time:-"+str(end_time))
          print("execution_time:-"+str(execution_time))
          print("desired_start_time:-"+str(desired_start_time))
          print("frequency:-"+str(frequency))
          print("value:-"+str(value))
          print("capacity:-"+str(capacity))
        i = i+1
    return
    
#main program
datasets = int(input("enter the number of datasets needed:"))
datasets_for_hours(datasets)
