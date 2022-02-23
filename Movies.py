from queue import PriorityQueue
from Conn import *
class Movies:
    def Insert(self):
        Conobj=Connect()
        MovieName=input('Enter Movie Name.')
        LeadActor=input('Enter Lead Actor Name.')
        LeadActress=input('Enter Lead Actoress Name.')
        YearOfRealese=input('Enter Year of Realese.')
        DirectorName=input('Enter Name of The Director.')
        Conobj.InsertRecord(MovieName,LeadActor,LeadActress,YearOfRealese,DirectorName)
    def Update(self):
        Conobj=Connect()
        id=int(input('Enter Id To Update.'))
        MovieName=input('Enter NEW Movie Name.')
        LeadActor=input('Enter  NEW Lead Actor Name.')
        LeadActress=input('Enter NEW Lead Actoress Name.')
        YearOfRealese=input('Enter NEW Year of Realese.')
        DirectorName=input('Enter NEW Name of The Director.')
        Conobj.UpdateRecord(id,MovieName,LeadActor,LeadActress,YearOfRealese,DirectorName)
    def Delete(self):
        Conobj=Connect()
        id=int(input('Enter Id To Delete.'))
        Conobj.DeleteRecord(id)
    def Display(self):
        Conobj=Connect()
        Conobj.DisplayRecord()
Movie=Movies()
print('Enter Your Choice.:')
print('1. For Insert')
print('2. For Update')
print('3. For Delete')
print('4. For Display')
print('5. Exit')
ch=int(input('Enter Choice.'))
while(True):
    if ch==1:
        Movie.Insert()
    elif ch==2:
        Movie.Update()
    elif ch==3:
        Movie.Delete()
    elif ch==4:
        Movie.Display()
    elif ch==5:
        break
    else:
        print("Invalid Choice.")
    ch=int(input('Enter Choice.'))

