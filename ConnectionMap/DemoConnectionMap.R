.rs.restartR()

library(tidyverse)
library(maps)
library(geosphere)

map(wrap = c(0,360), fill = TRUE, col = 2) 

par(mar=c(0,0,0,0))
map('world',col="#f2f2f2", fill=TRUE, bg="white", lwd=0.05,mar=rep(0,4),border=0, ylim=c(-80, 80))
# map_data("world")

Buenos_aires=c(-58,-34)
Paris=c(2,49)
Melbourne=c(145,-38)
data=rbind(Buenos_aires, Paris, Melbourne) %>% as.data.frame()
colnames(data)=c("long","lat")

Buenos_aires=c(-58,-34)
Paris=c(2,49)
Melbourne=c(145,-38)
data=rbind(Buenos_aires, Paris, Melbourne) %>% as.data.frame()
colnames(data)=c("long","lat")

points(x=data$long, y=data$lat, col="slateblue", cex=1, pch=20)

inter <- gcIntermediate(Paris,  Buenos_aires, n=50, addStartEnd=TRUE, breakAtDateLine=F)             
lines(inter, col="slateblue", lwd=1)

plot_my_connection=function( dep_lon, dep_lat, arr_lon, arr_lat, ...){
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

plot_my_connection(Paris[1], Paris[2], Melbourne[1], Melbourne[2], col="slateblue", lwd=1)
plot_my_connection(Buenos_aires[1], Buenos_aires[2], Melbourne[1], Melbourne[2], col="slateblue", lwd=1)
plot_my_connection(Buenos_aires[1], Buenos_aires[2], Paris[1], Paris[2], col="slateblue", lwd=1)
text(rownames(data), x=data$long, y=data$lat,  col="black", cex=.5, pos=4)
