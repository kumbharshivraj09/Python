import pandas as pd
import streamlit as slt
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

slt.title("DATA ANALYSIS")
slt.subheader("Data Analysis Using Python & Streamlit")
# upload dataset
upload=slt.file_uploader("UPLOAD YOUR DATA SET IN CSV FORMAT : ")
if upload is not None:
    data=pd.read_csv(upload)

# show dataset
if upload is not None:
 if slt.checkbox('Preview Dataset'):
    if slt.button('Head'):
        slt.write(data.head())
    if slt.button('Tail'):
        slt.write(data.tail())          
        
#check datatype
if upload is not None:
   slt.checkbox("Data Type Of Each Columns ")
   slt.text("DataType")
   slt.write(data.dtypes) 

# find the shape of dataset

if upload is not None:
   data_shape=slt.radio('What Dimention You Want To Check?',('Rows','Column'))   
   if data_shape=="Rows":
      slt.text("NUmber Of Rows : ")
      slt.write(data.shape[0])
   if data_shape=="Column":
      slt.text("NUmber Of Columns : ")
      slt.write(data.shape[1])

#find null values   

if upload is not None: 
   test=data.isnull().values.any()
   if test==True:
      if slt.checkbox("Null Value In Dataset"):
         plt.figure(figsize=(10,5))
         sns.heatmap(data.isnull())
         slt.pyplot(plt)         

#find duplicate values in dataset  
if upload is not None:
   test=data.duplicated().any()
   dup_count=data.duplicated().sum()
   slt.write("duplicate are found",dup_count)
   if test==True:
    #   slt.warning("This Dataset Contain Some Duplicate Values!"):
      dup=slt.selectbox("Do You Want To Remove Duplicate Values?",["select One ","Yes","No"])
      if dup=="Yes":
         data=data.drop_duplicates()
         slt.text("duplicate values are reomoved")
      if dup=="No":
         slt.text("Ok No Problem")  
                 
# ovearall statistic
if upload is not None:
  slt.checkbox("Summary Of The Dataset")
  slt.write(data.describe(include="all"))
  
   