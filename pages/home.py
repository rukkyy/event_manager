from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer
from components.event_card import show_event_card
import requests
from utils.api import base_url


@ui.page("/")
def show_home_page():
    show_navbar()

    # remove default padding/margin from content
    ui.query(".nicegui-content").classes("p-0 m-0")

    # HERO SECTION 
    with ui.column().classes(
        "w-full h-screen bg-[url('/assets/image.png')] bg-cover bg-center relative"
    ):
        # dark overlay for readability
        ui.element("div").classes("absolute inset-0 bg-black/40")

        # hero text content
        with ui.column().classes(
            "relative z-10 w-full h-full flex items-center justify-center text-center text-white space-y-6"
        ):
            ui.label("MADE FOR THOSE").classes(
                "text-5xl md:text-6xl font-extrabold tracking-tight"
            )
            ui.label("WHO DO").classes("text-5xl md:text-6xl font-extrabold tracking tight")

#Search Bar
        with ui.row().classes("-mb-10 bg-blue-600 rounded-xl shadow-lg p-4 w-11/12 md:w-3/4 justify-around space-x-4 z-20 mx-auto"):
                    ui.select(["Select event type", "Conference", "Workshop", "Concert"], value="Select event type", with_input=True).props("outlined dense").classes("w-1/4 bg-white rounded-lg text-gray-700")
                    ui.select(["Select location", "On Campus", "Online", "Restaurant"], value="Select location", with_input=True).props("outlined dense").classes("w-1/4 bg-white rounded-lg text-gray-700")
                    ui.input(label="Choose date and time").props("outlined dense").classes("w-1/4 bg-white rounded-lg text-gray-700")
                    ui.button(icon="search").classes("bg-purple-600 text-white rounded-sm p-3 hover:bg-indigo-700")


    # Upcoming events section
    with ui.column().classes("w-full items-center mt-16"):
        with ui.row().classes("items-baseline gap-x-2 justify-center mb-6"):
             ui.label("Upcoming Events").classes("text-4xl font-bold")

        with ui.row().classes("gap-6 flex-wrap justify-center items-center"):
             weekdays=["Weekdays", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
             ui.select(label="", value="Weekdays", options=weekdays).classes("w-48")

             event_type=["Event", "Indoor", "Outdoor"]
             ui.select(label="", value="Event", options=event_type).classes("w-40")

             category=["Category", "All", "Some", "Any", "Nothing", "Something"]
             ui.select(label="", value="Category", options=category).classes("w-40")

    with ui.grid(columns=3).classes("max-w-6xl mx-auto p-8 gap-8 justify-items-center"):
        response=requests.get(f"{base_url}/events?limit=6")
        json_data=response.json()
        for event in json_data["data"]:
            show_event_card(event)
                
    with ui.row().classes("w-full justify-center mt-6"):            
        ui.button("Load more.....",on_click=lambda: ui.navigate.to("/event")).classes("px-8 py-3 !bg-[#5a34c2] text-l font-bold justify-center rounded-full text-white hover:bg-black")

    
# Create Events Section
    with ui.element("section").classes("relative w-full h-[303px] mt-24"):
                # Navy blue background
        with ui.element("div").classes("absolute w-full h-[252px] left-0 top-[51px] bg-[#10107B]"):
                    pass
                # Left image
        with ui.element("div").classes("absolute w-[544.67px] h-[303px] left-[100px] top-0"):
             ui.image("assets/image copy.png").classes("w-full h-full object-cover rounded-[10px]")
                # Right content
        with ui.element("div").classes("absolute w-[417px] h-[182px] left-[696px] top-[86px]"):
             ui.label("Make your own Event").classes("text-[36px] font-bold leading-[42px] text-[#F8F8FA]")
             ui.label("Empower your campus—host, manage, and share unforgettable events with ease.").classes("mt-4 text-[18px] leading-[21px] text-[#F8F8FA]")
                # CTA Button
        with ui.element("div").classes("absolute w-[302px] h-[60px] left-[696px] top-[208px]"):
                    ui.button("Create Event",on_click=lambda: ui.navigate.to('/create_event')).classes(
                        "w-full h-full !bg-purple-600 text-white text-[18px] font-bold rounded-[5px] shadow-[0px_10px_50px_rgba(61,55,241,0.25)]"
                    )


    # Section: Join these brands
    ui.image("assets/brand.png")


    # Section: Trending colleges
    with ui.column().classes("w-full items-center mt-16"):
        ui.label("Trending colleges").classes("text-4xl font-bold mb-6 text-purple-700")

        with ui.row().classes("gap-8 flex-wrap justify-center"):
            colleges = [
                {
                    "name": "Harvard University",
                    "location": "Cambridge, Massachusetts, USA",
                    "image": "assets/harvard.png",
                    "rating": "4.8",
                },
                {
                    "name": "Stanford University",
                    "location": "Stanford, California, USA",
                    "image": "assets/stanford.png",
                    "rating": "4.8",
                },
                {
                    "name": "Nanyang University",
                    "location": "Nanyang Ave, Singapore",
                    "image": "assets/nanyang.png",
                    "rating": "4.8",
                },
            ]

            for college in colleges:
                with ui.card().classes("w-80 shadow-lg"):
                    ui.image(college["image"]).classes("w-full h-40 object-cover rounded-t-lg")
                    with ui.column().classes("p-4"):
                        ui.label(college["name"]).classes("font-semibold text-lg")
                        ui.label(college["location"]).classes("text-gray-600 text-sm")
                        ui.label(f"⭐ {college['rating']}").classes("mt-2 text-yellow-600 font-bold")

        ui.button("Load more...").classes("mt-6 !bg-purple-600 text-white px-6 py-2 rounded")


# Blogs 
    with ui.column().classes("w-full items-center mt-16"):
        ui.label("Our Blogs").classes("text-4xl font-bold mb-6 text-purple-700")

        with ui.row().classes("gap-8 flex-wrap justify-center"):
            for i in range(3):
                with ui.card().classes("w-80"):
                    ui.image("assets/blog1.png").classes("w-full h-48 object-cover rounded-lg")
                    ui.label("Best Seller Book bootcamp-write&market books").classes(
                        "text-lg font-semibold mt-2"
                    )



    # Footer at the bottom
    show_footer()
