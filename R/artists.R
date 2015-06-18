# Reading data from CSV
dat = read.csv(file="/home/nickedes/Workeda/suite/data/nickedes.csv",header=TRUE,sep=",")
library(ggplot2)
ggplot(data=dat, aes(x=Artist, y=Album)) + geom_bar(stat="identity")
