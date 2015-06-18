# Trying some plots! Coz sometimes u don't know what u want 
dat = read.csv(file="/home/nickedes/Workeda/suite/data/nickedes.csv",header=TRUE,sep=",")
library(ggplot2)
# Density plot
ggplot(dat, aes(x=Artist)) + geom_density()