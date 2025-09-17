from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page("/college")
def show_college_page():  
    show_navbar()
    ui.label('This is the College Page')
    ui.image("assets/college.png")
    show_footer()