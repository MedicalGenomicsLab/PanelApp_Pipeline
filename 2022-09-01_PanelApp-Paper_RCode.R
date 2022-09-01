#Setup
library(ggplot2)

#Figure 1a
import_table <- read.table("/Users/alanr/Downloads/2022-08-18_Paper_Fig1b.txt", sep='\t', quote='', header=TRUE)
df_temp <- data.frame(import_table)
df_temp$Date <- as.Date(df_temp$Date)
ggplot(data=df_temp, aes(x=Date-15, y=New.Panels)) + geom_line(size=0.25) +theme_light() + theme(text = element_text(size = 5)) + geom_point(size=0.5) + ylab("New Conditions") + ylim(0, 17) + xlab("Months")
ggsave(filename=paste("2022-08-18_Figure1a","90mm_.png",sep=""), plot= last_plot(), path="~/Downloads/", width = 90, height = 60, units = "mm", dpi = 500)

#Figure 1b
import_table <- read.table("/Users/alanr/Downloads/2022-08-18_Paper_Fig1a.txt", sep='\t', quote='', header=TRUE)
df_temp <- data.frame(import_table)
df_temp$Date <- as.Date(df_temp$Date)
ggplot(data=df_temp, aes(x=Date-15, y=Releases)) + geom_line(size=0.25) +theme_light() + theme(text = element_text(size = 5)) + geom_point(size=0.5) + ylab("No. Updated Panels") + ylim(0, 3000) + xlab("Months")
ggsave(filename=paste("2022-08-18_Figure1b","90mm_.png",sep=""), plot= last_plot(), path="~/Downloads/", width = 90, height = 60, units = "mm", dpi = 500)

#Figure 1c
import_table <- read.table("/Users/alanr/Downloads/2022-08-18_Paper_Fig1c.txt", sep='\t', quote='', header=TRUE)
df_temp <- data.frame(import_table)
ggplot(df_temp, aes(y=Releases, x=Genes)) + geom_point(alpha=0.4, size=0.5) + theme_light() + scale_x_continuous(trans='log10') + scale_y_continuous(trans='log10') + ylab("No. Genes") + xlab ("No. Releases") + theme(text = element_text(size = 5))
ggsave(filename=paste("2022-08-18_Figure1c","90mm_.png",sep=""), plot= last_plot(), path="~/Downloads/", width = 90, height = 60, units = "mm", dpi = 500)

#Figure 1d
import_table <- read.table("/Users/alanr/Downloads/2022-08-18_Paper_Fig1d.txt", sep='\t', quote='', header=TRUE)
df_temp <- data.frame(import_table)
ggplot(df_temp, aes(x=reorder(Variable, -Count), y=Count, fill=Variable, col=Variable, alpha=Variable)) + geom_boxplot() + scale_y_continuous(trans = "log10") + theme_light() + scale_fill_manual(values = c("#00843D", "#FFCD00")) +scale_color_manual(values=c("#00843D","#FFCD00")) + scale_alpha_manual(values=c(0.65,0.55)) + theme(legend.position = "none") + xlab("") + ylab("No. Genetic Entities") + theme(text = element_text(size = 5))
ggsave(filename=paste("2022-08-18_Figure1d","90mm_.png",sep=""), plot= last_plot(), path="~/Downloads/", width = 90, height = 60, units = "mm", dpi = 500)

#Figure 2a
library(ggplot2)
library(ggalt)
import_table <- read.table("/Users/alanr/Downloads/2022-08-21_Paper_Fig2a.txt", sep='\t', quote='', header=TRUE)
df_temp <- data.frame(import_table)
import_table_sub <- read.table("/Users/alanr/Downloads/2022_08_22-Paper2a-Subset.txt", sep='\t', quote='', header=TRUE)
subset_2a <- data.frame(import_table_sub)
re_ordered_data <- df_temp
re_ordered_data$Status <- factor(re_ordered_data$Status, levels=c(
  "Diagnostic Genes - Total Gene Changes",
  "Diagnostic Genes - Genes  Lost (Removed + Downgraded)", 
  "Diagnostic Genes - Genes Downgraded", 
  "Diagnostic Genes - Genes Removed", 
  "Diagnostic Genes - Genes Gained (Added + Upgraded)", 
  "Diagnostic Genes - Genes Upgraded", 
  "Diagnostic Genes - Genes Added", 
  "Diagnostic Genes - Net Differences", 
  "All Genes - Total Gene Changes", 
  "All Genes - Genes Removed",
  "All Genes - Genes Added",
  "All Genes - Net Differences"))
