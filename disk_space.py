# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 16:18:21 2018

@author: ABHISHEK
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 16:14:38 2018

@author: ABHISHEK
"""

import os
import pandas as pd
from plotly import __version__
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
import plotly.graph_objs as go
init_notebook_mode(connected=True)


flag=1
#taking directory as input
def input_name():
    global f
    f = input("Enter the directory = ")
    
    c=check(f)
    if(c==False):
        print("Incorrect Directory\nPlease try again!\n")
        input_name()
    
#checking whether the directory exists
def check(f1):
    if(os.path.exists(f1)==True):
        return True
    else:
        return False
input_name() 
file_path=f+"\\" 
#setting the directory to the input directory name
os.chdir(file_path)

print(file_path)
print('\n')

while(flag==1): 
    
    size=[]

    for file in (os.listdir()):
       size.append(os.stat(file).st_size)

    print('\n')
    
    size1=[i/(1024*1024) for i in size]
    #making a dataFrame to store the files and their respective size in megabytes
    d={'DISK_SPACE_IN_MEGA_BYTES': size1,'FILE_NAME': os.listdir(),}
    df = pd.DataFrame(data=d,columns=['FILE_NAME','DISK_SPACE_IN_MEGA_BYTES'])
    
    #plotting a bar graph to get a visualization of the space used by the files 
    print("Visualization of the data is as follows :\n\n")
    iplot([go.Bar(x=os.listdir(), y=size1)])
  
    #Checking whether the user wants to go to a child directory, parent directory or exit from the program.
    choice=input("\n\nEnter 1 to go to a child directory\nEnter 0 to go to parent directory\nEnter -1 to exit\nEnter your choice = ")
    
    
    if(choice=='1'):
        child_number=df.index
        child_name=df['FILE_NAME']
        print(len(child_name))
        #Showing the files in the current directory
        for i in range(0,len(child_name)-1):
            print("\nEnter ",child_number[i],"to go to ",child_name[i])
        #Taking user input 
        child=input("Enter your choice = ")
        file_path = os.path.join(file_path,child_name[int(child)])
        #Setting the current path to the user specified child file.
        os.chdir(file_path)
        flag=1
    
    elif(choice=='0'):
        file_path = file_path[:-1]
        file_path=os.path.dirname(file_path)
        #Setting the current path to the parent directory.
        os.chdir(file_path)
        flag=1
        
        
    elif(choice=='-1'):
        #Exit from the program
        flag=0
        
    else:
        print("Incorrect choice!")
        print("\nPrevious visualization is as follows: \n\n\n")
        flag=1
        
    
        
print("thank you!")