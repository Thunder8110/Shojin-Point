import os
import json
import flet as ft
import schedule
import time
import view_main
import view_info
import view_setting
import view_today
import parts
import values
import data_getter
from logging import getLogger
from logging import config as logging_config

with open("logger_config.json", "r") as file:
  config = json.load(file)
  logging_config.dictConfig(config)

logger = getLogger("ShojinPoint")

def main(page: ft.Page):
  page.title = "Shojin Point"
  page.window_height = 500
  page.window_width = 600
  page.window_resizable = False
  page.window_maximizable = False
  page.fonts = {
    "MPLUS1": "/fonts/MPLUS1-VARIABLEFONT_WGHT.TTF"
  }
  page.theme = ft.Theme(
    font_family="MPLUS1",
    text_theme=ft.TextTheme(
      body_large=ft.TextStyle(font_family="MPLUS1", weight=ft.FontWeight.W_400, color=ft.colors.BLACK),
      label_large=ft.TextStyle(font_family="MPLUS1", weight=ft.FontWeight.W_400),
      label_medium=ft.TextStyle(font_family="MPLUS1", weight=ft.FontWeight.W_400),
      body_small=ft.TextStyle(font_family="MPLUS1", weight=ft.FontWeight.W_400),
    ),
  )
  navbar = parts.navigation_bar(page)

  def route_change(event: ft.RouteChangeEvent):
    for i in range(len(page.views)):
      if page.views[i].route == event.route:
        page.views.append(page.views.pop(i))
    page.update()
  page.on_route_change = route_change

  vw_setting, refresh_setting = view_setting.view_setting(page=page, navigation_bar=navbar)
  vw_info, refresh_info = view_info.view_info(page=page, navigation_bar=navbar)
  vw_main, refresh_main = view_main.view_main(page=page, navigation_bar=navbar)
  vw_today, refresh_today = view_today.view_main(page=page, navigation_bar=navbar)
  
  page.views.clear()
  page.views.append(vw_setting)
  page.views.append(vw_info)
  page.views.append(vw_today)
  page.views.append(vw_main)

  def load_data():
    logger.info("Loading data...")
    dir_path = os.path.dirname(__file__) + "/data"
    if not os.path.isdir(dir_path):
      os.makedirs(dir_path)
    file_path = dir_path + "/data_values.json"
    if os.path.isfile(file_path):
      with open(file_path, "r") as file:
        obj = json.load(file)
        return dict_to_values(obj)
    else:
      return values.values()

  def save_data():
    logger.info("Saving data...")
    file_path = os.path.dirname(__file__) + "/data/data_values.json"
    with open(file_path, "w") as file:
      obj = vars(page.data)
      json.dump(obj, file)

  def dict_to_values(dc: dict) -> values.values:
    res = values.values()
    res.__dict__.update(dc)
    res.day = int(time.time())
    return res

  def window_event(event):
    if event.data == "close":
      save_data()
      page.window_destroy()

  page.data = load_data()
  page.on_window_event = window_event
  page.window_prevent_close = True
  refresh_main(page)
  refresh_today(page)
  refresh_setting(page)

  def refresh(page: ft.Page):
    data = data_getter.data_refresh(page.data)
    if data is None:
      return
    points, tee, points_today, tee_today = data
    page.data.points = points
    page.data.tee = tee
    page.data.points_today = points_today
    page.data.tee_today = tee_today
    refresh_main(page)
    refresh_today(page)
    page.update()
  page.update()

  schedule.every(1).seconds.do(refresh, page)
  while True:
    schedule.run_pending()
    time.sleep(0.1)

ft.app(target=main)