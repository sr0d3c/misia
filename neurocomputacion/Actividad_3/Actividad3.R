library(rminer)
library(nnet)

workingDir <- "C:/Users/sergi/Desktop/Code/Neurocomputacion/Actividad_3"
setwd(workingDir)

datos <- read.table(file=paste(workingDir,"datos_icb.txt",sep="/"), header=T, sep=" ", dec=".")

repHOut <- function(x, n, esq_val, neu){
  acc.tr <- c()
  acc.ts <- c()
  for (i in 1:n){
    ho <- holdout(x$recid, ratio = esq_val)
    train <- x[ho$tr,]
    test <- x[ho$ts,]
    fit <- nnet((recid=="SI") ~ edad+tam+grado+gang+quim+horm, data = train, size=neu,maxit=10000, decay=0.001)
    predicted.tr <- predict(fit, newdata=train, type="raw")
    predicted.ts <- predict(fit, newdata=test, type="raw")
    predicted_class.tr <- ifelse(predicted.tr>0.5, "SI","NO")
    predicted_class.ts <- ifelse(predicted.ts>0.5, "SI","NO")
    acc.tr <- c(acc.tr,sum(predicted_class.tr == train$recid)/length(train$recid))
    acc.ts <- c(acc.ts,sum(predicted_class.ts == test$recid)/length(test$recid))
  }
  list(X_acc.tr = mean(acc.tr), X_acc.ts = mean(acc.ts))
}

repHOut(datos, n=30, esq_val = 2/3, neu = 3)

result <- sapply(c(1:15), repHOut, x = datos, n = 30, esq_val = 2/3)

plot(unlist(result[1,]), type="l", col="blue", ylab="ACC", xlab="#Nhh", ylim = c(0.75, 1.00))
lines(unlist(result[2,]), type="l", col="red")

legend(8, .95, legend=c("Test", "Training"), col=c("red", "blue"), lty=1:2, cex=0.8)

