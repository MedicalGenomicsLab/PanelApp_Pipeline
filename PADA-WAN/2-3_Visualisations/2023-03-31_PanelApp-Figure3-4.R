#Set up space
library(ggplot2)

#Determine list of files of process
files <- list.files(path="/Users/alan/Desktop/QIMR-23/PanelApp_Data/June_2022_GenesOnly/AU/_CumulativeReclassifications", pattern="*.txt", full.names=TRUE, recursive=FALSE)

#######
#MASS PRODUCTION 
#######

#SPECIFIC

lapply(files, function(x) {
  #Extract Panel Name and Panel ID
  
  ID0 <- strsplit(x, split = "/")     
  ID1<-ID0[[1]][10]                       #First part of the file name (not the location)
  ID2 <- strsplit(ID1, split = "_AU_")    
  ID3 <- ID2[[1]][1]
  ID4 <- strsplit(ID3, split = ')', fixed=TRUE)
  ID5 <- strsplit(ID4[[1]][1], split = '(', fixed=TRUE)  
  ID_panel_name <- paste(ID5[[1]][1])
  ID_panel_name <- gsub("_", " ", ID_panel_name)
  ID_panel_id <- paste(ID5[[1]][2])
  print(ID_panel_name)
  
  t <- read.table(x, header=TRUE)
  df_production <- data.frame(t)
  df_production$Month <- as.Date(df_production$Month)
  threshold_percentage <- df_production[1,10]*.25
  threshold_numerical <- 4
  y_max <- (df_production$Cumulative_Changed_DiaGenes[30]*1.1) + 15
  
  ggplot(data=df_production, aes(x=Month-15, y=DiaGenes_Gained.Cumulative.)) + 
    geom_line(color = "#00843D", size=0.5) + geom_point(color = "#00843D", size=0.75)  + 
    theme_light(base_size = 4) + 
    geom_hline(yintercept=threshold_percentage, linetype="dashed",color = "#628395", size=0.4, alpha = 0.75) + 
    geom_hline(yintercept=threshold_numerical,color = "#dbad6a", size=0.4, alpha = 0.75) + ylab("No. Gained Genes") + 
    xlab("Time (Months)") + 
    annotate("label", y = df_production$DiaGenes_Gained.Cumulative.[1]-7, x = as.Date("2020-07-31"), label=paste(" Panel:",ID_panel_name, " (",ID_panel_id,")\n","Panel Type: ","Specific rare-disease panel \n","Diagnostic Genes in Initial Release:",df_production$No.DiaGenes[1], sep=" "), hjust = 0, size=2) + ylim(-10,y_max)
  
  ggsave(filename=paste("Cumulative-Reclassification-Plot_",ID_panel_name,".png",sep=""), plot= last_plot(), path="~/Downloads/2023-03-31_SPECIFIC/", width = 90, height = 60, units = "mm", dpi = 500)
  
})

#BROAD
lapply(files, function(x) {
  #Extract Panel Name and Panel ID
  
  ID0 <- strsplit(x, split = "/")     
  ID1<-ID0[[1]][10]                       #First part of the file name (not the location)
  ID2 <- strsplit(ID1, split = "_AU_")    
  ID3 <- ID2[[1]][1]
  ID4 <- strsplit(ID3, split = ')', fixed=TRUE)
  ID5 <- strsplit(ID4[[1]][1], split = '(', fixed=TRUE)  
  ID_panel_name <- paste(ID5[[1]][1])
  ID_panel_name <- gsub("_", " ", ID_panel_name)
  ID_panel_id <- paste(ID5[[1]][2])
  print(ID_panel_name)
  
  t <- read.table(x, header=TRUE)
  df_production <- data.frame(t)
  df_production$Month <- as.Date(df_production$Month)
  threshold_percentage <- df_production[1,10]*.449
  threshold_numerical <- 27
  y_max <- (df_production$Cumulative_Changed_DiaGenes[30]*1.1) + 15
  
  ggplot(data=df_production, aes(x=Month-15, y=DiaGenes_Gained.Cumulative.)) + 
    geom_line(color = "#00843D", size=0.5) + geom_point(color = "#00843D", size=0.75)  + 
    theme_light(base_size = 4) + 
    geom_hline(yintercept=threshold_percentage, linetype="dashed",color = "#628395", size=0.4, alpha = 0.75) + 
    geom_hline(yintercept=threshold_numerical,color = "#dbad6a", size=0.4, alpha = 0.75) + ylab("No. Gained Genes") + 
    xlab("Time (Months)") + 
    annotate("label", y = df_production$DiaGenes_Gained.Cumulative.[1]-7, x = as.Date("2020-07-31"), label=paste(" Panel:",ID_panel_name, " (",ID_panel_id,")\n","Panel Type: ","Broad rare-disease panel \n","Diagnostic Genes in Initial Release:",df_production$No.DiaGenes[1], sep=" "), hjust = 0, size=2) + ylim(-10,y_max)
  
  ggsave(filename=paste("Cumulative-Reclassification-Plot_",ID_panel_name,".png",sep=""), plot= last_plot(), path="~/Downloads/2023-03-31-BROAD/", width = 90, height = 60, units = "mm", dpi = 500)
  
})

######
# VERSION SPECIFIC
####

#Define the individual panel
individual_panel <- "24"
print(individual_panel)

lapply(files, function(x) {
  #Extract Panel Name and Panel ID
  
  ID0 <- strsplit(x, split = "/")     
  ID1<-ID0[[1]][10]                       #First part of the file name (not the location)
  ID2 <- strsplit(ID1, split = "_AU_")    
  ID3 <- ID2[[1]][1]
  ID4 <- strsplit(ID3, split = ')', fixed=TRUE)
  ID5 <- strsplit(ID4[[1]][1], split = '(', fixed=TRUE)  
  ID_panel_name <- paste(ID5[[1]][1])
  ID_panel_name <- gsub("_", " ", ID_panel_name)
  ID_panel_id <- paste(ID5[[1]][2])
  print(ID_panel_name)
  
  if(ID_panel_id == individual_panel){
  
  t <- read.table(x, header=TRUE)
  df_production <- data.frame(t)
  df_production$Month <- as.Date(df_production$Month)
  threshold_percentage <- df_production[1,10]*.449
  threshold_numerical <- 27
  y_max <- (df_production$Cumulative_Changed_DiaGenes[30]*1.1) + 15
  
  ggplot(data=df_production, aes(x=Month-15, y=DiaGenes_Gained.Cumulative.)) + 
    geom_line(color = "#00843D", size=0.5) + 
    geom_point(color = "#00843D", size=0.75)  + 
    theme_light(base_size = 4) + 
    geom_hline(yintercept=threshold_percentage, linetype="dashed",color = "#628395", size=0.4, alpha = 0.75) + 
    geom_hline(yintercept=threshold_numerical,color = "#dbad6a", size=0.4, alpha = 0.75) + ylab("No. Gained Genes") + 
    xlab("Time (Months)") + 
    annotate("label", y = 250, x = as.Date("2020-03-31"), label=paste(" Panel:",ID_panel_name, " (",ID_panel_id,")\n","Panel Type: ","Broad rare-disease panel \n","Diagnostic Genes in Initial Release:",df_production$No.DiaGenes[1], sep=" "), hjust = 0, size=2) + ylim(0,y_max)
  
  ggsave(filename=paste("Cumulative-Reclassification-Plot_",ID_panel_name,".png",sep=""), plot= last_plot(), path="~/Downloads/2023-03-31-BROAD/", width = 90, height = 60, units = "mm", dpi = 500)
  } 
})

