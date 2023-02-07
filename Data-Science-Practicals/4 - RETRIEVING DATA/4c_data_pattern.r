# 4C Data Pattern

# Executed by Nikhil K Pawanikar
# MScIT Part 1 - Sem 1 
# University Department of Information Technology
# 01-Jan-2022
# https://colab.to/r

library(readr)
library(data.table)

FileName=paste0('C:/Users/NGT/Desktop/Input files/IP_DATA_ALL_SMALL.csv')

IP_DATA_ALL = read_csv(FileName)

IP_DATA_ALL

hist_country=data.table(Country=unique(IP_DATA_ALL$Country))
hist_country

pattern_country=data.table(Country=hist_country$Country,PatternCountry=hist_country$Country)
pattern_country

oldchar=c(letters,LETTERS)
newchar=replicate(length(oldchar),"A")
oldchar
newchar

for (r in seq(nrow(pattern_country))){
s=pattern_country[r,]$PatternCountry;
for (c in seq(length(oldchar))){
s=chartr(oldchar[c],newchar[c],s)
};
for (n in seq(0,9,1)){
s=chartr(as.character(n),"N",s)
};
s=chartr(" ","b",s)
s=chartr(".","u",s)
pattern_country[r,]$PatternCountry=s;
};
View(pattern_country)

# pattern on Lattitude data
library(readr)
library(data.table)

#FileName=paste0('/content/IP_DATA_ALL_SMALL.csv')
IP_DATA_ALL = read_csv(FileName)

hist_latitude=data.table(Latitude=unique(IP_DATA_ALL$Latitude))
hist_latitude

pattern_latitude=data.table(latitude=hist_latitude$Latitude, Patternlatitude=as.character(hist_latitude$Latitude))
pattern_latitude

oldchar=c(letters,LETTERS)
newchar=replicate(length(oldchar),"A")

for (r in seq(nrow(pattern_latitude))){
s=pattern_latitude[r,]$Patternlatitude;
for (c in seq(length(oldchar))){
s=chartr(oldchar[c],newchar[c],s)
};
for (n in seq(0,9,1)){
s=chartr(as.character(n),"N",s)
};
s=chartr(" ","b",s)
s=chartr("+","u",s)
s=chartr("-","u",s)
s=chartr(".","u",s)
pattern_latitude[r,]$Patternlatitude=s;
};

setorder(pattern_latitude,latitude)

View(pattern_latitude[1:3])
