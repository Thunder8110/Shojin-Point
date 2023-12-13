import flet as ft
import datetime

def view_setting(page, navigation_bar):
  text_user = ft.Text("User Name:", size=20, weight=ft.FontWeight.W_400)
  textfield_user = ft.TextField(label="name", dense=True)
  row_user = ft.Row([text_user, textfield_user], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

  text_begin = ft.Text("Begin Date:", size=20, weight=ft.FontWeight.W_400)
  textfield_begin = ft.TextField(label="begin", dense=True)
  row_begin = ft.Row([text_begin, textfield_begin], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

  text_end = ft.Text("End Date:", size=20, weight=ft.FontWeight.W_400)
  textfield_end = ft.TextField(label="end", dense=True)
  row_end = ft.Row([text_end, textfield_end], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

  text_formula = ft.Text("Formula:", size=20, weight=ft.FontWeight.W_400)
  textfield_formula = ft.TextField(label="formula", dense=True)
  row_formula = ft.Row([text_formula, textfield_formula], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

  text_val = ft.Text("Variable:", size=20, weight=ft.FontWeight.W_400)
  row_val = ft.Row([text_val], alignment=ft.MainAxisAlignment.START)

  textfield_valx = ft.TextField(label="x", dense=True, expand=1)
  textfield_valy = ft.TextField(label="y", dense=True, expand=1)
  textfield_valz = ft.TextField(label="z", dense=True, expand=1)
  row_valxyz = ft.Row([textfield_valx, textfield_valy, textfield_valz], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

  def input_data(event):
    input_user = textfield_user.value
    if input_user is not None:
      page.data.user = input_user
    input_begin = textfield_begin.value
    if input_begin is not None:
      dtbegin = datetime.datetime.strptime(input_begin, "%Y-%m-%d %H:%M:%S")
      page.data.begin_date = int(dtbegin.timestamp())
    input_end = textfield_end.value
    if input_end is not None:
      dtend = datetime.datetime.strptime(input_end, "%Y-%m-%d %H:%M:%S")
      page.data.end_date = int(dtend.timestamp())
    input_formula = textfield_formula.value
    if input_formula is not None:
      page.data.formula = input_formula
    input_valx = textfield_valx.value
    if input_valx is not None:
      page.data.valx = float(input_valx)
    input_valy = textfield_valy.value
    if input_valy is not None:
      page.data.valy = float(input_valy)
    input_valz = textfield_valz.value
    if input_valz is not None:
      page.data.valz = float(input_valz)

  button_ok = ft.TextButton(text="OK", on_click=input_data)
  row_button = ft.Row([button_ok], alignment=ft.MainAxisAlignment.END)

  container_settingdisplay = ft.Container(
    content=ft.Column(
      controls=[row_user,
                row_begin,
                row_end,
                row_formula,
                row_val,
                row_valxyz,
                row_button,
                ],
      alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    ),
    margin=ft.margin.all(10),
    padding=ft.padding.all(10),
  )

  def refresh(page: ft.Page):
    pass

  return ft.View("/setting", [container_settingdisplay], navigation_bar=navigation_bar), refresh