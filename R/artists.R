# Reading data from CSV
dat = read.csv(file="/home/nickedes/Workeda/suite/data/nickedes.csv",header=TRUE,sep=",")
library(ggplot2)
# PLot of artist and der count!
ggplot(data=dat, aes(x=Artist)) + geom_bar(stat="bin")
