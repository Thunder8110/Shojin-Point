import datetime

def get_date_values(from_date: int, to_date: int) -> tuple[int, int, int]:
  from_dt = datetime.datetime.fromtimestamp(from_date)
  to_dt = datetime.datetime.fromtimestamp(to_date)
  delta = to_dt - from_dt
  day = delta.days
  hour = delta.seconds // 3600
  minute = (delta.seconds % 3600) // 60
  return day, hour, minute
  
def get_date_values_to_now(from_date: int) -> tuple[int, int, int]:
  now = datetime.datetime.now()
  return get_date_values(from_date, int(now.timestamp()))