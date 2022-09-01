##############################
#
# Condense every version of a panel into a monthly breakdown
#
##############################

# Introduction
# There are a lot of different versions of panel in PanelApp, like tens of thousands of them
# So in order to find meaning in this sea of data, this script was written to find the last panel released each month , and compare this to the month proceeding

# Alan Robertson
# 2022-01-25

# Update - 2022-03-04
# This script was updated to only support the output from the JSON downloads


# Update - 2022-03-07
# This script has been updated to print the results from this analysis to a defined output folder

# Update - 2022-06-27
# This script has been forked to only count genes, rather than genes, STRs and CNVs

import os
import re
import datetime
import time
from datetime import date
from dateutil.relativedelta import relativedelta

root_dir = '/Users/alanr/Desktop/PanelApp_Data/GIT_TEST'
out_dir = '/Users/alanr/Desktop/PanelApp_Data/GIT_TEST/_Monthly_Summaries'
input_dir = root_dir

id_date = datetime.date(2022,7,18)
download_start = datetime.date(2022,7,18)
download_end = datetime.date(2022,7,18)

################
# For each file
# Open each file and extract the condition name, and ID
###############

for directory, subdirectories, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.txt'):
            if file.startswith('AU'):
                condition_raw = re.split(r'Total_Summary', file)
                condition_raw1 = re.split(r'AU_', condition_raw[0])
                condition_raw2 = re.split(r'\(', condition_raw1[1])
                condition = condition_raw2[0]
                condition_raw3 = re.split(r'\)', condition_raw2[1])
                ID = condition_raw3[0]
                print(condition,ID)

################
# Condense for the end of each month
# While still in each file
###############

                start_date = datetime.date(2019, 10, 1)
                current_date = start_date
                #end_date = datetime.date(2022, 6, 1)            #update to current month
                end_date0 = date.today()
                end_date = end_date0 + relativedelta(months=0)
                last_date = datetime.date(2019, 10, 31)  # start date minus one month
                y_delta = datetime.timedelta(days=1)

                carry_over = "N/A"
                hold_over = "N/A\tN/A(N/A)\tN/A\tN/A\tN/A\tN/A\tN/A\tN/A\tN/A\tN/A"
                counter = 1
                output_dict = {}
    #
    # ###############
    # # Actually open the file
    # ###############

                while current_date <= end_date:
                    this_month = current_date - y_delta
                    file0 = "%s/%s" % (input_dir,file)
                    file1 = open(file0, "r")
    #
                    for line in file1:
                        line1 = re.split(r'\t+', line)  # for each line, seperate by tab
                        version_id_str0 = str(line1[0])
                        if version_id_str0 == "PanelName(PanelID)":
                            continue
                        #version_id_str = str(re.split('\(', version_id_str0)[0])
                        version_id_str = str(line1[3])
                        raw_timestamp = line1[2]
                        test_inter = re.split(' ', raw_timestamp)
                        version_dateraw = test_inter[1]
                        version_year = int(re.split("-", version_dateraw)[0])
                        version_month = int(re.split("-", version_dateraw)[1])
                        version_day = int(re.split("-", version_dateraw)[2])
                        version_date = datetime.date(version_year, version_month, version_day)
                        version_time = test_inter[1]

                        gene_count = line1[6]
                        diagene_count = line1[7]
                        str_count = line1[8]
                        diastr_count = line1[9]
                        region_count = line1[10]
                        diaregion_count = line1[11]
                        diaregion_count = diaregion_count.replace('\n', '')

                        if last_date < version_date <= this_month:
                            # print(this_month,"\t",version_date,"\t",counter)
                            output_dict[this_month] = ("%s\t%s(%s)\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s") % (
                            counter, version_id_str, version_date, line1[4], line1[5], gene_count, diagene_count, str_count, diastr_count, region_count, diaregion_count)
                            hold_over = ("0\t%s(%s)\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s") % (
                            version_id_str, version_date, line1[4], line1[5], gene_count, diagene_count, str_count, diastr_count, region_count, diaregion_count)
                            counter = counter + 1
                            # time.sleep(1)

                        if counter == 1:
                            output_dict[this_month] = hold_over

                        # prepare for next cycle

                    current_date = current_date + relativedelta(months=+1)
                    last_date = this_month
                    counter = 1
                    file1.close()


            ##########
            # Part Two
            ##########

            # print the output
            output_file = "%s/AU_%s(%s)-Monthly_Summary.txt" %(out_dir, condition, ID)
            file_001 = open(output_file, "w+")
            head = "Period\tReleases\tLast-Release(Date)\tNo.Ent\tNo.DiaEnt\tNo.Genes\tNo.DiaGenes\tNo.Repeats\tNo.DiaRepeats\tNo.CNVs\tNo.DiaCNVs"
            print(head, file=file_001)
            for k,v in output_dict.items():
                print(k, "\t", v, file=file_001)
                print(k, "\t", v)
            print("NOTE: The summary of information that's described as", last_date, "was determined on", end_date0, "using IDs downloaded on", id_date, " Data was downloaded between", download_start,"and",download_end, file=file_001)