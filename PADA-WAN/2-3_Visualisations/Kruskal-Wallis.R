#Adapted from: http://www.sthda.com/english/wiki/kruskal-wallis-test-in-r

#Set Up R
library(readxl)

#Import data
import_table <- read_excel("Downloads/2023-03-31-KW-TEST.xlsx")

#Confirm Headings
head(import_table)

#Perform Test
kruskal.test(import_table$`No. Genes` ~ import_table$`Panel-Type`, data = import_table)

#Interpret Results
"As the p-value is less than the significance level 0.05, we can conclude that there are significant differences between the treatment groups."
