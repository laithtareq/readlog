import re,sqlite3
db = sqlite3.connect("Data.db")
db.execute("create table if not EXISTS At(Text char,Ref int)")
db.execute("delete from At")
db.execute("create table if not EXISTS Logs(Date date,Time time,Type char,Text char,ID int,Ref int)")
db.execute("delete from Logs")
db.execute("create table if not EXISTS Logs2(Type char,Text char,ID int,Ref int)")
db.execute("delete from Logs2")
File = open("server2.log","r")
Data = re.findall("\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+\] [ERROR|WARN].+|: com\.accela\.aa\.exception\..+:.+|.+at.+",File.read())
#for line in File:
#    print(line)
ID = 0
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
        
        db.execute("insert into Logs(Date,Time,Type,Text,ID,Ref) values (?,?,?,?,?,?)",(Date,Time,Type,Text,ID,""))
    elif re.match(": com\.accela\.aa\.exception\..+:.+",line):
        ID+=1
        Type = re.findall(": (com\.accela\.aa\.exception\..+):.+",line)[0]
        Text = re.findall(": com\.accela\.aa\.exception\..+:(.+)",line)[0]
        db.execute("insert into Logs2(Type,Text,ID,Ref) values (?,?,?,?)",(Type,Text,ID,""))
    else:

        if re.match(".+at.+",Text) :
            db.execute("insert into At(Text,Ref) values (?,?)",(Text,ID))
        elif re.match(".+at.+",line):
            db.execute("insert into At(Text,Ref) values (?,?)",(line,ID))
        else:
            db.execute("insert into At(Text,Ref) values (?,?)",(Text,""))
    
db.commit()
