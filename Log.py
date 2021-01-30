import re,sqlite3
db = sqlite3.connect("Data.db")
db.execute("create table if not EXISTS Logs(Date date,Time time,Type char,Text char,ID int,Ref int)")
db.execute("delete from Logs")
File = open("server2.log","r")
Data = re.findall("\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+\] [ERROR|WARN].+",File.read())
#for line in File:
#    print(line)
ID = 0
for line in Data:
    Date = re.findall("\[([0-9]{4}-[0-9]{2}-[0-9]{2}) [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+\] [ERROR|WARN]+.+",line)[0]
    Time = re.findall("\[[0-9]{4}-[0-9]{2}-[0-9]{2} ([0-9]{2}:[0-9]{2}:[0-9]{2}),[0-9]+\] [ERROR|WARN]+.+",line)[0]
    Type = re.findall("\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+\] ([ERROR|WARN]+).+",line)[0]
    Text = re.findall("\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+\] [ERROR|WARN]+(.+)",line)[0]
    
    if re.match(".+java\.lang\.Exception",Text):
        ID+=1
        db.execute("insert into Logs(Date,Time,Type,Text,ID,Ref) values (?,?,?,?,?,?)",(Date,Time,Type,Text,ID,""))
    else:
        #re.match(r"\\", r"\\")
        if re.match(".+at.+",Text):
            db.execute("insert into Logs(Date,Time,Type,Text,ID,Ref) values (?,?,?,?,?,?)",(Date,Time,Type,Text,"",ID))
        else:
            db.execute("insert into Logs(Date,Time,Type,Text,ID,Ref) values (?,?,?,?,?,?)",(Date,Time,Type,Text,"",""))
    
db.commit()
