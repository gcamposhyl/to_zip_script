import main

# ruta del proyecto a comprimir
root_folder = r'c:\Users\dev-h\OneDrive\Escritorio\proyectos_python\test_input'
# ruta del archivo .txt que lista archivos a excluir
exclusion_file = r'c:\Users\dev-h\OneDrive\Escritorio\proyectos_python\test_input\exclusiones.txt'
# ruta destino zip resultante
output_zip = r'c:\Users\dev-h\OneDrive\Escritorio\proyectos_python\test_output'
# nombre zip
zip_name = 'output.zip'

main.zip_folder(root_folder, exclusion_file, output_zip, zip_name)