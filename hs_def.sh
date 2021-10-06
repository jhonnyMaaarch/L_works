#!/bin/bash
######################################################
####Module will define node objects and parameters####
# Developed by: Sunny Adeola                      ####
# Date:         05/01/2020                        ####
# Contact:      osadeola@us.ibm.com               ####
######################################################
# Get node name
read -p "Enter Node name (e.g hs22n71): " Node_name

# get management module
read -p "Enter Management Module (e.g c37bc2mm1): " managt_mod
rscan $managt_mod -z > $Node_name

vi $Node_name

cat $Node_name | mkdef -z
makegocons $Node_name

lsdef $Node_name
