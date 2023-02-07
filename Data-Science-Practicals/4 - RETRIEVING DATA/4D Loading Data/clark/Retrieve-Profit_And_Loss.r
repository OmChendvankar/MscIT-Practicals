###########################################
rm(list=ls()) #will remove ALL objects
###########################################
library(readr)
library(data.table)
library(tibble) 

FileName=paste0('Z:/Pracs/final/prac 4 Retrieve/4D Loading/clark/Profit_And_Loss.csv') 
########################################### 
Profit_And_Loss <- read_csv(FileName,
                    col_types = cols(
                      Amount = col_double(), 
                      ProductClass1 = col_character(), 
                      ProductClass2 = col_character(), 
                      ProductClass3 = col_character(), 
                      QTR = col_character(), 
                      QTY = col_double(), 
                      TypeOfEntry = col_character()
                    ), na = "empty") 
View(Profit_And_Loss )
###########################################
### Sort the results
###########################################
keyList=c('QTR','TypeOfEntry','ProductClass1','ProductClass2','ProductClass3')
setorderv(Profit_And_Loss, keyList, order= c(-1L,1L,1L,1L,1L), na.last=FALSE)
###########################################
FileNameOut=paste0('Z:/Pracs/final/prac 4 Retrieve/4D Loading/clark/Retrieve_Profit_And_Loss.csv')
fwrite(Profit_And_Loss, FileNameOut)
###########################################
View(Profit_And_Loss)
###########################################
