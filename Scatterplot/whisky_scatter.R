library(magrittr)
library(dplyr)
library(ggplot2)
library(ggrepel)

setwd("/Users/jacquessham/Documents/MSDS/MSAN622/FinalProject/Data")
data <- read.csv("data_scatter.csv", stringsAsFactors = F)

# EDA
data %>% ggplot() + geom_point(aes(x=min, y=max))
## There are outliers
# Filter out outliers
data <- data %>% filter(max < 5000)

labels_needed <- data %>% filter(min >90 | max > 1000)

# EDA again
data %>% ggplot() + geom_point(aes(x=min, y=max, color=factor(Region))) +
  geom_text_repel(data=labels_needed, aes(x=min, y=max, label=brand))+
  theme_minimal() +
  labs(x="Min Price($)", y="Max Price($)") +
  scale_color_discrete(name="Region") +
  ggtitle("Whisky Brand Min and Max Price in Total Wine")
