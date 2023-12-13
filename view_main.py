import flet as ft
import datetime

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

  text_begin = ft.Text("Begin:", size=30, weight=ft.FontWeight.W_300)
  text_begindate = ft.Text("", size=30, weight=ft.FontWeight.W_300)
  row_begin = ft.Row(
    controls=[text_begin, text_begindate],
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
  )

  text_end = ft.Text("End:", size=30, weight=ft.FontWeight.W_300)
  text_enddate = ft.Text("", size=30, weight=ft.FontWeight.W_300)
  row_end = ft.Row(
    controls=[text_end, text_enddate],
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
  )

  container_subdisplay = ft.Container(
    content=ft.Column(
      [row_begin, row_end]
    ),
    margin=ft.margin.all(10),
    padding=ft.padding.all(10),
  )

  def refresh(page: ft.Page):
    points = page.data.points
    tee = page.data.tee
    begin = page.data.begin_date
    end = page.data.end_date
    
    text_mainpointsnum.value = str(points)
    text_subpointsnum.value = f"{tee:.2f}"
    text_begindate.value = str(datetime.datetime.fromtimestamp(begin))
    text_enddate.value = str(datetime.datetime.fromtimestamp(end))

  return ft.View("/", [container_maindisplay, container_subdisplay], navigation_bar=navigation_bar), refresh