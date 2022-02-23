from msilib.schema import ControlEvent
import sqlite3
class Connect:
    def __init__(self):
        self.con=sqlite3.connect('Movies.db')
        self.con.execute('create table if not exists MoviesDetails (id INTEGER PRIMARY KEY AUTOINCREMENT, MovieName text,LeadActor text,LeadActress text, YearOfRealese number,DirectorName text)')
    def InsertRecord(self,MovieName,LeadActor,LeadActress,YearOfRealese,DirectorName):        
        self.con.execute('insert into MoviesDetails(MovieName,LeadActor,LeadActress,YearOfRealese,DirectorName)values(?,?,?,?,?)',(MovieName,LeadActor,LeadActress,YearOfRealese,DirectorName))
        print("Record Inserted.")
        self.con.commit()
    def UpdateRecord(self,id,MovieName,LeadActor,LeadActress,YearOfRealese,DirectorName):
        self.con.execute('update MoviesDetails set MovieName=?,LeadActor=?,LeadActress=?,YearOfRealese=?,DirectorName=? where id=?',(MovieName,LeadActor,LeadActress,YearOfRealese,DirectorName,id))
        print("Record Updated.")
        self.con.commit()
    def DeleteRecord(self,idd):
        self.con.execute('delete from MoviesDetails where id=?',(idd,))
        print("Record Deleted.")
        self.con.commit()
    def DisplayRecord(self):
        Result=self.con.execute('select * from MoviesDetails')
        Rows=Result.fetchall()
        for Row in Rows:
            print('**********************************************')        
            print("Movie Name.:",Row[0])
            print("Movie LeadActor Name.:",Row[1])
            print("Movie LeadActress Name.:",Row[2])
            print("Movie YearOfRealese.:",Row[3])
            print("Movie DirectorName.:",Row[4])
            print('**********************************************')        
conn=Connect()