dat = read.csv(file="/home/nickedes/Workeda/suite/data/play_time.csv",header=TRUE,sep=",")
library(ggplot2)
g<-ggplot(data=dat, aes(x=Time,y=count)) + geom_bar(stat="identity")
g<-g+ggtitle('Plays')
library(extrafont)
g<-g+theme(plot.title = element_text(size=20,lineheight=.8, vjust=1,family="Bauhaus 93"))
g<-g + theme(axis.text.x=element_text(angle=60, size=10, vjust=0.5))
g