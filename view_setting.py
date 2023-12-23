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
    user = None
    begin = None
    end = None
    formula = None
    valx = None
    valy = None
    valz = None

    is_valid = True
    try:
      user = values.validate_user(textfield_user.value)
      textfield_user.error_text = None
    except ValueError:
      textfield_user.error_text = "input username"
      is_valid = False

    try:
      begin = values.validate_date(textfield_begin.value)
      textfield_begin.error_text = None
    except ValueError:
      textfield_begin.error_text = "input correct date (YYYY-MM-DD hh-mm-ss)"
      is_valid = False

    try:
      end = values.validate_date(textfield_end.value)
      textfield_end.error_text = None
    except ValueError:
      textfield_end.error_text = "input correct date (YYYY-MM-DD hh-mm-ss)"
      is_valid = False

    try:
      formula = values.validate_formula(textfield_formula.value)
      textfield_formula.error_text = None
    except ValueError:
      textfield_formula.error_text = "input correct formula"
      is_valid = False
      
    try:
      valx = values.validate_val(textfield_valx.value)
      textfield_valx.error_text = None
    except ValueError:
      valx = 0.0

    try:
      valy = values.validate_val(textfield_valy.value)
    except ValueError:
      valy = 0.0

    try:
      valz = values.validate_val(textfield_valz.value)
    except ValueError:
      valz = 0.0

    if is_valid:
      page.data.user = user
      page.data.begin_date = begin
      page.data.end_date = end
      page.data.formula = formula
      page.data.valx = valx
      page.data.valy = valy
      page.data.valz = valz

    page.update()

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