import os
import math
import requests
import json
import values
import formula_parser

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
  submissions = user_submissions(user)
  accepted = submissions["accepted"]
  probs = problems()
  tee_sum = 0.0
  for unique_ac in accepted:
    if unique_ac in probs and begin <= accepted[unique_ac] < end:
      prob = probs[unique_ac]
      if "slope" not in prob or "intercept" not in prob:
        continue
      tee_sum += tee_problem(prob["slope"], prob["intercept"])
  variables = {"tee": tee_sum, "x": valx, "y": valy, "z": valz}
  points = formula_parser.calculate(formula, variables)
  return points, tee_sum

def tee_problem(slope: float, intercept: float):
  top_player_rating = 4000
  log_time = slope * top_player_rating + intercept
  return math.exp(log_time)

def user_submissions(user: str):
  dir_path = os.path.dirname(__file__)
  file_path = dir_path + f"/data/user_submissions/{user}.json"
  if not os.path.isdir(dir_path):
    os.makedirs(dir_path)
  if not os.path.isfile(file_path):
    with open(file_path, "w") as file:
      file.write(json.dumps({"newest": 0, "accepted": {}}))
  with open(file_path, "r") as file:
    curr_data = json.load(file)
    newest = curr_data["newest"]
  with open(file_path, "w") as file:
    user_url = f"https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user={user}&from_second={newest}"
    res = requests.get(user_url)
    cont = res.text
    
    new_data = json.loads(cont)
    merge_submission_data(curr_data, new_data)
    json.dump(curr_data, file)
  return curr_data

def merge_submission_data(curr_data, new_data):
  if len(new_data) == 0: return
  curr_data["newest"] = new_data[-1]["epoch_second"]
  accepted = curr_data["accepted"]
  for sub in new_data:
    res = sub["result"]
    prob_id = sub["problem_id"]
    sub_time = sub["epoch_second"]
    if res == "AC" and prob_id not in accepted:
      accepted[prob_id] = sub_time

def download_problems():
  file_path = os.path.dirname(__file__) + "\\data\\problem-models.json"
  problems_url = "https://kenkoooo.com/atcoder/resources/problem-models.json"
  res = requests.get(problems_url)
  cont = res.text
  with open(file_path, "w") as file:
    file.write(cont)

def problems():
  file_path = os.path.dirname(__file__) + "\\data\\problem-models.json"
  with open (file_path, "r") as file:
    probs = json.load(file)
  return probs
