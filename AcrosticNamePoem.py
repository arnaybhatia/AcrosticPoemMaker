import os
import random
from string import capwords
#Open the file and read it in
file=open("words.txt")
data=file.read()
data=data.lower()
#Split the words into a list
list=data.split("\n")
#Get the name
name=input("What is first your name? ")
name=name.lower()

#Split the name of the person into letters
x=0
nameletterlist=[]
for letter in name:
    find=name[x]
    x=x+1
    nameletterlist+=str(find)
#Get the first letter of each item in list
z=0
firstletter=[]
for letter in list:
    firstletter+=str(list[z][0])
    z=z+1
a=0
matchlist=[]
for letter in nameletterlist:
    d=0
    matchlisttemp=[]
    for letter in firstletter:
        if nameletterlist[a]==firstletter[d]:
            matchlisttemp.append(list[d])
        d=d+1
    i=len(matchlisttemp)
    h=random.randrange(0,i)
    matchlist.append(matchlisttemp[h])
    a=a+1
k=0
for g in matchlist:
    
    print(capwords(matchlist[k]))
    k=k+1