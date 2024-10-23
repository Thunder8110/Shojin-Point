import math
import datetime

def tee_sum(accepted: dict, probs: dict, begin: int, end: int):
  tee_sum = 0.0
  for unique_ac in accepted:
    if unique_ac in probs and begin <= accepted[unique_ac] < end:
      prob = probs[unique_ac]
      if "slope" not in prob or "intercept" not in prob:
        continue
      tee_sum += tee_problem(prob["slope"], prob["intercept"])
  return tee_sum

def tee_sum_on_day(accepted: dict, probs: dict, day: int):
  tee_sum_today = 0.0
  for unique_ac in accepted:
    if unique_ac in probs and datetime.datetime.fromtimestamp(accepted[unique_ac]).date() == datetime.datetime.fromtimestamp(day).date():
      prob = probs[unique_ac]
      if "slope" not in prob or "intercept" not in prob:
        continue
      tee_sum_today += tee_problem(prob["slope"], prob["intercept"])
  return tee_sum_today

def tee_problem(slope: float, intercept: float):
  top_player_rating = 4000
  log_time = slope * top_player_rating + intercept
  return math.exp(log_time)

def problem_tee_from_id(probs: dict, id: str) -> float | None:
  if id in probs:
    prob = probs[id]
    if "slope" not in prob or "intercept" not in prob:
      return None
    return tee_problem(prob["slope"], prob["intercept"])
  return None
