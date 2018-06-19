# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 19:04:23 2018

@author: ABHISHEK
"""

import os
import pandas as pd
import cufflinks as cf
from plotly import __version__
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)
cf.go_offline()


flag=1
def input_name():
    global f
    f = input("Enter the directory = ")
    
    c=check(f)
    if(c==False):
        print("Incorrect Directory\nPlease try again!\n")
        input_name()
    

def check(f1):
    if(os.path.exists(f1)==True):
        return True
    else:
        return False
input_name() 
file_path=f+"\\" 

os.chdir(file_path)
print(file_path)
print('\n')




while(flag==1): 
    
    
    
    size=[]

    for file in (os.listdir()):
         size.append(os.stat(file).st_size)

    print('\n')
    
    
    size1=[i/(1024*1024) for i in size]
    d={'DISK_SPACE_IN_MEGA_BYTES': size1,'FILE_NAME': os.listdir(),}
    df = pd.DataFrame(data=d,columns=['FILE_NAME','DISK_SPACE_IN_MEGA_BYTES'])
    
    
    print("Visualization of the data is as follows :\n\n")
    df.iplot(kind='bar',x='FILE_NAME',y='DISK_SPACE_IN_MEGA_BYTES',mode='markers',xTitle='FILE_NAME',yTitle='DISK_SPACE_IN_MEGA_BYTES',color='red')
    
    
    choice=input("\n\nEnter 1 to go to a child directory\nEnter 0 to go to parent directory\nEnter -1 to exit\nEnter your choice = ")
    
    if(choice=='1'):
        
        child_number=df.index
        child_name=df['FILE_NAME']
            
        print(len(child_name))
        for i in range(0,len(child_name)-1):
            print("\nEnter ",child_number[i],"to go to ",child_name[i])
            
        child=input("Enter your choice = ")
        file_path = os.path.join(file_path,child_name[int(child)])
        os.chdir(file_path)
        flag=1
    
    elif(choice=='0'):
        file_path = file_path[:-1]
        file_path=os.path.dirname(file_path)
        os.chdir(file_path)
        flag=1
        
        
    elif(choice=='-1'):
        flag=0
        
    else:
        print("Incorrect choice!")
        print("\nPrevious visualization is as follows: \n\n\n")
        flag=1
        
    
        
print("thank you!")