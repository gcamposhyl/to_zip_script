import main

if __name__ == "__main__":
    root_folder = input("Ingresa la ruta de la carpeta a comprimir: ")
    exclusion_file = input("Ingresa la ruta del archivo .txt para exclusiones: ")
    output_zip = input("Ingresa la ruta de la carpeta destino para archivo .zip: ")
    output_zip = input("Ingresa la ruta de la carpeta destino para archivo .zip: ")
    zip_name = input("Ingresa el nombre del archivo")

    main(root_folder, exclusion_file, output_zip, zip_name)
    