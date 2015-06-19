# Trying some plots! Coz sometimes u don't know what u want 
dat = read.csv(file="/home/nickedes/Workeda/suite/data/albums.csv",header=TRUE,sep=",")
library(ggplot2)
# Density plot
g<-ggplot(data=dat, aes(x=Album,y=count)) + geom_bar(stat="identity")
g<-g+ggtitle('Albums')
g<-g + theme(axis.text.x=element_text(angle=90, size=10, vjust=0.5))
g
