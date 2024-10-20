import flet as ft
import datetime
import time
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
  button_left = ft.TextButton(text="<<", on_click=day_dec)
  button_today = ft.TextButton(text="today", on_click=go_today)
  button_right = ft.TextButton(text=">>", on_click=day_add)
  row_buttons = ft.Row(
    controls=[button_left,button_today, button_right],
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