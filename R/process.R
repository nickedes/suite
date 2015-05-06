data<-read.csv(file="../data/AirPassengers.csv",head=TRUE,sep=",")
plot(data$AirPassengers,data$time)
dev.copy(png,filename="../Results/plot.png")
dev.off ()