from nicegui import ui

# Título
ui.label('Calculadora de operaciones básicas').classes('text-h4')

# Entrada de datos
num1 = ui.number(label='Número 1', value=0)
num2 = ui.number(label='Número 2', value=0)

# Resultado
resultado = ui.label('Resultado: 0').classes('text-h5')

# Funciones de operaciones
def sumar():
    suma = num1.value + num2.value
    resultado.text = f'Resultado: {suma}'
    ui.notify(f'Suma: {suma}')

def restar():
    resta = num1.value - num2.value
    resultado.text = f'Resultado: {resta}'
    ui.notify(f'Resta: {resta}')

def multiplicar():
    multiplicacion = num1.value * num2.value
    resultado.text = f'Resultado: {multiplicacion}'
    ui.notify(f'Multiplicación: {multiplicacion}')

def dividir():
    if num2.value != 0:
        division = num1.value / num2.value
        resultado.text = f'Resultado: {division}'
        ui.notify(f'División: {division}')
    else:
        resultado.text = 'Error: División por cero'
        ui.notify('No se puede dividir entre cero')

# Botones para cada operación
with ui.row():
    ui.button('Sumar', on_click=sumar)
    ui.button('Restar', on_click=restar)
    ui.button('Multiplicar', on_click=multiplicar)
    ui.button('Dividir', on_click=dividir)

# Ejecutar la app
ui.run()
