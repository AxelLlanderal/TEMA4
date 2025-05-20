from nicegui import ui
#Los datos a guardar, se ocupan dos listas nombre y edad
datos = [
 {'Nombre': 'Ana', 'Edad': 21},
 {'Nombre': 'Luis', 'Edad': 23},
 {'Nombre': 'Carla', 'Edad': 22},
]
#Se usa una tabla donde se arreglan los datos,
ui.table(
	columns=[
		{'name': 'Nombre', 'label': 'Nombre', 'field': 'Nombre'},
		{'name': 'Edad', 'label': 'Edad', 'field': 'Edad'}
	],
	rows=datos,
	row_key='Nombre'
)
ui.run()