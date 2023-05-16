#Set everything up
library(ggplot2)

#Import data
import_table <- read_excel("Downloads/2023-03-31_PanelApp-Figure2.xlsx")

#Reorder data for boxplot
import_table$`Type of Change` <- factor(import_table$`Type of Change` , levels = c("Total Gene Changes", "Gene Gains", "Gene Additions", "Gene Upgrades", "Gene Losses", "Gene Removals", "Gene Downgrades"))

ggplot(import_table, aes(x=`Type of Change`, y=`No. Genes`, fill=Cohort)) + 
  geom_boxplot(lwd=0.2, outlier.size=0.5) + 
  facet_grid(import_table$Cohort ~ ., scales="free", switch = "y") + 
  theme_light() + 
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) + 
  theme(strip.text.y = element_text(size = 5, color = "Black", face = "bold.italic")) +
  theme(legend.position = "none")  + 
  scale_fill_manual(values=c( "#707070", "#B8B8B8")) +
  theme(axis.title.x = element_blank()) +
  theme(text = element_text(size = 5))

#Export
ggsave(filename=paste("2023-03-31_Figure2","_90mm.png",sep=""), plot= last_plot(), path="~/Downloads/", width = 90, height = 90, units = "mm", dpi = 500)
