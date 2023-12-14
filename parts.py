import flet as ft

def navigation_bar(page: ft.Page):
  def view_change(event: ft.ControlEvent):
    idx = event.control.selected_index
    page.go(["/", "/info", "/setting"][idx])

  return ft.NavigationBar(
    selected_index=0,
    on_change=view_change,
    destinations=[
      ft.NavigationDestination(label="Main", icon=ft.icons.SHOW_CHART),
      ft.NavigationDestination(label="Information", icon=ft.icons.INFO_OUTLINE),
      ft.NavigationDestination(label="Settings", icon=ft.icons.SETTINGS),
    ],
  )
