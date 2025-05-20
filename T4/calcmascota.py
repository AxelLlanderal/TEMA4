from nicegui import ui
humano = ui.number(label='Edad humana')
resultado = ui.label()

def calcular():
 edad_mascota = int(humano.value) * 7 
 resultado.set_text(f'Edad estimada en años perrunos: {edad_mascota}')

ui.button('Calcular edad de mascota', on_click=calcular)

ui.run()