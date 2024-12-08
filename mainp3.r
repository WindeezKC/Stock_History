# Libraries Needed
library(dplyr)
library(lubridate)

# Read CSV files, kinda normal
nvda <- read.csv("NVDA_data.csv")
tesla <- read.csv("TSLA_data.csv")
lock <- read.csv("LMT_data.csv")
raytheon <- read.csv("RTX_data.csv")

# Evens and their start dates list, same as in python pretty much
events <- list(
  "Ukraine/Russia" = "2022-02-24",
  "Israel/Palestine" = "2023-10-07",
  "Election 2020" = "2020-01-02",
  "Election 2024" = "2024-01-18",
  "China/HongKong" = "2020-06-30",
  "US Afghanistan" = "2021-08-15"
)

#Find the % change after 30 days from event
change <- function(stocks, start_date) {
  start_date <- as.Date(start_date)
  
# Date rangte for the stock price
  end_date <- start_date + days(30)
  stocks <- stocks %>%
    filter(as.Date(time) >= start_date & as.Date(time) <= end_date)
  
  if (nrow(stocks) > 0) {
#GEt the price for the 30 days now
        start_price <- stocks$close[which.min(abs(as.Date(stocks$time) - start_date))]
    end_price <- stocks$close[which.min(abs(as.Date(stocks$time) - end_date))]
    
#Simnple maths for the % change
    pctChange <- ((end_price - start_price) / start_price) * 100
    return(pctChange)
  } else {
    return(NA) #error catch in case in doesnt hold the 30 days
  }
}
#Loop through events and calculate the change
for (event in names(events)) {
  event_date <- events[[event]]
#Do it for each stock now
  nvdaChange <- change(nvda, event_date)
  tslaChange <- change(tesla, event_date)
  lockChange <- change(lock, event_date)
  rtxChange <- change(raytheon, event_date)
  
#Print
  print(paste("event:", event))
  print(paste("NVDA change:", nvdaChange))
  print(paste("TSLA change:", tslaChange))
  print(paste("LMT change:", lockChange))
  print(paste("RTX change:", rtxChange))
  
}
