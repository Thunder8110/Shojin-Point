import flet as ft

def view_info(page, navigation_bar):
  texts = ["Shojin Point", "version 0.2.0-alpha", "Made By KA37RI",
           "// TODO", "Features: History, Editorial AC", "Setting: Validator",
           "Software: Make Executable File", "Software: Update Problems data"]
  text_info = [ft.Text(tx, size=20) for tx in texts]

  container_info = ft.Container(
    content=ft.Column(text_info),
    margin=ft.margin.all(10),
    padding=ft.padding.all(10),
  )

  def refresh(page: ft.Page):
    pass

  return ft.View("/info", [container_info], navigation_bar=navigation_bar), refresh