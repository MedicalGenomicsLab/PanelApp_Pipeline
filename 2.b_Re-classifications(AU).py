#####################################
# FIVE - RECLASSIFCATION / DATA FRAME TEST
#####################################

# 1. Open ID file - for each panel in the id file
# 2. Open the panel's monthly breakdown - open the corresponding specific version of the panel
# 3. Ingest each version into a data frame (ID and gel status)
# 4. Append each version's df to the main data frame
# 5. print the results from the reclassification test

#######################################

import re
import datetime
import time
import numpy as np
import pandas as pd

start_date = datetime.date(2019, 11, 1)
end_date = datetime.date(2022, 6, 1)

###################################################
# Set up key variables
###################################################

###################################################
# From a list of panels, focus on a singular panel, extract source, name and ID
###################################################

file_ID = open("/Users/alanr/Desktop/PanelApp_Data/IDs/2022-08-31_10-06_PA-AU_Panel_IDs.tsv", "r")

for line in file_ID:
    line1 = re.split(r'\t', line)                  #for each line, seperate by tab

    panel_name = line1[0]
    if panel_name == 'Panel':
        continue

    panel_name=panel_name.strip()
    panel_name = panel_name.replace(' ', '_')
    panel_id = line1[1]
    source = line1[8]
    source = source.strip()

##################################################
# For each panel, create the output files
###################################################
    parent_location1 = "/Users/alanr/Desktop/PanelApp_Data/GIT_TEST/_Reclassifications/"
    parent_location2 = "%s_%s_%s-Panel_GeneLevel_Matrix" % (source, panel_id, panel_name)

    reclassification_summary = "%s/%s(%s)-%s_Reclassifcation_Summary.txt" % (parent_location1, panel_name, panel_id, source)
    reclassification_file = open(reclassification_summary, "a+")
    head_summary = "Period\tVersion\tNo.Releases\tNo.Genes\tNew.Genes\tLost.Genes\tNo.DG-Genes\tNew.DG-Genes\tUpgraded.Genes\tLost.DG-Genes\tDowngraded.DG-Genes"
    #print(head_summary)
    print(head_summary, file=reclassification_file)

##################################################
# Set up panel specific variables
#################################################
    master_df = pd.DataFrame(columns=['Genes'])

###################################################
# For each panel, open the monthly summary file
###################################################

    monthly_breakdown = "%s_%s(%s)-Monthly_Summary" %(source, panel_name, panel_id)
    monthly_breakdown_loc = "/Users/alanr/Desktop/PanelApp_Data/GIT_TEST/_Monthly_Summaries"
    monthly_path = ("%s/%s.txt") % (monthly_breakdown_loc, monthly_breakdown)

    file_monthlybreakdown = open(monthly_path, "r")
    for line_mbd in file_monthlybreakdown:
        line2 = re.split(r'\t', line_mbd)
        if line2[0] == 'Period':
            continue
        if "NOTE" in line2[0]:
            continue
        if "N/A" in line2[1]:
            new_panel_check = 1
            last_total_tge = 0
            last_total_dgge = 0
            continue
        # if "2019-11-30" in line2[0]:
        #     new_panel_check = 1

        # total_tge = line2[3]
        # total_dgge = line2[4]
        new_panel_check = 0
        timepoint_date0 = line2[0]
        timepoint_line = re.split(r'-', timepoint_date0)
        timepoint_year = int(timepoint_line[0])
        timepoint_month = int(timepoint_line[1])
        timepoint_month1 = ("{:02d}".format(timepoint_month))
        timepoint_month2 = int(timepoint_month1)
        timepoint_day = int(timepoint_line[2])
        time_stamp = datetime.date(timepoint_year, timepoint_month, timepoint_day)
        time_stamp2 = "%s_%s_%s" % (timepoint_year, timepoint_month1, timepoint_day)
        time_stamp3 = "%s-%s" %(timepoint_year, timepoint_month1)
        this_month = time_stamp3
        last_month0 = timepoint_month2 - 1
        last_month0 = ("{:02d}".format(last_month0))
        if timepoint_month2 == 1:
            last_month0 = 12
            last_year = int(timepoint_year)-1
            last_month = "%s-%s" %(last_year, last_month0)
        else:
            last_month = "%s-%s" %(timepoint_year, last_month0)

        monthly_releases = line2[1]

        if time_stamp < start_date:
            continue

        version = line2[2]
        line22 = re.split(r'\(', version)
        version_processed = line22[0]

        if 'N/A' in version_processed:
            continue

        print("Opening", panel_name, "\t", time_stamp3, "\t", version_processed)

