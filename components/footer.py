from nicegui import ui

def handle_subscribe():
    ui.notify('Subscribed!')

def show_footer():
    with ui.element('div').classes('w-full bg-blue-900 text-white p-2'):
        with ui.column().classes('w-full max-w-6xl mx-auto'):
            # Centered navlinks and subscription form
            with ui.column().classes('items-center justify-center w-full'):
                with ui.row().classes('space-x-4 text-sm justify-center mb-4'):
                    ui.link('Home', '/').classes('hover:text-gray-300')
                    ui.link('About', '/').classes('hover:text-gray-300')
                    ui.link('Services', '/').classes('hover:text-gray-300')
                    ui.link('Get in touch', '/').classes('hover:text-gray-300')
                    ui.link('FAQs', '/').classes('hover:text-gray-300')
                with ui.row().classes('items-center justify-center space-x-4 mb-8'):
                    ui.input(placeholder='Enter your email').classes('bg-white w-full max-w-sm rounded-lg').props('outlined dense')
                    ui.button('Subscribe', on_click=handle_subscribe).classes('!bg-purple-600 font-semibold rounded-md px-6 py-2 transition-colors')

            ui.element('hr').classes('w-full border-t border-gray-700 my-4')

            # Copyright right, languages left, socials center
            with ui.row().classes('items-center w-full text-xs text-gray-400'):
                # Left: Languages
                with ui.row().classes('space-x-4 flex-1 justify-start'):
                    ui.label('English')
                    ui.label('French')
                # Center: Socials
                with ui.row().classes('space-x-4 flex-1 justify-center'):
                    ui.icon('img:https://cdn-icons-png.flaticon.com/512/174/174857.png').classes('w-6 h-6 hover:text-gray-300') # LinkedIn
                    ui.icon('img:https://cdn-icons-png.flaticon.com/512/174/174883.png').classes('w-6 h-6 hover:text-gray-300') # Youtube
                    ui.icon('img:https://cdn-icons-png.flaticon.com/512/25/25231.png').classes('w-6 h-6 hover:text-gray-300') # Instagram
                # Right: Copyright
                with ui.row().classes('flex-1 justify-end'):
                    ui.label('Non Copyrighted ©️ 2025 Upload by EventHive').classes('text-right')