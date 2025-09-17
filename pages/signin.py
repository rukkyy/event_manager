from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page("/signin")
def show_signin_page():
    with ui.column().classes('items-center justify-center min-h-screen gap-6'):
        ui.label('Sign In').classes('text-3xl font-bold text-blue-700')

        email = ui.input('Email').classes('w-72')
        password = ui.input('Password', password=True, password_toggle_button=True).classes('w-72')

        def handle_signin():
            ui.notify(f'Signed in as {email.value}', type='positive')

        ui.button('Sign In', on_click=handle_signin).classes('bg-blue-500 text-white rounded-lg px-6 py-2 hover:bg-blue-600')

        ui.link('Don’t have an account? Sign Up here.', '/signup').classes('text-sm text-gray-600 underline')
        

