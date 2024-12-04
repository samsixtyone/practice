import os
import sys
import json
import time

def loggly(func):
  def wrapper(*args, **kwargs):
    with open ("high_score.log", "w") as logfile:
      start = time.perf_counter()
      result = func(*args, **kwargs)
      endtime = time.perf_counter()
      logfile.write(f"Function: {func.__name__} took {endtime - start:.6f} seconds")
      with open ("my.json", "w") as myjson:
        json.dump(list(result), myjson)
    return result
  return wrapper

def usage():
  print ("__" * 15)
  print ("\npython highest.py score_recs.data 5\n")
  print ("__" * 15)

# check valid arguments
def arg_check(arg):
  if len (arg) != 3:      # take two valid arguments
    usage()
  elif not os.path.isfile(arg[1]):    #check if file exits
    usage()
    sys.exit(1)
  elif not arg[2].isdigit():
    usage()
    sys.exit(1)
  #·check·if·file·exits·and·numer·of·sample·is·digit
  elif os.path.isfile(arg[1]) and arg[2].isdigit():
    return True
  else:
    usage()


@loggly
def whacker(arg):
  no_of_samples=int(arg[2]) #·convert·number·sample·arg·to·integer
  with open(arg[1], "r") as file:
    for line in file:
      score, idx = line.split(":", 1)  #·split·each·on·first·":"
      try:
        idx = json.loads(idx) #·validate·json·
      except ValueError as e:
        sys.exit(2)
      if "id" not in idx: #·check·if·id·exists·in·json·record
        sys.exit(2)
      if idx["id"] not in samples.values():  #·if·recoard·already·not·added·to·samples
        samples[score]=idx["id"]
  sorted_samples = sorted(samples.items(), key=lambda x: x[0], reverse=True)[:no_of_samples]
  sorted_samples = dict(sorted_samples)
  #·convert·response·into·requested·output
  jsonlist=[]
  for key, val in sorted_samples.items():
    jsonlist.append({'score': key, 'id': val})
  print(json.dumps(jsonlist, indent=4))
  return (jsonlist)
#  sys.exit(0)

if __name__ == "__main__":
  samples={}   # hold all samples
  arg = sys.argv  # argument list
  chk = arg_check(arg)
  if chk:
    whacker(arg)
