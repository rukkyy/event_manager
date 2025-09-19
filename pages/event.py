from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer
from components.event_card import show_event_card
import requests 
from utils.api import base_url

@ui.page("/event")

def show_event_page():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    show_navbar()
    event_id = ui.context.client.request.query_params.get("id")
    response= requests.get(f"{base_url}/events/{event_id}")
    if response.status_code==200:
        json_data=response.json()
        event = json_data["data"]

        #Hero Section
        hero_image_url = event["image"]
        
        with ui.column().classes("relative w-full h-screen font-sans bg-cover bg-center").style(f'background-image: url("{hero_image_url}")'):
            # div for the dark overlay
            ui.element('div').classes('absolute top-0 left-0 w-full h-full bg-black/65')

            # This column holds the content and sits on top of the overlay
            with ui.column().classes('relative w-full h-full text-white p-8'):
                # Back button
                ui.button("< Back", on_click=lambda: ui.navigate.to("/")).classes("bg-blue-700 text-white mb-8 self-start")

                # Main content on the image
                with ui.row().classes("w-full justify-between items-start mt-20"):
                    # Left side: Event details
                    with ui.column().classes("w-1/2 space-y-4"):
                        ui.label(text=event["title"]).classes("font-bold text-5xl")
                        ui.label("IIIT Sonepat").classes("font-bold text-3xl")
                        ui.label(
                            text=event["description"]).classes("text-sm")
                        with ui.row().classes("items-center"):
                            ui.icon("location_on", size="md").classes("mr-2")
                            #ui.link("View map", "https://www.google.com/maps", new_tab=True).classes("text-white text-lg")

                    # Right side: Booking card
                    with ui.card().classes("w-1/3 bg-white/20 text-white backdrop-blur-sm"):
                        ui.label("Date & Time").classes("font-bold text-xl mb-2")
                        ui.label("Saturday, March 18 2023, 9:30")
                        ui.link("Add to calendar").classes("text-white hover:text-gray-300 mb-4")
                        with ui.column().classes("items-center w-full space-y-2"):
                            ui.button("Book now", color="blue").classes("w-full")
                            ui.button("Program promoter", color="blue").classes("w-full")

        # Details Section Below Hero 
        # Centered container for all content below the hero
        with ui.column().classes('w-full max-w-screen-lg mx-auto p-8 space-y-12'):
            with ui.element("div").classes("w-full flex flex-row"):
                # Left column for Description, Hours, Contact
                with ui.element("div").classes("w-1/2 pr-8"):
                    ui.label("Description").classes("text-xl mb-4 font-bold")
                    ui.label(
                        "DesignHub organized a 3D Modeling Workshop using Blender on 16th February at 5 PM. The workshop taught participants the magic of creating stunning 3D models and animations using Blender. It was suitable for both beginners and experienced users. The event was followed by a blender-render competition, which added to the excitement."
                    ).classes("text-sm mb-4")
                    ui.label("Hours").classes("text-xl mb-4 font-bold")
                    with ui.row().classes("text-sm mb-2"):
                        ui.label("Weekdays hour:")
                        ui.label("7PM - 10PM").classes("text-purple-600")
                    with ui.row().classes("text-sm mb-4"):
                        ui.label("Sunday hour:")
                        ui.label("7PM - 10PM").classes("text-purple-600")

                    ui.label("Organizer Contact").classes("text-xl mb-2 font-bold")
                    ui.html(
                        "<p>Please go to <a href='/' class='text-blue-600 hover:underline'>www.rukayamohammed.com</a> and refer the FAQ section for more detail</p>"
                    )

                # Right column for Location, Tags, Share
                with ui.element("div").classes("w-1/2 pl-8"):
                    ui.label("Event Location").classes("text-xl mb-4 font-bold")
                    ui.image("assets/map.png").classes("w-full h-40 object-cover mb-4 rounded-lg")
                    ui.label("Dream world wide in jakatra").classes("text-xl mb-4")
                    ui.label(
                        "Dummy location generation model by RSU. Our approach generates more realistic dummy locations."
                    ).classes("text-sm mb-4")
                    ui.label("Tags").classes("text-xl mb-4 font-bold")
                    with ui.row().classes("text-sm mb-4 gap-2"):
                        ui.label("Indonesia event").classes("bg-gray-300 p-1 rounded")
                        ui.label("Jakarta event").classes("bg-gray-300 p-1 rounded")
                        ui.label("Seminar").classes("bg-gray-300 p-1 rounded")
                        ui.label("Cincinnati event").classes("bg-gray-300 p-1 rounded")
                    ui.label("Share with friends").classes("text-xl mb-4 font-bold")
                    with ui.row().classes("text-4xl space-x-4"):
                        pass
            with ui.column().classes('w-full'):
                with ui.row().classes('items-baseline gap-x-2'):
                    ui.label("Other events you may like").classes("text-3xl font-bold")
                with ui.grid(columns=3).classes("w-full gap-4"):
                    for i in range(6):
                        with ui.card():
                            ui.image("/assets/blog1.png")
                            ui.label(
                                "BestSeller Book Bootcamp-write,Market & Publish Your Book- Lucknow"
                            )
                            ui.label("Saturday, March 18, 9.30PM").classes("w-full")
                            ui.label("ONLINE EVENT - Attend anywhere").classes("w-full")
    elif response.status_code == 422:
        ui.label(text="Something went wrong")
    show_footer()