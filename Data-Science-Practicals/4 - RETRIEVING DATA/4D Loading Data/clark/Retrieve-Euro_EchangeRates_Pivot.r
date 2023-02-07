###########################################
rm(list=ls()) #will remove ALL objects
###########################################
library(readr)
library(data.table)
library(stringi) 
###########################################
########### 
FileDir='C:/VKHCG/04-Clark/01-Retrieve/01-EDS/01-R'
FileName=paste0('Z:/Pracs/final/prac 4 Retrieve/4D Loading/clark/Euro_ExchangeRates.csv') 
Euro_EchangeRates <- read_csv(FileName, 
                    col_types = cols(
                      .default = col_double(),
                      Date = col_date(format = "%d/%m/%Y")
                    ), 
                    locale = locale(asciify = TRUE), na = "empty")
###########################################
FileNameOut=paste0(FileDir,'/Retrieve_Euro_EchangeRates_Pivot.csv')
fwrite(Euro_EchangeRates, FileNameOut)
###########################################
View(Euro_EchangeRates) 
###########################################
