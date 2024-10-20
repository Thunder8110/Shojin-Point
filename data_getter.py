import os
import sys
import math
import requests
import json
import values
import date_values
import formula_parser
import time
import datetime

def data_refresh(val: values.values):
  # dataver = val.dataver
  # ver_url = "https://tools.kaminarinet.com/Shojin-Point-Web/data/data_version.json"
  # res = requests.get(ver_url)
  # dataver_new = json.loads(res.text)
  # if dataver is None or dataver_new["problems"] > dataver:
  #   download_problems()
  #   print("dl_problems")
  #   val.dataver = dataver_new["problems"]
  return get(val)

def get(val: values.values):
  user = val.user
  begin = val.begin_date
  end = val.end_date
  formula = val.formula
  valx = val.valx
  valy = val.valy
  valz = val.valz
  if user is None or begin is None or end is None or formula is None:
    return None
  submissions = user_submissions(val,user)
  accepted = submissions["accepted"]
  probs = problems()
  tee_sum = 0.0
  tee_sum_today = 0.0
  for unique_ac in accepted:
    if unique_ac in probs and begin <= accepted[unique_ac] < end:
      prob = probs[unique_ac]
      if "slope" not in prob or "intercept" not in prob:
        continue
      tee_sum += tee_problem(prob["slope"], prob["intercept"])
    if unique_ac in probs and datetime.datetime.fromtimestamp(accepted[unique_ac]).date() == datetime.datetime.fromtimestamp(val.day).date():
      prob = probs[unique_ac]
      if "slope" not in prob or "intercept" not in prob:
        continue
      #print(unique_ac,tee_problem(prob["slope"], prob["intercept"]))
      tee_sum_today += tee_problem(prob["slope"], prob["intercept"])
  day, hour, minute = date_values.get_date_values_to_now(begin)
  variables = {
    "tee": tee_sum, "day": day, "hour": hour, "minute": minute,
      "x": valx, "y": valy, "z": valz
    }
  variables_today = {
    "tee": tee_sum_today, "day": 1, "hour": 24, "minute": 1440,
      "x": valx, "y": valy, "z": valz
    }
  points = formula_parser.calculate(formula, variables)
  points_today = formula_parser.calculate(formula, variables_today)
  return points, tee_sum, points_today, tee_sum_today

def tee_problem(slope: float, intercept: float):
  top_player_rating = 4000
  log_time = slope * top_player_rating + intercept
  return math.exp(log_time)

def user_submissions(val:values.values,user: str):
  dir_path = os.path.dirname(__file__) + "/data"
  file_path = dir_path + f"/user_submissions/{user}.json"
  if not os.path.isdir(dir_path):
    os.makedirs(dir_path)
  if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
    with open(file_path, "w") as file:
      file.write(json.dumps({"newest": 0, "accepted": {}}))
  with open(file_path, "r") as file:
    curr_data = json.load(file)
    newest = curr_data["newest"]
  if val.last_get_time is None or time.time() - val.last_get_time >= 60:
    val.last_get_time = time.time()
    with open(file_path, "w") as file:
      while True:
        time.sleep(1)
        user_url = f"https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user={user}&from_second={newest}"
        print("user_submissions_getting...",user_url)
        res = requests.get(user_url)
        cont = res.text
        new_data = json.loads(cont)
        if type(new_data) == list:
          merge_submission_data(curr_data, new_data)
          if len(new_data) == 0:
            break
          try:
            newest = new_data[-1]["epoch_second"]
          except Exception as e:
            print(f"An error occured: {e}", file=sys.stderr)
            print(f"New data was: {new_data}", file=sys.stderr)
            return curr_data
          if len(new_data) != 500:
            break
        else:
          break
      json.dump(curr_data, file)
  return curr_data

def merge_submission_data(curr_data, new_data):
  try:
    curr_data["newest"] = new_data[-1]["epoch_second"]
  except Exception as e:
    print(f"An error occured: {e}", file=sys.stderr)
    print(f"New data was: {new_data}", file=sys.stderr)
    return
  accepted = curr_data["accepted"]
  for sub in new_data:
    res = sub["result"]
    prob_id = sub["problem_id"]
    sub_time = sub["epoch_second"]
    if res == "AC" and prob_id not in accepted:
      accepted[prob_id] = sub_time

def download_problems():
  print("download_problems")
  file_path = os.path.dirname(__file__) + "/data/problem-models.json"
  problems_url = "https://kenkoooo.com/atcoder/resources/problem-models.json"
  res = requests.get(problems_url)
  cont = res.text
  with open(file_path, "w") as file:
    file.write(cont)

def problems():
  file_path = os.path.dirname(__file__) + "/data/problem-models.json"
  with open (file_path, "r") as file:
    probs = json.load(file)
  return probs
