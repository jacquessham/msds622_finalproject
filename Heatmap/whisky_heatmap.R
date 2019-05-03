library(tidyverse)
library(magrittr)
library(ggplot2)

setwd("/Users/jacquessham/Documents/MSDS/MSAN622/FinalProject/Data")

data <- read.csv("whisky_heatmap.csv", stringsAsFactors = F)

data %>% ggplot(aes(x=Region, y=factor(Body))) + geom_tile(aes(fill=Winey)) +
  scale_fill_gradientn(colours = rev(heat.colors(5))) + theme_minimal() +
  labs(x="Regions", y="Body Score") +
  ggtitle("Scotch Whisky Average Smoky Score Relative to Body Score by Region")
