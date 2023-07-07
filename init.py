import main

if __name__ == "__main__":
    input_option = input('''
Desplegar archivo en Python Anywhere => Digite 1
Comprimir archivo en local => Digite 2
                         
''')

    if input_option == "1":
        pass
    elif input_option == "2":
        root_folder = input("Ingresa la ruta de la carpeta a comprimir: ")
        exclusion_file = input("Ingresa la ruta del archivo .txt para exclusiones: ")
        output_zip = input("Ingresa la ruta de la carpeta destino para archivo .zip: ")
        output_zip = input("Ingresa la ruta de la carpeta destino para archivo .zip: ")
        zip_name = input("Ingresa el nombre del archivo")

    main(root_folder, exclusion_file, output_zip, zip_name)
    