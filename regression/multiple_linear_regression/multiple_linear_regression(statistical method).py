# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:01:12 2020

@author: Aiva
"""


import numpy as np
se_line=0
se_mean=0
accuracy=0
xcord=0
ycord=0
cords=np.zeros(2)
no_of_variables=0
beta_o=[]
beta_x=[]

se_mean=0
se_line=0
no_of_variables=int(input("Enter the number of coeffecients:"))
size=int(input("Enter the number of training data:"))
term_of_se_line=np.zeros(size)
beta_i=np.zeros(no_of_variables)
data=np.zeros((size,no_of_variables+1))
mean=[]
for i in range(size):
    cords=input("Enter data:").split(",")
    for j in range(len(cords)):
        data[i][j]=int(cords[j])
#completed
        
        
mean=(data.sum(axis=0))/size

beta_upper=np.zeros(no_of_variables)
beta_lower=np.zeros(no_of_variables)

for i in range(no_of_variables):
    for j in range(size):
        
        beta_upper[i]+=(data[j][i]-mean[i])*(data[j][no_of_variables]-mean[no_of_variables])
        beta_lower[i]+=(data[j][i]-mean[i])*(data[j][i]-mean[i])
     
for i in range(no_of_variables):
    
    beta_i[i]=(beta_upper[i]/beta_lower[i])
    
beta_x=np.multiply(beta_i,mean[:no_of_variables-1])
beta_o=mean[no_of_variables] 
for i in range(no_of_variables):
    beta_o-=(beta_x[i])
    
#completed


print("resulted equation is y=",beta_i,"x + ",beta_o,"\n")  

for i in range(size):
    term_of_se_line[i]=data[i][no_of_variables]
    coef_terms=np.multiply(beta_i,data[i,:no_of_variables])
    term_of_se_line[i]-=coef_terms.sum(axis=0)
    term_of_se_line[i]*=term_of_se_line[i]
    
    se_mean+=(data[i][no_of_variables]-mean[no_of_variables])*(data[i][no_of_variables]-mean[no_of_variables])
    
se_line=term_of_se_line.sum(axis=0)
    

    
   
     
accuracy=1-(se_line/se_mean)    

print("The accuracy of the algorithm is: ",accuracy)