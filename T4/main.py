from nicegui import ui

ui.label('Hola mundo!')

ui.button("Haz click", on_click=lambda: ui.notify("Botón clickeado"))

ui.icon('star')

ui.run()