my.labels.vert = c(
  "All Genes\nNet Differences", 
  "All Genes\nGenes Added",
  "All Genes\nGenes Removed" ,
  "All Genes\nTotal Gene Changes" ,
  "Diagnostic Genes\nNet Differences",
  "Diagnostic Genes\nGenes Added",
  "Diagnostic Genes\nGenes Upgraded",
  "Diagnostic Genes\nGenes Gained\n(Added + Upgraded)",
  "Diagnostic Genes\nGenes Removed",
  "Diagnostic Genes\nGenes Downgraded",
  "Diagnostic Genes\nGenes Lost\n(Removed + Downgraded)",
  "Diagnostic Genes\nTotal Gene Changes")
ggplot(data = re_ordered_data, aes(Change,Status, colour=Status)) + geom_boxplot(lwd=0.25, fatten = 1, outlier.size = 0.35) + geom_encircle( data=subset_2a,   color="red", alpha=0.5,   size=0.85,    expand=0.0175, spread=0.02) + geom_boxplot(lwd=0.25, fatten = 1, outlier.size = 0.35) + theme_light() + xlab("No. Altered Genes") + ylab("") + theme(legend.position="none", axis.text.x = element_text(size = 3)) + scale_color_manual(values=c("#00843D", "#00843D", "#00843D", "#00843D","#00843D", "#00843D", "#00843D", "#00843D", "#FFCD00","#FFCD00","#FFCD00","#FFCD00"))  + theme(text = element_text(size = 4)) + geom_point(data=subset_2a, colour="red", size=0.45)  + scale_y_discrete(labels = c('Diagnostic Genes\nTotal No. Gene Changes', 'Diagnostic Genes\nNo. Genes Lost \n(Removed + Downgraded)','Diagnostic Genes\nNo. Genes Downgraded','Diagnostic Genes\nNo. Genes Removed','Diagnostic Genes\nNo. Genes Gained\n(Added + Upgraded)', 'Diagnostic Genes\nNo. Genes Upgraded', 'Diagnostic Genes\nNo. Genes Added', 'Diagnostic Genes\nNet Differences', 'All Genes\nTotal No. Gene Changes', 'All Genes\nNo. Genes Removed','All Genes\nNo. Genes Added', 'All Genes\nNet Differences'))
ggsave(filename=paste("2022-08-21_Figure2a","_90mm.png",sep=""), plot= last_plot(), path="~/Downloads/", width = 90, height = 60, units = "mm", dpi = 800)
ggsave(filename=paste("2022-08-21_Figure2a","_190mm.png",sep=""), plot= last_plot(), path="~/Downloads/", width = 190, height = 60, units = "mm", dpi = 800)

#Figure2b

library(ggplot2)
library(ggalt)
import_table <- read.table("/Users/alanr/Downloads/2022-08-21_Paper_Fig2b.txt", sep='\t', quote='', header=TRUE)
df_temp <- data.frame(import_table)
import_table <- read.table("/Users/alanr/Downloads/2022-08-22_Paper2b-Subset.txt", sep='\t', quote='', header=TRUE)
subset_2b <- data.frame(import_table)
re_ordered_data <- df_temp
re_ordered_data$Status <- factor(re_ordered_data$Status, levels=c(
   "Diagnostic Genes - Total Gene Changes",
   "Diagnostic Genes - Genes  Lost (Removed + Downgraded)", 
   "Diagnostic Genes - Genes Downgraded", 
   "Diagnostic Genes - Genes Removed", 
   "Diagnostic Genes - Genes Gained (Added + Upgraded)", 
   "Diagnostic Genes - Genes Upgraded", 
   "Diagnostic Genes - Genes Added", 
   "Diagnostic Genes - Net Differences", 
   "All Genes - Total Gene Changes", 
   "All Genes - Genes Removed",
   "All Genes - Genes Added",
   "All Genes - Net Differences"))
my.labels.vert = c(
  "All Genes\nNet Differences", 
  "All Genes\nGenes Added",
  "All Genes\nGenes Removed" ,
  "All Genes\nTotal Gene Changes" ,
  "Diagnostic Genes\nNet Differences",
  "Diagnostic Genes\nGenes Added",
  "Diagnostic Genes\nGenes Upgraded",
  "Diagnostic Genes\nGenes Gained\n(Added + Upgraded)",
  "Diagnostic Genes\nGenes Removed",
  "Diagnostic Genes\nGenes Downgraded",
  "Diagnostic Genes\nGenes Lost\n(Removed + Downgraded)",
  "Diagnostic Genes\nTotal Gene Changes")
