##############################
#
# Download Panels IDS - PanelApp AU
#
##############################

#Introduction
#This script was written to download a list of panel IDS from PanelApp AU
#This information is required to download the genes associate with panel in Panel App AUSTRALIA

#This script has been copied from Download_IDs-UK, but adjusted to PanelApp-Au

#Alan Robertson
#2021-12-02

#2022-02-01
#Updated to include superpanel status

#2022-06-01
#Updated to include rare disease status

import re
import requests
from datetime import datetime

now = datetime.now()
now = now.strftime("%Y-%m-%d_%H-%M")

#Download from multiple pages
count = 1
count_str = str(count)
partial_path = 'https://panelapp.agha.umccr.org/api/v1/panels/?page='
path = partial_path + count_str

rerun = "true"

#Connect to the PanelApp-AU API
headers = {
    'accept': 'application/json',
    'X-CSRFToken': 'PSgeKIwkDKU2Kt9LVAeDEFoLz2FE8UpKeACrS4uUi6rri8shbemDNv1oWHzD4bp0',
}
aDict={}

#Setup output file
filename = "/Users/alanr/Desktop/PanelApp_Data/IDs/%s_PA-AU_Panel_IDs.tsv" %(now)
f = open(filename, "w")
f.write("Panel\tID\tVersion\tRelease-Date\tNo.Genes\tNo.STRs\tNo.Regions\tSuperPanel-Status\tSource\tDisease-Group\tPanelType\n")

#The solution to getting IDs from different pages of PA (i.e. if you want more than the first 100 panels)

while rerun == 'true':
    response = requests.get(path, headers=headers)
    check = response
    check_str = str(check)
    print('Panel App Page Number:', count,)
    data = response.json()
    for line in data['results']:
        b = "Panel"
        a = line['types']
        c = "Misc."
        for a1 in a:                            #for each list inside types
            a11 = a1['description']
            if re.search(r'uper', a11):
                b = "Super Panel"

            if re.search(r'uper',line['name']):
                b = "Super Panel"

            a22 = a1['slug']
            if re.search(r'rare', a22):
                c = "Rare Disease"

        print(line['name'], line["id"], line["version"], line["version_created"], line['stats']["number_of_genes"],
              line['stats']["number_of_strs"], line['stats']["number_of_regions"], b, "AU", line["disease_group"], c,
              sep="\t", file=f)

    count = count + 1
    count_str = str(count)
    path = partial_path + count_str
    response2 = requests.get(path, headers=headers)
    check_data = str(response2)
    print("Check:", check_data)
    if check_data != "<Response [200]>":
        rerun = "false"
        print('More Pages =',rerun)
    else:
        print('More Pages =',rerun)