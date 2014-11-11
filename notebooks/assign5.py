# -*- coding: utf-8 -*-
"""
Created on Thu Nov 06 17:29:01 2014

@author: Morgen
"""
#importing and loading
import os,site
currdir=os.getcwd()
head,tail=os.path.split(currdir)
libdir=os.path.join(head,'lib')
site.addsitedir(libdir)
import new_walk
reload(new_walk)

files=new_walk.index('\Users\Morgen\Documents\GitHub\classcode\notebooks\cpsc189\notebooks')
#opening the files
#finding the name,seze,owner, and date modified
#spliting the data
def tree_to_csv(filename,filelist):
    with open(filename,'w') as f:
        #write the header first
        f.write('file_name;owner;size;modified\n')
        for the_line in filelist:
            thelevel=len(the_line[0].split(os.sep))-1
            f.write("{:s};{:s};{:d};{:d};{:d}\n".format(*the_line,thelevel))
#error here, not sure why?
tree_to_csv('out.csv',files)

import pandas as pd

data=pd.read_csv('out.csv',sep=';')
data
#printing the level
#adding in the indents for each level
out=data.groupby('thelevel')
for thelevel, dflevel in out:
   print thelevel,dflevel[site].sum()
   for index, item in dflevel.iterrows():
       indent=(thelevel-1)*'    '
       print thelevel, item('filename')