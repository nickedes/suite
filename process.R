data<-read.csv(file="data/AirPassengers.csv",head=TRUE,sep=",")
data
plot(data$AirPassengers,data$time)
dev.copy(jpeg,filename="plot.jpg");
dev.off ();