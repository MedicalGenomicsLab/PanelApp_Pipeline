#Load the modules 
library(readxl)
library(ggplot2)

##########
#Figure 1a (New panels per month)
##########

import_table <- read_excel("Downloads/2023_03_31_1a_NewPanels.xlsx")

#Convert to data.frame and ensure dates are read as dates
df_temp <- data.frame(import_table)
df_temp$Date <- as.Date(df_temp$Date)

ggplot(data=df_temp, aes(x=Date-15, y=New.Panels, group=Type)) + 
  geom_line(aes(linetype=Type, color=Type), size=0.25) + 
  scale_linetype_manual(values=c("solid", "solid", "solid")) + 
  scale_color_manual(values=c("#353535","#B8B8B8", "#707070")) + 
  theme_light() + theme(text = element_text(size = 5)) + 
  geom_point(aes(color=Type, shape=Type), size=1) + 
  ylab("New Panels Released") + 
  ylim(0, 27) + xlab("Release Window (Months)") + theme(legend.position = "none")

##########
#Figure 1b (BarGraph)
#########

test <- read_excel("Downloads/2023_03_31_1b_BarGraph_MendRemoved.xlsx") 

#Revised Plot
ggplot(data=test, aes(x= reorder(Panel,No_Gene), y=No_Gene, fill=Gene_Type)) +
  geom_bar(stat="identity", position = "identity") + 
  theme_classic() + 
  scale_fill_manual(values=c("#586A6A", "#6BBF59")) +
  theme(legend.position = "none") +
  ylab("Panel Size (No. Genes)") + 
  xlab("Panels") +
  theme(axis.text.x = element_blank()) +
  theme(axis.ticks.x = element_blank()) +
  facet_wrap(vars(Panel_Type), scales = "free") +
  theme(text = element_text(size = 5))

##########
#Figure 1c (Releases per month)
##########

import_table <- read_excel("Downloads/2023_03_31_1c_Updates.xlsx")


#Plot
ggplot(data=df_temp, aes(x=Date-15, y=Updates, group=Panel_Type)) + 
  geom_line(aes(linetype=Panel_Type, color=Panel_Type), size=0.25) +
  scale_linetype_manual(values=c("solid", "solid", "solid")) + 
  scale_color_manual(values=c("#353535","#B8B8B8", "#707070")) + 
  theme_light() + theme(text = element_text(size = 5)) +
  geom_point(aes(color=Panel_Type, shape=Panel_Type), size=1) +
  ylab("No. Updates Made to Panels") +
  xlab("Release Window (Months)") + theme(legend.position = "none")

#Export
ggsave(filename=paste("2023-03-31_Figure1c","_90mm.png",sep=""), plot= last_plot(), path="~/Downloads/", width = 90, height = 60, units = "mm", dpi = 500)

##########
#Figure 1d (Panel Size vs. Releases)
##########
import_table <- read_excel("Downloads/2023_03_31_1d_ReleasesXSize.xlsx")

#Import data and process data
df_temp <- data.frame(import_table)

#Determine correlation
cor.test(df_temp$Updates, df_temp$Size, method = "pearson", conf.level = 0.95)

#Plot
ggplot(df_temp, aes(y=Updates, x=Size)) + 
  geom_point(alpha=0.5, size=0.6) +
  theme_classic() + 
  scale_y_continuous(trans = "log10") +
  scale_x_continuous(trans = "log10") + 
  theme(text = element_text(size = 5)) + 
  geom_smooth(method="lm", se=FALSE) +
  annotate("text", x = 100, y=10000, label = "Pearson Correlation : 0.80", size=2) +
  xlab("Panel Size (No. Genes)") + ylab ("No. Updates Made to Panel")

#Export
ggsave(filename=paste("2023-03-31_Figure1d","_90mm.png",sep=""), plot= last_plot(), path="~/Downloads/", width = 90, height = 60, units = "mm", dpi = 500)
