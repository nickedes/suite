data<-read.csv(file="data/AirPassengers.csv",head=TRUE,sep=",")
pdf("myfile.pdf",width=8,height=6)
plot(data$AirPassengers,data$time)
dev.off()