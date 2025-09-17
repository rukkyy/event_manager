from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page("/signup")
def show_signup_page():
    with ui.column().classes('items-center justify-center min-h-screen gap-6'):
        ui.label('📝 Create an Account').classes('text-3xl font-bold text-green-700')

        username = ui.input('Username').classes('w-72')
        email = ui.input('Email').classes('w-72')
        password = ui.input('Password', password=True, password_toggle_button=True).classes('w-72')

        def handle_signup():
            ui.notify(f'Account created for {username.value}', type='positive')

        ui.button('Sign Up', on_click=handle_signup).classes('bg-green-500 text-white rounded-lg px-6 py-2 hover:bg-green-600')

        ui.link('Already have an account? Sign In here.', '/signin').classes('text-sm text-gray-600 underline')