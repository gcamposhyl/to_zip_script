## Pasos

1. intalar (ambiente local):
    ```batch
    pip install pyinstaller
    ```

2. Abrir linea de comando (powershell) al nivel de init.py y ejecutar:
    ```batch
    pyinstaller --onefile --windowed init.py
    ```

3. Abrir carpeta dist, crear acceso directo de init

4. usar acceso directo para ejecutar programa

## ejemplo input promt

# ruta del proyecto a comprimir
root_folder = r'c:\Users\dev-h\OneDrive\Escritorio\proyectos_python\test_input'
# ruta del archivo .txt que lista archivos a excluir
exclusion_file = r'c:\Users\dev-h\OneDrive\Escritorio\proyectos_python\test_input\exclusiones.txt'
# ruta destino zip resultante
output_zip = r'c:\Users\dev-h\OneDrive\Escritorio\proyectos_python\test_output'
# nombre zip
zip_name = 'output.zip'

c:\Users\dev-h\OneDrive\Escritorio\proyectos_python\test_output\output.zip