import tkinter as tk
from tkinter import filedialog
import main

def get_folder_path():
    folder_path = filedialog.askdirectory()
    entry_folder.delete(0, tk.END)
    entry_folder.insert(0, folder_path)

def get_exclusion_file_path():
    exclusion_file_path = filedialog.askopenfilename()
    entry_exclusion_file.delete(0, tk.END)
    entry_exclusion_file.insert(0, exclusion_file_path)

def get_output_zip_path():
    output_zip_path = filedialog.askdirectory()
    entry_output_zip.delete(0, tk.END)
    entry_output_zip.insert(0, output_zip_path)

def start_zip():
    root_folder = entry_folder.get()
    exclusion_file = entry_exclusion_file.get()
    output_zip = entry_output_zip.get()
    zip_name = entry_zip_name.get() + '.zip'

    main.zip_folder(root_folder, exclusion_file, output_zip, zip_name)

# Crear ventana principal
window = tk.Tk()

# Cambiar el nombre de la ventana
window.title("Aplicación de Compresión a .zip")

# Crear campos de entrada y etiquetas
label_folder = tk.Label(window, text="Ruta del proyecto a comprimir:")
entry_folder = tk.Entry(window, width=50)
button_folder = tk.Button(window, text="Seleccionar", command=get_folder_path)

label_exclusion_file = tk.Label(window, text="Ruta del archivo .txt que lista archivos a excluir:")
entry_exclusion_file = tk.Entry(window, width=50)
button_exclusion_file = tk.Button(window, text="Seleccionar", command=get_exclusion_file_path)

label_output_zip = tk.Label(window, text="Ruta destino zip resultante:")
entry_output_zip = tk.Entry(window, width=50)
button_output_zip = tk.Button(window, text="Seleccionar", command=get_output_zip_path)

label_zip_name = tk.Label(window, text="Nombre del archivo ZIP:")
entry_zip_name = tk.Entry(window, width=50)

button_start = tk.Button(window, text="Comenzar compresión", command=start_zip)

# Colocar los elementos en la ventana
label_folder.pack()
entry_folder.pack()
button_folder.pack()

label_exclusion_file.pack()
entry_exclusion_file.pack()
button_exclusion_file.pack()

label_output_zip.pack()
entry_output_zip.pack()
button_output_zip.pack()

label_zip_name.pack()
entry_zip_name.pack()

button_start.pack()

# Ejecutar el bucle de eventos de la ventana
window.mainloop()
