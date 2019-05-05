library(tidyverse)
library(maps)
library(geosphere)

setwd("/Users/jacquessham/Documents/MSDS/MSAN622/FinalProject/Data")
data <- read.csv("export2017.csv")
map('world',col="#f2f2f2", fill=TRUE, bg="white", lwd=0.05,mar=rep(0,4),border=0, ylim=c(-80, 80))

plot_my_connection=function(dep_lat, dep_lon, arr_lat, arr_lon, ...){
  inter <- gcIntermediate(c(dep_lon, dep_lat), c(arr_lon, arr_lat), n=50, addStartEnd=TRUE, breakAtDateLine=F)             
  inter=data.frame(inter)
  diff_of_lon=abs(dep_lon) + abs(arr_lon)
  if(diff_of_lon > 180){
    lines(subset(inter, lon>=0), ...)
    lines(subset(inter, lon<0), ...)
  }else{
    lines(inter, ...)
  }
}

stl_lat <- 38.63
stl_lon <- -90.20

for (i in 1:nrow(data)){
  plot_my_connection(stl_lat, stl_lon, data[i,4], data[i,5] , col="slateblue", lwd=2)
}
