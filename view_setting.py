import flet as ft
import datetime
import values
import data_getter

def view_setting(page, navigation_bar):
  text_user = ft.Text("User Name:", size=20, weight=ft.FontWeight.W_400)
  textfield_user = ft.TextField(label="name", dense=True, content_padding=6, helper_text="your user name")
  row_user = ft.Row([text_user, textfield_user], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

  text_begin = ft.Text("Begin Date:", size=20, weight=ft.FontWeight.W_400)
  textfield_begin = ft.TextField(label="begin", dense=True, content_padding=6, helper_text="beginning date (included)", hint_text="YYYY-MM-DD hh:mm:ss")
  row_begin = ft.Row([text_begin, textfield_begin], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

  text_end = ft.Text("End Date:", size=20, weight=ft.FontWeight.W_400)
  textfield_end = ft.TextField(label="end", dense=True, content_padding=6, helper_text="ending date (excluded)", hint_text="YYYY-MM-DD hh:mm:ss")
  row_end = ft.Row([text_end, textfield_end], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

  text_formula = ft.Text("Formula:", size=20, weight=ft.FontWeight.W_400)
  textfield_formula = ft.TextField(label="formula", dense=True, content_padding=6, helper_text="variables must be surround by \"[]\"")
  row_formula = ft.Row([text_formula, textfield_formula], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

  text_val = ft.Text("Variable:", size=20, weight=ft.FontWeight.W_400)
  row_val = ft.Row([text_val], alignment=ft.MainAxisAlignment.START)

  textfield_valx = ft.TextField(label="x", dense=True, content_padding=6, expand=1, helper_text="variable x")
  textfield_valy = ft.TextField(label="y", dense=True, content_padding=6, expand=1, helper_text="variable y")
  textfield_valz = ft.TextField(label="z", dense=True, content_padding=6, expand=1, helper_text="variable z")
  row_valxyz = ft.Row([textfield_valx, textfield_valy, textfield_valz], alignment=ft.MainAxisAlignment.START, spacing=3)

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

  def problems_data(event):
    data_getter.download_problems()

  button_ok = ft.TextButton(text="OK", on_click=input_data)
  button_ref = ft.TextButton(text="Refresh problems", on_click=problems_data)
  row_button = ft.Row([button_ref, button_ok], alignment=ft.MainAxisAlignment.END)

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
      alignment=ft.MainAxisAlignment.START,
      spacing=3,
    ),
    margin=ft.margin.all(10),
    padding=ft.padding.all(10),
  )

  def refresh(page: ft.Page):
    data: values.values = page.data
    if data is None:
      return
    user = data.user
    if user is not None:
      textfield_user.value = user
    begin = data.begin_date
    if begin is not None:
      textfield_begin.value = datetime.datetime.fromtimestamp(begin).strftime("%Y-%m-%d %H:%M:%S")
    end = data.end_date
    if end is not None:
      textfield_end.value = datetime.datetime.fromtimestamp(end).strftime("%Y-%m-%d %H:%M:%S")
    formula = data.formula
    if formula is not None:
      textfield_formula.value = formula
    valx = data.valx
    if valx is not None:
      textfield_valx.value = str(valx)
    valy = data.valy
    if valy is not None:
      textfield_valy.value = str(valy)
    valz = data.valz
    if valz is not None:
      textfield_valz.value = str(valz)


  return ft.View("/setting", [container_settingdisplay], navigation_bar=navigation_bar, scroll=ft.ScrollMode.AUTO), refresh