import re,sqlite3
db = sqlite3.connect("Data.db")
db.execute("create table if not EXISTS Logs2(Type char,Text char,ID int,Ref int)")
db.execute("delete from Logs2")
File = open("server2.log","r")
Data = re.findall(": com\.accela\.aa\.exception\..+:.+|.+at.+",File.read())
ID = 0
for line in Data:
    Type = re.findall(": (com\.accela\.aa\.exception\..+):.+",line)[0]
    Text = re.findall(": com\.accela\.aa\.exception\..+:(.+)",line)[0]
    print(line)
#    if re.match(": com\.accela\.aa\.exception\..+:.+",line):
#        ID+=1
#        db.execute("insert into Logs2(Type,Text,ID,Ref) values (?,?,?,?)",(Type,Text,ID,""))
#    else:
#        print("Ok")
#        if re.match(".+at.+",line):
#            db.execute("insert into Logs2(Type,Text,ID,Ref) values (?,?,?,?)",(Type,Text,"",ID))
#        else:
#            pass
    
db.commit()