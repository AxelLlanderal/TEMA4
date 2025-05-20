from nicegui import ui
# poner filas 
with ui.row():
    with ui.card():
        ui.label('💰 Ventas')
        ui.label(' $1,200')
    with ui.card():
        ui.label('👤 Usuarios')
        ui.label(' 342')
    with ui.card():
        ui.label('🎟️ Tickets')
        ui.label(' 18')
ui.run()