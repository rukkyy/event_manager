
from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer
import requests
from utils.api import base_url

# Global to hold uploaded image
_event_image = None


def _handle_image_upload(event):
    global _event_image
    _event_image = event.content  


def _post_event(data, files):
    response = requests.post(f"{base_url}/events", data=data, files=files)
    print(response.status_code, response.content)

    if response.status_code == 200:
        ui.notify("Event added Successfully!", type="positive")
        return ui.navigate.to("/")
    elif response.status_code == 422:
        ui.notify("Please ensure all inputs are filled!", type="negative")
    else:
        ui.notify(f"Error: {response.status_code}", type="negative")


@ui.page("/create_event")
def show_create_event_page():
    show_navbar()

    with ui.column().classes("w-full items-center mt-12"):
        ui.label("Create Event").classes("text-3xl text-purple-600 font-bold mb-6")

        with ui.card().classes("w-[600px] p-6 shadow-md rounded-xl"):
            # Form inputs
            event_title = ui.input("Event Title").props("outlined").classes("w-full")
            event_venue = ui.input("Event Venue").props("outlined").classes("w-full")

            with ui.row().classes("w-full gap-6"):
                event_start_time = ui.input("Start time").props("type=time outlined").classes("w-1/2")
                event_end_time = ui.input("End time").props("type=time outlined").classes("w-1/2")

            with ui.row().classes("w-full gap-6"):
                event_start_date = ui.input("Start date").props("type=date outlined").classes("w-1/2")
                event_end_date = ui.input("End date").props("type=date outlined").classes("w-1/2")

            ui.label("Event Description").classes("text-2xl font-bold mt-8")

            ui.upload(
                label="Upload Event Image",
                auto_upload=True,
                on_upload=_handle_image_upload,
            ).props("color=purple-600").classes(
                "w-full h-40 border border-gray-300 rounded-lg"
            )

            event_description = ui.textarea("Event Description").props("outlined").classes("w-full h-32")

            # Submit handler
            def submit():
                data = {
                    "title": event_title.value,
                    "venue": event_venue.value,
                    "start_time": event_start_time.value,
                    "end_time": event_end_time.value,
                    "start_date": event_start_date.value,
                    "end_date": event_end_date.value,
                    "description": event_description.value,
                }

                files = {"image": _event_image} if _event_image else None
                _post_event(data, files)

            # Submit button
            ui.button("Create event", on_click=submit).classes(
                "!bg-purple-600 text-white w-full py-3 rounded-lg font-bold mt-6"
            )

    show_footer()
