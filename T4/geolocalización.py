from nicegui import ui

# Definir las coordenadas de la ubicación 
lat = 20.08319
lon = -98.77372
# Construye la URL de Google Maps utilizando las coordenadas definidas y el idioma español.
map_url = f"https://www.google.com/maps?q={lat},{lon}&hl=es"
# Crear un botón que ejecuta JavaScript para abrir la URL de Google Maps en una nueva ventana del navegador.
6. 
ui.button('Ver mapa en Google Maps', on_click=lambda: ui.run_javascript(f'window.open("{map_url}", "_blank")'))
ui.run()