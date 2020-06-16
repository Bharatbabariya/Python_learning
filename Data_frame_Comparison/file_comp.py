# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:00:23 2020

@author: ARTI
"""
# This code will read the data from 2 csv file and compare it.
# it will share give you human readable report as output in one separate file.
import pandas as pd 
import datacompy
from datetime import datetime

source1="F:///Learning/Python_learning/File_comp/2015.csv"
source2="F:///Learning/Python_learning/File_comp/2015_2.csv"

src_df0 = pd.read_csv(source1)
src_df01 = pd.read_csv(source2)

#fieldnames="Country","Region","Happiness Rank","Happiness Score","Standard Error","Economy (GDP per Capita)","Family","Health (Life Expectancy)","Freedom","Trust (Government Corruption)","Generosity","Dystopia Residual"

###########################3Filter the record level data ###############################

src_df00 = src_df0[src_df0['Happiness Rank'] > 1]
src_df001=src_df01[src_df01['Happiness Rank'] > 1]
########################################################################################

# selecting only required column in data frame

l1=[0,1,2]
src_df1 = src_df00.iloc[:,l1]
final_df1 =src_df1.sort_values('Happiness Rank',ascending=True) # apply sorting on column 


src_df2 = src_df001.iloc[:,l1]
final_df2 =src_df2.sort_values('Happiness Rank',ascending=True)



compare = datacompy.Compare(
    final_df1,
    final_df2,
    on_index=True,
#    join_columns=2,  #You can also specify a list of columns
    abs_tol=0, #Optional, defaults to 0
    rel_tol=0, #Optional, defaults to 0
    df1_name='Original', #Optional, defaults to 'df1'
    df2_name='New' #Optional, defaults to 'df2'
    )
compare.matches(ignore_extra_columns=False)
# False

# This method prints out a human-readable report summarizing and sampling differences
#print(compare.report())
filename1 = "File_Comp_Report"+datetime.now().strftime("%Y%m%d_%H%M%S")+".txt"


with open(filename1,'w') as wf:
        wf.write(compare.report())



Final_Df_Bool = (final_df1 != final_df2).stack()  # Create Frame of comparison booleans
print(Final_Df_Bool)
#print(final_df1.stack()[Final_Df_Bool])

Final_Df_diff = pd.concat([final_dack()[Final_Df_Bool]f1.st, final_df2.stack()[Final_Df_Bool]], axis=1)
Final_Df_diff.columns=["Old", "New"]
print(Final_Df_diff)
# 


# =============================================================================
# def dfDiff(oldFrame, newFrame):
# 	dfBool = (oldFrame != newFrame).stack()  
# 	diff = pd.concat([oldFrame.stack()[dfBool],
# 					  newFrame.stack()[dfBool]], axis=1)
# 	diff.columns=["Old", "New"]
# 	return diff
# print(dfDiff(final_df1, final_df2))
# =============================================================================




#print(final_df)
#final_df = df.iloc[:,[0,1,2]]
