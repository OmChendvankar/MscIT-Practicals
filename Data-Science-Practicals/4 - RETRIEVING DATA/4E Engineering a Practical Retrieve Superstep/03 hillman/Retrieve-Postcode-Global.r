library(readr)
All_Countries <- read_delim("C:/VKHCG/03-Hillman/00-RawData/
All_Countries.txt",
                            "\t", col_names = FALSE,
                            col_types = cols(
                              X12 = col_skip(),
                              X6 = col_skip(),
                              X7 = col_skip(),
                              X8 = col_skip(),
                              X9 = col_skip()),
                            na = "null", trim_ws = TRUE)
write.csv(All_Countries,
          file = "C:/VKHCG/03-Hillman/01-Retrieve/01-EDS/01-R/Retrieve_All_Countries.csv")