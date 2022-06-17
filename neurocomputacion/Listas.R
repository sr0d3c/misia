# En R se usa la función list() para crear una lista
(alumno <- list("Jose",47,TRUE))
# str permite acceder al contenido de la lista
str(alumno)

length(alumno)
# mode devuelve el tipo de objeto al igual que class
mode(alumno)
class(alumno)
# La funcion names permite crear o cambiar los nombres de los elementos de una lista
names(alumno) <- c("nombre","edad","estado")

# La indexacion se realiza mediante los operadores [], que permiten obtener un elemento en formato lista
alumno[2]

# o se puede realizar la idexacion mediante el operador [[]] o $ que permiten recuperar los elementos de la lista en el formato de almacenamiento original
alumno[[1]]
mode(alumno[[1]])
alumno$nombre

# la funcion data.frame se utiliza para crear objetos del tipo data.frame
datos <- data.frame(nombre = c("jose","juan","pedro"), edad = c(47,54,34), estado = c(TRUE,FALSE,TRUE))

str(datos)

mode(datos)
class(datos)

datos[1,2]
datos[1,]
datos[,1]
datos[1,"edad"]

# La funcion matrix se usa para construir matrices en R
runif(10)
mat <- matrix(nrow = 2, ncol = 5)
dim(mat)
nrow(mat)
ncol(mat)
rownames(mat)
