# TAMAÑO DE LA MUESTRA (TEOREMA CENTRAL DEL LÍMITE)

# Divide el gráfico en 2 figuras
par(mfrow = c(1,2))
# Histogramas de las distribuciones normales con media = 0 y std = 1
hist(rnorm(20))
hist(rnorm(20000))

# ACTIVIDAD
x <- runif(20,min = 0,max = 10)

# FUNCIONES DE LA FAMILIA APPLY

# Matriz de dos dimensiones
M <- matrix(seq(1,16),4,4)

# Aplica min a las filas
apply(M, 1, min)

# Aplica max a las columnas
apply(M, 2, max)

# Array de 3 dimensiones
M <- array(seq(32),dim = c(4,4,2))

# Aplica sum sobre la 2da y 3ra dimension del array
apply(M, 1, sum)

# Aplica sum sobre la 3ra dimension
apply(M,c(1,2),sum)

# LAPPLY
# Lista con 3 elementos, cada uno de ellos un vector
x <- list(a = 1, b = 1:3, c = 10:100)
lapply(x, FUN = length)
lapply(x, FUN = sum)
# SAPPLY
y <- list(a = 1, b = 1:3, c = 10:100)
# Comparar el resultado con la versión anterior de lapply
sapply(y, FUN = length)
# Obtendríamos el mismo resultados usando unlist(lapply...)
unlist(lapply(x, FUN = length))
sapply(x, FUN = sum)