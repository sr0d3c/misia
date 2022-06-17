# Lectura de un fichero
datos <- read.table(file = "datos_icb.txt",header = TRUE,stringsAsFactors = TRUE)
# La funcion read.table devuelve un objeto de tipo data.frame
class(datos)
summary(datos)
# Estimacion de modelo de regresion logistica
# la funcion glm permite estimar modelos lineales en funcion de la distribucion
# de la variable dependientek indicado en el parametro family estableciendo
# el valor binomial (logit)
rlog <- glm(recid ~ edad + tam,data = datos,family = binomial("logit"))
summary(rlog)
