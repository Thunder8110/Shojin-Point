from datetime import datetime
from datetime import date
import time
import formula_parser
import lark

class values:
  def __init__(self) -> None:
    self.user: str | None = None
    self.points: int | None = None
    self.tee: float | None = None
    self.begin_date: int | None = None
    self.end_date: int | None = None
    self.formula: str | None = None
    self.dataver: int | None = None
    self.valx: float | None = None
    self.valy: float | None = None
    self.valz: float | None = None
    self.last_get_time : float | None = None
    self.tee_today : float | None = None
    self.today_tee : float | None = None
    self.points_today: int | None = None
    self.day : int | None = None

def validate_user(value):
  if value is None or value == "":
    raise ValueError("User name must not be empty.")
  return value

def validate_date(value):
  if value is None or value == "":
    raise ValueError("Date must not be empty.")
  try:
    dtbegin = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    return int(dtbegin.timestamp())
  except ValueError as err:
    raise err
  
def validate_formula(value):
  if value is None or value == "":
    raise ValueError("Formula must not be empty.")
  try:
    formula_parser.parse_formula(value)
  except lark.exceptions.UnexpectedInput as err:
    print(str(err))
    raise ValueError()
  return value

def validate_val(value):
  if value is None or value == "":
    raise ValueError("Valiable is empty.")
  try:
    return float(value)
  except ValueError as err:
    raise err
