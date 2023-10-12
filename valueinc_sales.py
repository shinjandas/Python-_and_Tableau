# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:28:13 2023

@author: Shinjan
"""
import pandas as pd

data=pd.read_csv('transaction2.csv')

data=pd.read_csv('transaction2.csv', sep=';')
#summary of the data
data.info()

#Defining Variables

CostPerItem=11.73
SellingPricePerItem=21.11
NumberofItemsPurchased=6

#Mathematical Operations on Tableau

ProfitPerItem=21.11-11.73
ProfitPerItem=SellingPricePerItem-CostPerItem

ProfitperTransaction= NumberofItemsPurchased * ProfitPerItem
CostPerTransaction= NumberofItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberofItemsPurchased + SellingPricePerItem

#CostPerTransaction= CostPerItem * NumberofItemsPurchases
#variable = dataframe[' column_name']

CostPerItem=data['CostPerItem']
NumberofItemPurchased=data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

#adding new column to the dataframe

data['CostPerTransaction']=CostPerTransaction

#Sales per Transaction

data['SalesPerTransaction']= data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Per Transaction= Sales-Cost

data['ProfitPerTransaction']=data['SalesPerTransaction'] - data['CostPerTransaction']

#markup=(Sales-cost)/Cost= profitpertransaction/costpertransactions

data['Markup']=(data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

#Rounding off marking

roundmarkup=round(data['Markup'],2)
#or
data['Markup']=round(data['Markup'],2)

#checking column data data-types
#print(data('Day').dtype)

#change column type

day=data['Day'].astype(str)
year= data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

#combining data fields of date, month and year to one column

my_date=day+ '-' + data['Month']+ '-' +year
data['Date']=my_date

#use iloc to specify rows/columns

data.iloc[0] #views row with index 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:0]# last 5 rows

data.head(5) #brings in first 5 rows
data.iloc[:,2]#brings in all rows on the 2nd col

data.iloc[4,2]#brings in 4 rows on the 2nd col

#using split to split the client_keywords field
#syntax: new_var=column_name.str.split('sep', expand=True)

split_col=data['ClientKeywords'].str.split(',', expand=True)

#creating new columns for split in CLient Keywords
data['ClientAge']=split_col[0]
data['ClientType']=split_col[1]
data['LengthofContract']=split_col[2]

#using the replace function

data['ClientAge']=data['ClientAge'].str.replace('[','')
data['ClientType']=data['ClientType'].str.replace(']','')

#using the lower function to change item to lowercase

data['ItemDescription']=data['ItemDescription'].str.lower()

#bringing in a new dataset

seasons= pd.read_csv("value_inc_seasons.csv",sep=';')

#how to merge files
#merging files: merge_df= pd.merge(df_old, df_new, on='key')

data=pd.merge(data,seasons, on='Month')

#delete/remove/drop columns
# dataframe= dataframe.drop('columnname',axis=1)

data=data.drop('ClientKeywords', axis=1)
data=data.drop('Day',axis=1)
data=data.drop(['Year', 'Month'], axis=1)

#export into a csv
#False here used to exclude index in the csv file, to include it, write True
data.to_csv('ValueInc_Cleaned.csv', index=False)