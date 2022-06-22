import random
import datetime as dt

def minutes(hours):
    return hours*60

def hours(minutes):
    rem = minutes%60
    time = str(int(minutes/60))+":"+str((minutes-rem)/60)
    return time

def random_generator(first_limit,last_limit):
    return random.randint(first_limit,last_limit)

def datasets_for_hours(datasets_needed):                                                                 #this is for 24hrs(i.e. tasks for one single day)
    i = 1
    print("===================================================================")
    print("DATASETS IN HOURS FORMAT FOR ONE DAY")
    print("===================================================================")
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
        i = i+1
    return

def datasets_for_datetime(datasets_needed):
    i = 1
    print("===================================================================")
    print("DATASETS IN DATETIME FORMAT FOR ONE MINUTE")
    print("===================================================================")
    while (i<datasets_needed + 1):                                                       #This is for one month
      s_no = i
      job = "job"+str(i)
      frequency = random_generator(1,48)
      value = random_generator(1,100)
      capacity = random_generator(1,80)
      start_datetime = dt.datetime(2022,7,random_generator(1,30),random_generator(1,23),random_generator(0,59))
      end_datetime = dt.datetime(2022,7,random_generator(1,30),random_generator(1,23),random_generator(0,59))
      execution_datetime = dt.time(2022,7,random_generator(1,30),random_generator(1,23),random_generator(0,59))
      desired_datetime = dt.datetime(2022,7,random_generator(1,30),random_generator(1,23),random_generator(0,59))

    
      if   (start_datetime.day > end_datetime.day) or (start_datetime.day > desired_datetime.day):  i = i-1
      elif (desired_datetime.day > end_datetime.day) or (execution_datetime.day > start_datetime.day):  i = i-1
      elif ((start_datetime.hour*60+start_datetime.minute) +(execution_datetime.hour*60+execution_datetime.minute) 
      > (end_datetime.hour*60+end_datetime.minute)):  i = i-1
      elif ((start_datetime.hour*60+start_datetime.minute)>(desired_datetime.hour*60+desired_datetime.minute)): i = i-1
      elif ((desired_datetime.hour*60+desired_datetime.minute) + 120 + 
            (execution_datetime.hour*60+execution_datetime.minute)>
      (end_datetime.hour*60+end_datetime.minute)):  i = i-1
      else:   
          print("s.no:-"+str(s_no))
          print("job:-"+job)
          print("start_time:-"+str(start_datetime))
          print("end_time:-"+str(end_datetime))
          print("execution_time:-"+str(execution_datetime))
          print("desired_start_time:-"+str(desired_datetime))
          print("frequency:-"+str(frequency))
          print("value:-"+str(value))
          print("capacity:-"+str(capacity))
      i = i+1
    return


#main program
print("***************************")
print("* 1. ONE DAY   SCHEDULER  *")
print("* 2. ONE MONTH SCHEDULER  *")
print("***************************")
ask = input("Which dataset do you need:")
if ask == '1' or ask.upper() == 'ONE DAY SCHEDULER':
    datasets = int(input("enter the number of datasets needed:"))
    datasets_for_hours(datasets)
elif ask == '2' or ask.upper() == 'ONE MONTH SCHEDULER':
    datasets = int(input("enter the number of datasets needed:"))
    datasets_for_datetime(datasets)
