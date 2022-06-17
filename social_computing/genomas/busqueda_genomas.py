import os

direccion = "C:/Users/sergi/Desktop/Code/informatica_social/genomas/"
texto = "wax synthase"
contenido = os.listdir(direccion)
lines = []
directorios = []

def buscar(direc,txt):
    with open(direc) as f:
        datafile = f.readlines ()
    for line in datafile:
        if txt in line:
            lines.append(line)
    return lines

for dir in contenido:
    if os.path.isdir(dir):
        directorios.append(dir)


lineas = buscar(direccion,texto)
for linea in lineas:
    print(linea)
