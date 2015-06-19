# Reading data from CSV
dat = read.csv(file="/home/nickedes/Workeda/suite/data/artists.csv",header=TRUE,sep=",")
library(ggplot2)
# PLot of artist and der count!
g<-ggplot(data=dat, aes(x=Artist,y=count)) + geom_bar(stat="identity")
g<-g+ggtitle('Artists')
library(extrafont)
g<-g+theme(plot.title = element_text(size=30,lineheight=.8, vjust=1,family="Bauhaus 93"))
g<-g + theme(axis.text.x=element_text(angle=90, size=10, vjust=0.5))
g
