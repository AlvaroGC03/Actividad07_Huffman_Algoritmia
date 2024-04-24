import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from collections import Counter
import os

#Ventana
window = tk.Tk()

def ventana_bienvenida():
    for widget in window.winfo_children():
        widget.destroy() #Esta funcion borra el contenido del widget
    ventana()
    ttk.Label(window, text="Bienvenido a la Actividad 07 - AGC").place(x=525, y=50) #Etiqueta pricipal mensaje
    ttk.Label(window, text="Selecciona Un Archivo").place(x=557, y=100) #mensaje de seleccionar archivo


def Abrir_Archivo(): #Función Seleccionar archivo
    filepath = askopenfilename(initialdir="/", title="Seleccion de Archivo", filetypes=(("Text files", "*.txt"), ("Todos los Archivos", "*.*"))) # Abre el explorador de archivos, filtrando solo archivos txt   
    return filepath #Retorna el archivo seleccionado


def ventana_archivo_abierto():
    for widget in window.winfo_children():
        widget.destroy() #Esta funcion borra el contenido del widget
    ventana()
    filepath = Abrir_Archivo() #Llama a la función Abrir_Archivo
    filename = os.path.basename(filepath) #Obtiene el nombre del archivo seleccionado
    archivos = ttk.Label(window, text="Seleccione Archivo:") #Etiqueta de seleccionar archivo
    archivos.place(x=555, y=50) #posicion de la etiqueta archivo
    archivos.configure(text="Archivo Abierto: \n\n"+ filename)#realiza la apertura del explorador de archivos y lo limita a los tipos .xlsx y csv

    with open(filepath, 'r') as file: #Abre el archivo seleccionado en modo lectura
        texto = file.read() #Lee el contenido del archivo
    lista = Counter(texto).most_common() #Cuenta la cantidad de caracteres en el archivo y el numero de veces que se repiten
    diccionario = dict(lista) #Convierte la lista en un diccionario

    # Crea un widget de texto
    output = tk.Text(window) 
    output.pack(expand=True, fill="x")
    # Se inserta el texto en el widget de texto 
    for key, value in diccionario.items(): #Recorre el diccionario y lo imprime en el widget de texto en formato de lista
        output.insert(tk.END, f'\n{key}: {value}\n') #Imprime el resultado en el widget de texto
    output.see() # Muestra el resultado en el widget de texto
    

def ventana():
    for widget in window.winfo_children():
        widget.destroy() #Esta funcion borra el contenido del widget

    button_frame = tk.Frame(window)
    button_frame.pack(side=tk.BOTTOM, padx=10, pady=10)
    # Boton Examinar 
    examinar_button = tk.Button(button_frame, text="Examinar", command=ventana_archivo_abierto)
    examinar_button.pack(side=tk.RIGHT, padx=5)
    #Boton Comprimir
    comprimir_button = tk.Button(button_frame, text="Comprimir")
    comprimir_button.pack(side=tk.RIGHT, padx=5)
    # Boton Descomprimir
    descomprimir_button = tk.Button(button_frame, text="Descomprimir")
    descomprimir_button.pack(side=tk.RIGHT, padx=5)

window.title("Actividad 07 - AGC") # Titulo en la ventana 
window.geometry("1200x700") # Tamaño de la ventana 
ventana_bienvenida()
window.mainloop() # Mainloop para correr ventana



