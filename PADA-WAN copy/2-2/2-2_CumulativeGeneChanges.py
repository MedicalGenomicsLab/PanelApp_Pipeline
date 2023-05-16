##################################################
#
# DETERMINE CUMULATIVE CHANGES 
#
# i.e. how much change has occured between two time points
# or, how would we actually graph everything? 
#
##################################################

#This script has been designed to characterise the cumulative changes each month for a panel 

# Alan Robertson - Feburary 2022

# Version 0.1
# 2023-05-05 - PRODUCTIONISE
# I'M SORRY FOR THE HACKY DATE SOLUTION

###############################################

import os
import re
import time
import argparse
import pandas as pd

###############################################

#Define main function
def main(file_path: str):
	parameters_df = pd.read_csv(file_path,sep="\t")
	temp_name = parameters_df.iloc[0,1]
	temp_version = parameters_df.iloc[1,1]
	temp_indir = parameters_df.iloc[2,1]
	temp_outdir = parameters_df.iloc[3,1]
	return(temp_name, temp_version, temp_indir, temp_outdir)

#Excute the code to actually import the params file and extract the key values
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--file-path", type=str, required=True, help="Path to parameter file")

	args, unknowns = parser.parse_known_args()
	file_path = args.file_path

	main(file_path=file_path,)
	the_returned = main(file_path)
	name_exp = the_returned[0]
	source = the_returned[1]
	source_x = "-%s" % (source)
	input_dir = the_returned[2]
	out_dir = the_returned[3]

###################################################
# From a list of panels, focus on a singular panel, extract source, name and ID
###################################################

for directory, subdirectories, files in os.walk(input_dir):
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
			condition_raw1 = re.split(source_x, condition_raw[0])
			condition_raw2 = re.split(r'\(', condition_raw1[0])
			condition = condition_raw2[0]   #Condition Name

			condition_raw3 = re.split(r'\)', condition_raw2[1])
			ID = condition_raw3[0]          #Condition Raw
			identifer = "%s(%s)" % (condition, ID)
			identifer = str(identifer)
			print(identifer)

			out_name = '%s_%s_Cumulative_Changes.txt' % (identifer, source)
			outer = '%s/%s' % (out_dir, out_name)
			outer_file = open(outer, "a+")

			print("PANEL:",identifer,"\nMonth","Releases", "Cumulative_Releases(AfterIntitalReleaseWindow)","No.Genes","Genes_Added(Month)","Genes_Removed(Month)","Genes_Added(Cumulative)","Genes_Removed(Cumulative)","Cumulative_Changed_Genes","No.DiaGenes", "DiaGenes_Added(Month)", "DiaGenes_Upgraded(Month)" ,"DiaGenes_Removed(Month)", "DiaGenes_Downgraded(Month)", "DiaGene.Gains(Cumulative)", "DiaGene.Losses(Cumulative)", "DiaGene.Changes(Cumulative)", sep="\t", file=outer_file)

			file0 = "%s/%s" % (input_dir, file)
			file1 = open(file0, "r")

			for line in file1:
				line2 = re.split(r'\t', line)
				if line2[0] == 'PANEL:':
					continue	
				if line2[0] == 'Period':
					continue
				month = line2[0]

				################
				#HACKY NON-SENSE
				################

				#if month == "2018-01":
					#month = "2018-01-31"
				#if month == "2018-02":
					#month = "2018-02-28"
				#if month == "2018-03":
					#month = "2018-03-31"
				if month == "2018-04":
					month = "2018-04-30"
				if month == "2018-05":
					month = "2018-05-31"
				if month == "2018-06":
					month = "2018-06-30"
				if month == "2018-07":
					month = "2018-07-31"
				if month == "2018-08":
					month = "2018-08-31"
				if month == "2018-09":
					month = "2018-09-30"
				if month == "2018-10":
					month = "2018-10-31"
				if month == "2018-11":
					month = "2018-11-30"
				if month == "2018-12":
					month = "2018-12-31"

				if month == "2019-01":
					month = "2019-01-31"
				if month == "2019-02":
					month = "2019-02-28"
				if month == "2019-03":
					month = "2019-03-31"
				if month == "2019-04":
					month = "2019-04-30"
				if month == "2019-05":
					month = "2019-05-31"
				if month == "2019-06":
					month = "2019-06-30"
				if month == "2019-07":
					month = "2019-07-31"
				if month == "2019-08":
					month = "2019-08-31"
				if month == "2019-09":
					month = "2019-09-30"
				if month == "2019-10":
					month = "2019-10-31"
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
				if month == "2022-06":
					month = "2022-06-30"
				if month == "2022-07":
					month = "2022-07-31"
				if month == "2022-08":
					month = "2022-08-31"
				if month == "2022-09":
					month = "2022-09-30"
				if month == "2022-10":
					month = "2022-10-31"
				if month == "2022-11":
					month = "2022-11-30"
				if month == "2022-12":
					month = "2022-12-31"

				if month == "2023-01":
					month = "2023-01-31"
				if month == "2023-02":
					month = "2023-02-28"
				if month == "2023-03":
					month = "2023-03-31"
				if month == "2023-04":
					 month = "2023-04-30"
				#if month == "2023-05":
					#month = "2023-05-31"
				#if month == "2023-06":
					#month = "2023-06-30"
				#if month == "2023-07":
					#month = "2023-07-31"
				#if month == "2023-08":
					#month = "2023-08-31"
				#if month == "2023-09":
					#month = "2023-09-30"
				#if month == "2023-10":
					#month = "2023-10-31"
				#if month == "2023-11":
					#month = "2023-11-30"
				#if month == "2023-12":
					#month = "2023-12-31"	

############################

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

				print(month, releases, cum_releases, no_tges, tges_added, tges_removed, cum_tges_added, cum_tges_removed, cum_total_tge, no_dgges, dgges_added, dgges_upgraded, dgges_removed, dgges_downgraded, cum_dgges_added, cum_dgges_removed, cum_total_dgge, sep="\t", file=outer_file)
				counter = counter + 1
				time.sleep(0.25)
