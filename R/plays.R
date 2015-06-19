dat = read.csv(file="/home/nickedes/Workeda/suite/data/play_time.csv",header=TRUE,sep=",")
library(ggplot2)
g<-ggplot(data=dat, aes(x=Time,y=count)) + geom_bar(stat="identity")
g<-g+ggtitle('Plays')
g