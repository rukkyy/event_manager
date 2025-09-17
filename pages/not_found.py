from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer


@ui.page("/not_found")
def show_not_found_page():
    show_navbar()
    ui.label("This is the not found page ")
    show_footer()