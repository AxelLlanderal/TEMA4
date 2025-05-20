from nicegui import ui
#Función para que se muestre el color elegido
def mostrar():
    ui.notify(f'Color: {color.value}, Tema oscuro: {tema.value}')
#Valores a elegir y declaración de palabras
color = ui.select(['Rojo', 'Verde', 'Azul'], label='Color favorito')
tema = ui.switch('Tema oscuro')
ui.button('Guardar preferencias', on_click=mostrar)

ui.run()