ggplot(data = re_ordered_data, aes(Change, Status, colour=Status)) + geom_encircle( data=subset_2b, color="red", alpha=0.5, size=0.85, expand=0.0175, spread=0.02) + geom_boxplot(lwd=0.25, fatten = 1, outlier.size = 0.35) + theme_light() + xlab("Proportion of Altered Genes") + ylab("") + theme(legend.position="none", axis.text.x = element_text(size = 3)) + scale_color_manual(values=c("#FFCD00", "#00843D", "#00843D", "#FFCD00","#00843D", "#FFCD00", "#00843D", "#FFCD00", "#00843D","#00843D","#00843D","#00843D"))  + theme(text = element_text(size = 4)) + geom_point(data=subset_2b, colour="red", size=0.45)  + scale_y_discrete(labels = c('Diagnostic Genes\nTotal No. Gene Changes', 'Diagnostic Genes\nNo. Genes Lost \n(Removed + Downgraded)','Diagnostic Genes\nNo. Genes Downgraded','Diagnostic Genes\nNo. Genes Removed','Diagnostic Genes\nNo. Genes Gained\n(Added + Upgraded)', 'Diagnostic Genes\nNo. Genes Upgraded', 'Diagnostic Genes\nNo. Genes Added', 'Diagnostic Genes\nNet Differences', 'All Genes\nTotal No. Gene Changes', 'All Genes\nNo. Genes Removed','All Genes\nNo. Genes Added', 'All Genes\nNet Differences')) + scale_x_continuous(labels = scales::percent)
ggsave(filename=paste("2022-08-22_Figure2b","_90mm.png",sep=""), plot= last_plot(), path="~/Downloads/", width = 90, height = 60, units = "mm", dpi = 800)
ggsave(filename=paste("2022-08-22_Figure2b","_190mm.png",sep=""), plot= last_plot(), path="~/Downloads/", width = 190, height = 60, units = "mm", dpi = 800)

#Figure3
files <- list.files(path="/Users/alanr/Desktop/PanelApp_Data/June_2022_GenesOnly/AU/_CumulativeReclassifications", pattern="*.txt", full.names=TRUE, recursive=FALSE)

lapply(files, function(x) {
  ID0 <- strsplit(x, split = "/")
  ID1<-ID0[[1]][9]
  ID1
  ID2 <- strsplit(ID1, split = "_AU_")
  ID3 <- ID2[[1]][1]
  
  t <- read.table(x, header=TRUE)
  df_production <- data.frame(t)
  df_production$Month <- as.Date(df_production$Month)
  threshold_percentage <- df_production[1,10]*.286
  threshold_numerical <- 9
  y_max <- (df_production$Cumulative_Changed_DiaGenes[30]*1.1) + 15
  #if(is.na(y_max)) {y_max <- 15
  #}else{
  #if(y_max < threshold_percentage) {y_max <- threshold_percentage} else {y_max <- y_max }}
  
  #Single Column
  ggplot(data=df_production, aes(x=Month-15, y=DiaGenes_Gained.Cumulative.)) + geom_line(color = "#00843D", size=0.5) + geom_point(color = "#00843D", size=0.75)  + theme_light(base_size = 4) + geom_hline(yintercept=threshold_percentage, linetype="dashed",color = "#628395", size=0.4, alpha = 0.75) + geom_hline(yintercept=threshold_numerical,color = "#dbad6a", size=0.4, alpha = 0.75) + ylab("No. Gained Diagnostic Genes") + xlab("Months") + annotate("label", y = df_production$DiaGenes_Gained.Cumulative.[1]-6.6, x = as.Date("2020-07-31"), label=paste(" Panel:",ID3,"\n","Diagnostic Genes in Initial Release:",df_production$No.DiaGenes[1], sep=" ", size=3), hjust = 0, size=2.25) + ylim(-10,y_max)
  ggsave(filename=paste("Cumulative-Reclassification-Plot_",ID3,".png",sep=""), plot= last_plot(), path="~/Downloads/Cumulative_Reclassification_Plots-90mm", width = 90, height = 60, units = "mm", dpi = 500)  
  
  #Double Column
  ggplot(data=df_production, aes(x=Month-15, y=DiaGenes_Gained.Cumulative.)) + geom_line(color = "#00843D", size=0.3) + geom_point(color = "#00843D", size=0.65) + theme_light(base_size = 4) + geom_hline(yintercept=threshold_percentage, linetype="dashed",color = "#628395", size=0.2, alpha = 0.75) + geom_hline(yintercept=threshold_numerical,color = "#dbad6a", size=0.2, alpha = 0.75) + ylab("No. Gained Diagnostic Genes") + xlab("Months") + annotate("label", y = df_production$DiaGenes_Gained.Cumulative.[1]-5, x = as.Date("2021-07-31"), label=paste(" Panel:",ID3,"\n","Diagnostic Genes in Initial Release:",df_production$No.DiaGenes[1], sep=" ", size=4), hjust = 0, size=2) + ylim(-10,y_max)
  ggsave(filename=paste("Cumulative-Reclassification-Plot_",ID3,".png",sep=""), plot= last_plot(), path="~/Downloads/Cumulative_Reclassification_Plots-190mm", width = 190, height = 90, units = "mm", dpi = 500) 
})
