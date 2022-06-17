library(caret)
library(rminer)
library(nnet)
library(pROC)

workingDir <- "C:/Users/sergi/Desktop/Code/Neurocomputacion/Actividad_4"
setwd(workingDir)

datos <- read.table(file=paste(workingDir,"datos_icb.txt",sep="/"), header=T, sep=" ", dec=".")

folds <- createFolds(datos$recid, k=10)

crossVal <- function(x){
  auc.tr <- c()
  auc.ts <- c()
  fold.tr <- datos[-x, ]
  fold.ts <- datos[x, ]
  rlog <- glm(as.factor(fold.tr$recid) ~ .,data = fold.tr,family = binomial("logit"))
  #rlog.ts <- glm(as.factor(fold.ts$recid) ~ .,data = fold.ts,family = binomial("logit"))
  pred.tr <- predict(rlog, type = "response",newdata=fold.tr)
  pred.ts <- predict(rlog, type = "response", newdata=fold.ts)
  recid.tr <- ifelse(fold.tr$recid == "SI", 1, 0)
  recid.ts <- ifelse(fold.ts$recid == "SI", 1, 0)
  auc.tr <- c(auc(recid.tr,pred.tr,levels = c(0, 1), direction = "<"))
  auc.ts <- c(auc(recid.ts,pred.ts,levels = c(0, 1), direction = "<"))
  list(auc.tr, auc.ts)
}
result <- sapply(folds, crossVal)
X_auc.cross.tr <- mean(unlist(result[1,]))
X_auc.cross.ts <- mean(unlist(result[2,]))
print(X_auc.cross.ts)
print(X_auc.cross.tr)

repHOut <- function(x, n, esq_val, neu){
  auc.tr <- c()
  auc.ts <- c()
  for (i in 1:n){
    ho <- holdout(x$recid, ratio = esq_val)
    train <- x[ho$tr,]
    test <- x[ho$ts,]
    fit <- nnet((recid=="SI") ~ ., data = train, size=neu,maxit=10000, decay=0.001)
    predicted.tr <- predict(fit, newdata=train, type="raw")
    predicted.ts <- predict(fit, newdata=test, type="raw")
    recid.tr <- ifelse(train$recid == "SI", 1, 0)
    recid.ts <- ifelse(test$recid == "SI", 1, 0)
    auc.HO.tr <- c(auc(recid.tr,predicted.tr,levels = c(0, 1), direction = "<"))
    auc.HO.ts <- c(auc(recid.ts,predicted.ts,levels = c(0, 1), direction = "<"))
  }
  list(X_acc.tr = mean(auc.HO.tr), X_acc.ts = mean(auc.HO.ts))
}

result.HO <- repHOut(datos, n=30, esq_val = 2/3, neu = 3)
print(result.HO)

result.cross <- sapply(folds, crossVal)
result.cross <- result.cross[mean(result.cross[1,]),mean(result.cross[2,])]





