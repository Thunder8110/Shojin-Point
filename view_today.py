import flet as ft
import datetime
import time
from tee_values import tee_problem
from data_getter import problems,user_submissions
def view_main(page, navigation_bar):
  text_mainpoints = ft.Text("Points:", size=40, weight=ft.FontWeight.W_400)
  text_mainpointsnum = ft.Text("", size=80, weight=ft.FontWeight.W_600, italic=True)
  row_mainpoints = ft.Row(
    controls=[text_mainpoints, text_mainpointsnum],
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    vertical_alignment=ft.CrossAxisAlignment.START,
  )

  text_subpoints = ft.Text("TEE:", size=40, weight=ft.FontWeight.W_400)
  text_subpointsnum = ft.Text("", size=40, weight=ft.FontWeight.W_400)
  row_subpoints = ft.Row(
    controls=[text_subpoints, text_subpointsnum],
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
  )
  

  container_maindisplay = ft.Container(
    content=ft.Column(
      [row_mainpoints, row_subpoints]
    ),
    border=ft.border.symmetric(vertical=ft.border.BorderSide(1, ft.colors.BLACK)),
    margin=ft.margin.all(10),
    padding=ft.padding.all(10),
    bgcolor=ft.colors.BLACK12,
  )

  text_begin = ft.Text("Day:", size=30, weight=ft.FontWeight.W_300)
  text_begindate = ft.Text("", size=30, weight=ft.FontWeight.W_300)
  row_begin = ft.Row(
    controls=[text_begin, text_begindate],
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
  )
  def day_add(x):
    page.data.day += 60*60*24
  def day_dec(x):
    page.data.day -= 60*60*24
  def go_today(x):
    page.data.day = int(time.time())
  
  def get_ac_values_day(accepted: dict, probs: dict, day: int):
    tee_sum_today = 0.0
    ac_count = 0
    top_tees = []
    for unique_ac in accepted:
      if unique_ac in probs and datetime.datetime.fromtimestamp(accepted[unique_ac]).date() == datetime.datetime.fromtimestamp(day).date():
        ac_count += 1
        prob = probs[unique_ac]
        if "slope" in prob and "intercept" in prob:
          tee_sum_today += tee_problem(prob["slope"], prob["intercept"])
          if "difficulty" in prob:
            top_tees.append((tee_problem(prob["slope"], prob["intercept"]),prob["difficulty"],unique_ac))
        elif "difficulty" in prob:
          top_tees.append((-float("inf"),prob["difficulty"],unique_ac))
        else:
          top_tees.append((-float("inf"),-float("inf"),unique_ac))
    top_tees.sort(reverse=True)
    return (ac_count,tee_sum_today,top_tees)
  def tweet(x):
    selected_day = page.data.day
    user = page.data.user
    day = datetime.datetime.fromtimestamp(selected_day).strftime("%m月%d日")
    probs = problems()
    submissions = user_submissions(page.data,user)
    accepted = submissions["accepted"]
    ac_count,tee_sum_today,top_tees = get_ac_values_day(accepted,probs,selected_day)
    text = f"{day} {user}の精進記録\n"
    text += f"新規AC数: {ac_count}\n"
    text += f"獲得TEE: {int(tee_sum_today)}\n"
    if len(top_tees) != 0:
      text += "解いた問題たち\n"
      for i in range(min(5,len(top_tees))):
        text += f"{top_tees[i][2]} "
        if top_tees[i][0] != -float("inf"):
          text += f"TEE: {int(top_tees[i][0])} "
        else:
          text += "TEE: ---- "
        if top_tees[i][1] != -float("inf"):
          text += f"diff: {int(top_tees[i][1])} "
        else:
          text += "diff: ---- "
        text += "\n"
    page.launch_url("https://twitter.com/intent/tweet?text="+text)
  button_left = ft.TextButton(text="<<", on_click=day_dec)
  button_today = ft.TextButton(text="today", on_click=go_today)
  button_right = ft.TextButton(text=">>", on_click=day_add)
  button_tweet = ft.TextButton(text="tweet", on_click=tweet)
  row_buttons = ft.Row(
    controls=[button_left,button_today,button_tweet,button_right],
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
  )
  

  container_subdisplay = ft.Container(
    content=ft.Column(
      [row_begin, row_buttons]
    ),
    margin=ft.margin.all(10),
    padding=ft.padding.all(10),
  )

  def refresh(page: ft.Page):
    points = page.data.points_today
    tee = page.data.tee_today
    begin = page.data.begin_date
    end = page.data.end_date
    
    if points is not None:
      text_mainpointsnum.value = str(points)
    if tee is not None:
      text_subpointsnum.value = f"{tee:.2f}"
    if begin is not None:
      text_begindate.value = str(datetime.datetime.fromtimestamp(page.data.day).date())

  return ft.View("/today", [container_maindisplay, container_subdisplay], navigation_bar=navigation_bar), refresh