###################################################
# Read file into data frame
###################################################

        individual_panel_location = "/Users/alanr/Desktop/PanelApp_Data/GIT_TEST/%s_%s_%s" % ( source, panel_id, panel_name)
        each_version_file = "%s_v%s(%s)_Annotated_PA-%s.tsv" % (panel_name, version_processed, panel_id, source)
        version_specific_path = "%s/%s" % (individual_panel_location, each_version_file)
        file_specific_version = open(version_specific_path, "r")
        df_this_month = pd.DataFrame(columns=['Genes'])

        for gene_line in file_specific_version:
            line3 = re.split(r'\t', gene_line)
            g_symbol = line3[0]
            g_status = line3[1]
            ensg_id_0 = line3[4]
            ensg_id = "%s-%s-%s" % (g_symbol, ensg_id_0, g_status)
            #ensg_id = line3[4]
            version_checker = line3[6]
            dge_status = line3[5]

            if 'GEL-Status' in line3[5]:
                continue
            if g_status != 'gene':
                continue

            if dge_status != "":
                if ensg_id in df_this_month.values:
                    print("", end="")
                else:
                    DGE = int(dge_status)
                    df_temp = {'Genes': ensg_id, time_stamp3: DGE}
                    df_this_month = df_this_month.append(df_temp, ignore_index=True)

        master_df = pd.merge(master_df, df_this_month, on='Genes', how='outer')


        ##########################################
        #mystery
        # investigate = "%s/%s(%s)_Reclassifcation_Summary.txt" % (
        # parent_location1, panel_name, version_processed)
        # investigate_file = open(investigate, "a+")
        # print(master_df.to_string(), file=investigate_file)
        # time.sleep(10)

###################################################
# Compare this month to last month
###################################################


        add_count = 0
        dgge_add_count = 0
        same_count = 0
        up_count = 0
        dgge_up_count = 0
        down_count = 0
        dgge_down_count = 0
        remove_count = 0
        dgge_remove_count = 0

        for index, row in master_df.iterrows():
            y = row[this_month]
            # if this_month == "2019-11":
            if last_month not in master_df:
                add_count = add_count + 1
                if y >= 3:
                    dgge_add_count = dgge_add_count + 1
                same_count = 0
                up_count = 0
                down_count = 0
                remove_count = 0
                continue

            x = row[last_month]
            z = row['Genes']

            if np.isnan(x) == True and np.isnan(y) == True:
                continue
            if np.isnan(x) == True and y >= 0:
                add_count = add_count + 1
                if y == 3:
                    dgge_add_count = dgge_add_count + 1
            if np.isnan(y) == True and x >= 0:
                remove_count = remove_count + 1
                if x == 3:
                    dgge_remove_count = dgge_remove_count + 1
            if x == y:
                same_count = same_count + 1
            if y > x:
                up_count = up_count + 1
                if y == 3:
                    dgge_up_count = dgge_up_count + 1
            if y < x:
                down_count = down_count + 1
                if x == 3:
                    dgge_down_count = dgge_down_count + 1


        total_tge = last_total_tge + add_count - remove_count
        total_dgge = last_total_dgge + (dgge_add_count + dgge_up_count) - (dgge_remove_count + dgge_down_count)
        print(this_month, version_processed, monthly_releases, total_tge, add_count, remove_count,
        total_dgge, dgge_add_count, dgge_up_count, dgge_remove_count, dgge_down_count, sep="\t", file=reclassification_file)
        last_total_tge = total_tge
        last_total_dgge = total_dgge

###################################################
# For each panel
###################################################
    this_month = "2019-11"
    last_month = "2019-10"
    time.sleep(1)