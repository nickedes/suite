data<-read.csv(file="data/AirPassengers.csv",head=TRUE,sep=",")
data
plot(data$AirPassengers,data$time)
dev.copy(png,filename="plot.png");
dev.off ();