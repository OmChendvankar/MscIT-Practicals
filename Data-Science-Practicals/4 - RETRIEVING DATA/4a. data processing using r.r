library(readr)
IP_DATA_ALL <- read_csv("C:/Users/NGT/Desktop/Input files/IP_DATA_ALL.csv")
View(IP_DATA_ALL)
IP_DATA_ALL
spec(IP_DATA_ALL)
library(tibble)
set_tidy_names(IP_DATA_ALL, syntactic = TRUE, quiet = FALSE)

spec(IP_DATA_ALL)

IP_DATA_ALL_FIX=set_tidy_names(IP_DATA_ALL, syntactic = TRUE, quiet = TRUE)
View(IP_DATA_ALL_FIX)

FileName= paste0('C:/Users/NGT/Desktop/Input files/IP_DATA_ALL_FIX.csv')

write.csv(IP_DATA_ALL_FIX, FileName)

#Unique Identifier of Each Data Entry
IP_DATA_ALL_with_ID=rowid_to_column(IP_DATA_ALL_FIX, var = "RowID")
View(IP_DATA_ALL_with_ID)

FileName=paste0("C:/Users/NGT/Desktop/Input files/IP_DATA_ALL_with_ID.csv")

write.csv(IP_DATA_ALL_with_ID,FileName)

#Data Type of Each Data Column
sapply(IP_DATA_ALL_with_ID, typeof)

library(data.table)
hist_country=data.table(Country=unique(IP_DATA_ALL_with_ID[is.na(IP_DATA_ALL_with_ID ['Country']) == 0, ]$Country))
View(hist_country)

setorder(hist_country,'Country')
View(hist_country)

hist_country_with_id=rowid_to_column(hist_country, var = "RowIDCountry")
View(hist_country_with_id)

IP_DATA_COUNTRY_FREQ=data.table(with(IP_DATA_ALL_with_ID, table(Country)))
View(IP_DATA_COUNTRY_FREQ)

FileName=paste0("C:/Users/NGT/Desktop/Input files/IP_DATA_COUNTRY_FREQ.csv")
write.csv(IP_DATA_COUNTRY_FREQ,FileName)

# Profiling the data lake, 
#frequency of lattitude
library(data.table)
hist_latitude =data.table(Latitude=unique(IP_DATA_ALL_with_ID [is.na(IP_DATA_ALL_with_ID ['Latitude']) == 0, ]$Latitude))
setkeyv(hist_latitude, 'Latitude')
setorder(hist_latitude)
hist_latitude_with_id=rowid_to_column(hist_latitude, var = "RowID")
View(hist_latitude_with_id)

IP_DATA_Latitude_FREQ=data.table(with(IP_DATA_ALL_with_ID,
table(Latitude)))
View(IP_DATA_Latitude_FREQ)
FileName=paste0("C:/Users/NGT/Desktop/Input files/IP_DATA_Latitude_FREQ.csv")
write.csv(IP_DATA_Latitude_FREQ,FileName)

# similar process for longitude

#Minimum Value
min(hist_country$Country)
or
sapply(hist_country[,'Country'], min, na.rm=TRUE)

# Maximum Value
max(hist_country$Country)
or
sapply(hist_country[,'Country'], max, na.rm=TRUE)

# mean
sapply(hist_latitude_with_id[,'Latitude'], mean, na.rm=TRUE)
#sapply(hist_longitude_with_id[,'Longitude'], mean, na.rm=TRUE)

#Median
sapply(hist_latitude_with_id[,'Latitude'], median, na.rm=TRUE)

# Mode
IP_DATA_COUNTRY_FREQ=data.table(with(IP_DATA_ALL_with_ID, table(Country)))
setorder(IP_DATA_COUNTRY_FREQ,-N)
IP_DATA_COUNTRY_FREQ[1,'Country']

IP_DATA_Latitude_FREQ=data.table(with(IP_DATA_ALL_with_ID,
table(Latitude)))
setorder(IP_DATA_Latitude_FREQ,-N)
IP_DATA_Latitude_FREQ[1,'Latitude']


# Range
sapply(hist_latitude_with_id[,'Latitude'], range, na.rm=TRUE)


# Quartiles
sapply(hist_latitude_with_id[,'Latitude'], quantile, na.rm=TRUE)

#Standard Deviation
sapply(hist_latitude_with_id[,'Latitude'], sd, na.rm=TRUE)

#Skewness
library(e1071)
skewness(hist_latitude_with_id$Latitude, na.rm = FALSE, type = 2)

#missing values
missing_country=data.table(Country=unique(IP_DATA_ALL_with_ID[is.na(IP_DATA_ALL_with_ID ['Country']) == 1, ]))
View(missing_country)
