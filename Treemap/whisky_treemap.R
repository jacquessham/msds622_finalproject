library(tidyverse)
library(magrittr)
library(ggplot2)
library(treemapify)

setwd("/Users/jacquessham/Documents/MSDS/MSAN622/FinalProject/Data")
data <- read.csv("whisky_treemap_count.csv")


data %>% ggplot(aes(area=count, fill=region, label=text)) + geom_treemap() +
  geom_treemap_text(colour = "white", place = "centre") + 
  ggtitle("Scotch Whisky Proportion to Region Sold in Total Wine") + 
  theme(legend.position="none", plot.title = element_text(hjust = 0.5))
