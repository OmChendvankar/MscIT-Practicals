##########################################
# section 7.1.5 Decision Trees in R
##########################################

library("rpart") # load libraries
library("rpart.plot")

setwd('E:\\LECTS\\BDA\\Prac\\data sets\\classification')
getwd()
# Read the data
play_decision <- read.table("DTdata.csv", header=TRUE, sep=",")
play_decision
View(play_decision)
summary(play_decision)

# build the decision tree
fit <- rpart(Play ~ Outlook + Temperature + Humidity + Wind,
             method="class",
             data=play_decision,
             control=rpart.control(minsplit=1),
             parms=list(split='information'))
summary(fit)

?rpart.plot
rpart.plot(fit, type=4, extra=1)
rpart.plot(fit, type=4, extra=1)
rpart.plot(fit, type=4, extra=2, clip.right.labs=FALSE,
           varlen=0, faclen=0)

newdata <- data.frame(Outlook="rainy", Temperature="mild",
                      Humidity="high", Wind=FALSE)
newdata

predict(fit,newdata=newdata,type="prob")
predict(fit,newdata=newdata,type="class")
