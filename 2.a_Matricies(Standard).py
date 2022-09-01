##############################
#
# Condense every version of a panel into a monthly breakdown
#
##############################

#This script has been written to combine ALL the different condensed panels into a single matrix

#Alan Robertson
#2022-01-31

#2022-06-01
#Updated to include to automatically produce all matrix files

#2022-07-1
#Updated to support diagnostic grade genes

import os
import re
import time

import pandas as pd

engine='python'
period ="Period"
release = "Last-Release(Date)"


var_list = ["No.Ent","No.DiaEnt","No.Genes","No.DiaGenes","No.Repeats","No.DiaRepeats","No.CNVs","No.DiaCNVs", "Releases"]

for var in var_list:
    root_dir = '/Users/alanr/Desktop/PanelApp_Data/GIT_TEST/_Monthly_Summaries'
    input_dir = root_dir
    out_dir = '/Users/alanr/Desktop/PanelApp_Data/GIT_TEST/_Matrices'
    out_name = 'June-2022_%s_AU.txt' % (var)
    out_name_T = 'June-2022_%s_AU(transposed).txt' % (var)
    outer = '%s/%s' % (out_dir, out_name)
    outer_T = '%s/%s' % (out_dir, out_name_T)

################
# For each file
# Open each file and extract the condition name, and ID
###############

    li = []

    for directory, subdirectories, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.txt'):
                condition_raw = re.split(r'-Monthly_Summary', file)
                condition_raw1 = re.split(r'AU_', condition_raw[0])
                condition_raw2 = re.split(r'\(', condition_raw1[1])
                condition = condition_raw2[0]
                condition_raw3 = re.split(r'\)', condition_raw2[1])
                ID = condition_raw3[0]
                identifer = "%s(%s)" % (condition, ID)
                identifer = str(identifer)
                print(identifer)

                file0 = "%s/%s" % (input_dir, file)
                file1 = open(file0, "r")
                #print(var, "opening:", identifer,"\n", file0,"\n")
                #time.sleep(.1)

                df = pd.read_csv(file0, index_col='Period', header=0, sep='\t', skipfooter=1)
                c = '%s - %s' % (identifer, var)
                df.rename(columns={var: c}, inplace=True)
                li.append(df[c])

            df = pd.concat(li, axis=1, ignore_index=False)
            df.to_csv(outer, index=True, sep="\t", na_rep="n/a", float_format='%.0f')
            df1=df.transpose() #transpose
            df1.to_csv(outer_T, index=True, sep="\t", na_rep="n/a", float_format='%.0f')
    #time.sleep(10)



    print(var)