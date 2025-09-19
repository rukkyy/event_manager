from nicegui import ui

def show_event_card(event):
    with ui.card().on(
        "click",
        lambda: ui.navigate.to(f"/event?id={event['id']}")
    ).classes("w-[30rem] h-[25rem] cursor-pointer"):
        ui.image(event["image"]).classes("w-full h-48 object-cover rounded-lg")
        ui.label(event["title"]).classes("text-lg font-semibold mt-2")
        ui.label(event["venue"]).classes("text-sm text-gray-600")

        