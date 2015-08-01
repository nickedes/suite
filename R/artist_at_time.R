readinteger <- function()
{ 
  n <- readline(prompt="Enter time in the range 0-24 hrs: ")
  return(as.integer(n))
}

# Time range
start = readinteger()
end = start + 1

# Reading data from CSV
dat = read.csv(file="/home/nickedes/Workeda/suite/data/artists.csv",header=TRUE,sep=",")

# PLotting library
library(ggplot2)
