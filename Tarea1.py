import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

random.seed(113) #se maneja una semilla para que los resultados sean reproducibles (me gusta el 113)

def gen_points(n): #Funcion que genera los puntos aleatorios dentro del cuadrado [-2, 2] x [-2, 2] y los clasifica según al circulo al que pertenecen
    points = [(random.uniform(-2, 2), random.uniform(-2, 2)) for x in range(n)] #(x, y)
    circle_points = [[], [], []]  
    for x in points:
        if x[0]**2 + x[1]**2 <= 1: #circulo de radio 1
            circle_points[0].append(x)
        if x[0]**2 + x[1]**2 <= 2: #circulo de radio sqrt(2)
            circle_points[1].append(x)
        if x[0]**2 + x[1]**2 <= 4: #circulo de radio 2
            circle_points[2].append(x)
    return circle_points #devuelve unicamente los puntos que pertenecen a cada circulo


n_case = [100, 1000, 10000, 100000, 1000000]

error = []
aprox = []
numpoints = []
piaprox = [[], [], []]
for x in n_case: #para cada n se generan los puntos y se calculan las aproximaciones y errores
    points = gen_points(x)
    numpoints.append(len(points[0]))
    aprox.append(len(points[0]) / x)
    error.append(abs((len(points[0]) / x) - 0.19634954))
    piaprox[0].append(16 * (len(points[0]) / x))
    piaprox[1].append(8 * (len(points[1]) / x))
    piaprox[2].append(4 * (len(points[2]) / x))


fig, ax = plt.subplots(figsize=(8, 4.5))
plt.subplots_adjust(bottom=0.25)
ax.axis('off')
column = [['Valor de N', 'Puntos en Círculo', 'Aproximación', 'Error'], ['Valor de N', 'Aproximación', 'Aproximación de Pi', 'Error'], ['Valor de N', 'r = 1', "r =√2", 'r = 4'], ['Valor de N', 'error pi r = 1', 'error pi r = √2', 'error pi r = 4']]
titulos = ["Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 3 (Errores)"]

data = [[],[],[],[]] #lista que contiene los datos de las diferentes tablas
for i in range(len(n_case)): #meto los datos en la lista data para poder mostrarlos en las diferentes tablas
    data[0].append([
        n_case[i],                  
        numpoints[i],               
        aprox[i],                
        error[i],                  
    ])
    data[1].append([ 
    
        n_case[i],                  
        aprox[i],   
        piaprox[0][i],             
        error[i],                  
    ])
    data[2].append([
        n_case[i],
        piaprox[0][i],
        piaprox[1][i],
        piaprox[2][i]
    ])
    data[3].append([
        n_case[i],
        abs(piaprox[0][i] - np.pi),
        abs(piaprox[1][i] - np.pi),
        abs(piaprox[2][i] - np.pi)
    ])

index = 0 
def draw_table(): #funcion para dibujar la tabla correspondiente al indice actual
    ax.clear()
    ax.axis('off')
    

    tabla = ax.table(
        cellText=data[index],
        colLabels=column[index],
        loc='center',
        cellLoc='center'
    )
    
    tabla.scale(1, 1.6)
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(8)
    
    ax.set_title(titulos[index], fontsize=12, weight='bold', pad=15)
    
    fig.canvas.draw_idle()

def on_key(event): #boton para cambiar de tabla
    global index
    if event.key == 'right':
        index = (index + 1) % len(data)
        draw_table()

draw_table()
ax_boton = plt.axes([0.4, 0.08, 0.2, 0.06])
next_button = Button(ax_boton, 'Cambiar Tabla', color='#e1e1e1', hovercolor='#cccccc')
next_button.on_clicked(lambda event: on_key(type('Event', (object,), {'key': 'right'})()))
plt.show()
