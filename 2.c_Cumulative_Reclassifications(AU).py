#####################################
# FIVE D - Cumulative re-classifiacation events
#####################################

# Re-write to focus on genes

#######################################


import os
import re
import time

import pandas as pd

######################################

root_dir = '/Users/alanr/Desktop/PanelApp_Data/GIT_TEST/_Reclassifications'
input_dir = root_dir
out_dir = '/Users/alanr/Desktop/PanelApp_Data/GIT_TEST/_CumulativeReclassifications'

###################################################
# For each panel level summary file
###################################################

for directory, subdirectories, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.txt'):

            net_genes = 0
            last_month_net_genes = 0
            total_tges = 0
            last_month_total_tges = 0
            monthly_tges_added = 0
            monthly_tges_removed = 0
            cum_tges_added = 0
            cum_tges_removed = 0
            cum_total_tge = 0
            cum_dgges_added = 0
            cum_dgges_removed = 0
            cum_dgges_up = 0
            cum_dgges_down = 0
            cum_total_dgge = 0
            cum_releases = 0

            counter = 0

            condition_raw = re.split(r'-Summary', file)
            condition_raw1 = re.split(r'-AU', condition_raw[0])
            condition_raw2 = re.split(r'\(', condition_raw1[0])
            condition = condition_raw2[0]   #Condition Name
            #print(condition)
            condition_raw3 = re.split(r'\)', condition_raw2[1])
            ID = condition_raw3[0]          #Condition Raw
            identifer = "%s(%s)" % (condition, ID)
            identifer = str(identifer)
            print(identifer)

            out_name = '%s_AU_Cumulative_Reclassification.txt' % (identifer)
            outer = '%s/%s' % (out_dir, out_name)
            outer_file = open(outer, "a+")

            print("Month","Releases", "Cumulative_Releases(AfterIntitalReleaseWindow)",
                  "No.Genes","Genes_Added(Month)","Genes_Removed(Month)","Genes_Added(Cumulative)","Genes_Removed(Cumulative)","Cumulative_Changed_Genes",
                  "No.DiaGenes", "DiaGenes_Added(Month)", "DiaGenes_Upgraded(Month)" ,"DiaGenes_Removed(Month)", "DiaGenes_Downgraded(Month)", "DiaGenes_Gained(Cumulative)", "DiaGenes_Lost(Cumulative)", "Cumulative_Changed_DiaGenes",
                  sep="\t", file=outer_file)

            file0 = "%s/%s" % (input_dir, file)
            file1 = open(file0, "r")

            for line in file1:
                line2 = re.split(r'\t', line)
                if line2[0] == 'Period':
                    continue
                month = line2[0]

                if month == "2019-11":
                    month = "2019-11-30"
                if month == "2019-12":
                    month = "2019-12-31"

                if month == "2020-01":
                    month = "2020-01-31"
                if month == "2020-02":
                    month = "2020-02-29"
                if month == "2020-03":
                    month = "2020-03-31"
                if month == "2020-04":
                    month = "2020-04-30"
                if month == "2020-05":
                    month = "2020-05-31"
                if month == "2020-06":
                    month = "2020-06-30"
                if month == "2020-07":
                    month = "2020-07-31"
                if month == "2020-08":
                    month = "2020-08-31"
                if month == "2020-09":
                    month = "2020-09-30"
                if month == "2020-10":
                    month = "2020-10-31"
                if month == "2020-11":
                    month = "2020-11-30"
                if month == "2020-12":
                    month = "2020-12-31"

                if month == "2021-01":
                    month = "2021-01-31"
                if month == "2021-02":
                    month = "2021-02-28"
                if month == "2021-03":
                    month = "2021-03-31"
                if month == "2021-04":
                    month = "2021-04-30"
                if month == "2021-05":
                    month = "2021-05-31"
                if month == "2021-06":
                    month = "2021-06-30"
                if month == "2021-07":
                    month = "2021-07-31"
                if month == "2021-08":
                    month = "2021-08-31"
                if month == "2021-09":
                    month = "2021-09-30"
                if month == "2021-10":
                    month = "2021-10-31"
                if month == "2021-11":
                    month = "2021-11-30"
                if month == "2021-12":
                    month = "2021-12-31"

                if month == "2022-01":
                    month = "2022-01-31"
                if month == "2022-02":
                    month = "2022-02-28"
                if month == "2022-03":
                    month = "2022-03-31"
                if month == "2022-04":
                    month = "2022-04-30"
                if month == "2022-05":
                    month = "2022-05-31"

            ########

                version = line2[1]
                releases = int(line2[2])
                no_tges = int(line2[3])
                tges_added = int(line2[4])
                tges_removed = int(line2[5])
                no_dgges = int(line2[6])
                dgges_added = int(line2[7])
                dgges_removed = int(line2[9])
                dgges_upgraded = int(line2[8])
                dgges_downgraded = int(line2[10])

                #
                if counter == 0:
                    print("", end="")
                else:
                    cum_tges_added = cum_tges_added + tges_added
                    cum_tges_removed = cum_tges_removed + tges_removed
                    cum_total_tge = cum_tges_added + cum_tges_removed
                    cum_dgges_added = dgges_added + dgges_upgraded + cum_dgges_added
                    cum_dgges_removed = dgges_removed + dgges_downgraded + cum_dgges_removed
                    cum_total_dgge = cum_dgges_removed + cum_dgges_added
                    cum_releases = releases + cum_releases

                    # YOU ARE HERE, EXPAND TO INCLUDE DGGES - ADD SAVE FUNCTION
                #
                print(month, releases, cum_releases,
                      no_tges, tges_added, tges_removed, cum_tges_added, cum_tges_removed, cum_total_tge,
                      no_dgges, dgges_added, dgges_upgraded, dgges_removed, dgges_downgraded, cum_dgges_added, cum_dgges_removed, cum_total_dgge,
                      sep="\t", file=outer_file)
                counter = counter + 1
                time.sleep(0.25)