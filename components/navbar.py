from nicegui import ui

def show_navbar():
    with ui.header().classes('flex flex-row items-center justify-between w-full p-4 bg-white shadow-md'):
        # Logo
        with ui.row().classes('items-center'):
            ui.html('<span style="font-size:1.5rem;font-weight:bold;color:#1f2937;">Event</span><span style="font-size:1.5rem;font-weight:bold;color:#4f46e5;">Hive</span>')
        with ui.row().classes('md:flex items-center space-x-6'):
            ui.button('Event', on_click=lambda: ui.navigate.to('/event')).props('flat').classes('text-indigo-600 font-semibold')
            ui.button('College', on_click=lambda: ui.navigate.to('/college')).props('flat').classes('text-indigo-600 font-semibold')
        # Login/Signup buttons
        with ui.row().classes('items-center space-x-4'):
            ui.button('Sign Up', on_click=lambda: ui.navigate.to('/signup')).props('flat').classes('text-indigo-600 font-semibold')
            ui.button('Sign In', on_click=lambda: ui.navigate.to('/signin')).classes('bg-indigo-600 hover:bg-indigo-700 font-semibold rounded-md px-6 py-2 transition-colors')