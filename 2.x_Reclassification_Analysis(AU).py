##############################
#
# Examine how
#
##############################

import os
import re
import pandas as pd
import time

engine='python'
period ="Period"
release = "Last-Release(Date)"

var_list = ["No.Releases", "No.Genes", "New.Genes", "Lost.Genes", "No.DG-Genes", "New.DG-Genes", "Upgraded.Genes", "Lost.DG-Genes", "Downgraded.DG-Genes"]

for var in var_list:
    root_dir = '/Users/alanr/Desktop/PanelApp_Data/GIT_TEST/_Reclassifications'
    input_dir = root_dir
    out_dir = '/Users/alanr/Desktop/PanelApp_Data/GIT_TEST/_Reclassification_Matrix'
    out_name = 'June-2022_%s_AU.txt' % (var)
    out_name_T = 'June-2022_%s_AU(transposed).txt' % (var)
    outer = '%s/%s' % (out_dir, out_name)
    outer_T = '%s/%s' % (out_dir, out_name_T)

    li = []

    for directory, subdirectories, files in os.walk(root_dir):
        for file in files:                                                          #for each file in the directory
            if file.endswith('.txt'):
                condition_raw = re.split(r'_Summary', file)                         #extract the name of the condition from the title of the file name
                condition_raw1 = re.split(r'\)-AU', condition_raw[0])
                condition_raw2 = re.split(r'\(', condition_raw1[0])
                condition = condition_raw2[0]
                ID = condition_raw2[1]
                identifer = "%s(%s)" % (condition, ID)
                identifer = str(identifer)
                #print(identifer, var)
                #time.sleep(5)

                file0 = "%s/%s" % (input_dir, file)                                 #open each file
                file1 = open(file0, "r")

                df = pd.read_csv(file0, index_col='Period', header=0, sep='\t')     #read file into df
                c = '%s - %s' % (identifer, var)                                    #add information to df
                print(c)
                df.rename(columns={var: c}, inplace=True)
                li.append(df[c])

            df = pd.concat(li, axis=1, ignore_index=False)
            df.to_csv(outer, index=True, sep="\t", na_rep="n/a", float_format='%.0f')
            df1=df.transpose() #transpose
            df1.to_csv(outer_T, index=True, sep="\t", na_rep="n/a", float_format='%.0f')