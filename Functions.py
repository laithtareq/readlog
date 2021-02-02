import sqlite3,re
class DataLog:
    def __init__(self,**kwargs):
        #self.LogFileName = input("Enter File Name: ")
        self.LogFileName = "server2.log"
        self.db = sqlite3.connect("Data.db")
    def UpdateDb(self):
        ID = 0
        File = open(self.LogFileName,"r")
        Data = re.findall("\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+\] [ERROR|WARN].+|: com\.accela\.aa\.exception\..+:.+|.+at.+",File.read())
        for line in Data:
            try:
                Text = re.findall("\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+\] [ERROR|WARN]+(.+)",line)[0]
            except:
                Text = ""
            if re.match(".+java\.lang\.Exception",Text):
                ID+=1
                Date = re.findall("\[([0-9]{4}-[0-9]{2}-[0-9]{2}) [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+\] [ERROR|WARN]+.+",line)[0]
                Time = re.findall("\[[0-9]{4}-[0-9]{2}-[0-9]{2} ([0-9]{2}:[0-9]{2}:[0-9]{2}),[0-9]+\] [ERROR|WARN]+.+",line)[0]
                Type = re.findall("\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+\] ([ERROR|WARN]+).+",line)[0]
                Text = re.findall("\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+\] [ERROR|WARN]+(.+)",line)[0]

                self.db.execute("insert into Logs(Date,Time,Type,Text,ID,Ref) values (?,?,?,?,?,?)",(Date,Time,Type,Text,ID,""))
            elif re.match(": com\.accela\.aa\.exception\..+:.+",line):
                ID+=1
                Type = re.findall(": (com\.accela\.aa\.exception\..+):.+",line)[0]
                Text = re.findall(": com\.accela\.aa\.exception\..+:(.+)",line)[0]
                self.db.execute("insert into Logs2(Type,Text,ID,Ref) values (?,?,?,?)",(Type,Text,ID,""))
            elif re.match("\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+\] [ERROR|WARN].+",line):
                ID+=1
                Date = re.findall("\[([0-9]{4}-[0-9]{2}-[0-9]{2}) [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+\] [ERROR|WARN]+.+",line)[0]
                Time = re.findall("\[[0-9]{4}-[0-9]{2}-[0-9]{2} ([0-9]{2}:[0-9]{2}:[0-9]{2}),[0-9]+\] [ERROR|WARN]+.+",line)[0]
                Type = re.findall("\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+\] ([ERROR|WARN]+).+",line)[0]
                Text = re.findall("\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+\] [ERROR|WARN]+(.+)",line)[0]
                self.db.execute("insert into Logs(Date,Time,Type,Text,ID,Ref) values (?,?,?,?,?,?)",(Date,Time,Type,Text,ID,""))
            else:
            
                if re.match(".+at.+",Text) :
                    self.db.execute("insert into At(Text,Ref) values (?,?)",(Text,ID))
                elif re.match(".+at.+",line):
                    self.db.execute("insert into At(Text,Ref) values (?,?)",(line,ID))
                else:
                    self.db.execute("insert into At(Text,Ref) values (?,?)",(Text,""))
        self.db.commit()
    def getData(self,Type,Date=None,Time=None):
        if Type=='ERROR' or Type=='WARN':
            if Date==None or Time==None:
                Data = self.db.execute("select * from Logs where Type = ?",(Type,))
            else:
                Data = self.db.execute("select * from Logs where Type = ? and Date = ? and Time = ?",(Type,Date,Time))
            print(Data)
            return Data
        elif Type =='Logs2':
            Data = self.db.execute("select * from Logs2")
            print(Data)
            return Data
#Log = DataLog()
#Log.UpdateDb()
#Data = Log.getData("Logs2")
#print(list(Data))