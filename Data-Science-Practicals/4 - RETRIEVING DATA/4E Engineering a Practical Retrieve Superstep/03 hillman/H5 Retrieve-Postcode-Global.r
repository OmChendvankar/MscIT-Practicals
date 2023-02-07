InputFileName='All_Countries.txt'
OutputFileName='Retrieve_All_Countries.csv'
InputFileDir= 'C:/VKHCG/03-Hillman/00-RawData'
OutputFileDir='C:/VKHCG/03-Hillman/01-Retrieve/01-EDS/01-R'
###########################################
FileNameInput=paste0(InputFileDir,'/',InputFileName) 
FileNameInput
library(readr)
All_Countries <- read_delim(FileNameInput, "\t", col_names = FALSE, 
col_types = cols(
X12 = col_skip(), 
X6 = col_skip(), 
X7 = col_skip(), 
X8 = col_skip(), 
X9 = col_skip()), 
na = "null", trim_ws = TRUE)
View(All_Countries)
FileNameOutput=paste0(OutputFileDir,'/',OutputFileName) 
write.csv(All_Countries, file = FileNameOutput)
