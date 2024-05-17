import pathlib
import os
import mysql.connector

global path_string

path_string='D:\\Università\\Digital Content Retrieval B\\Progetto DCR\\DCRB'
#path_string='D:\\Università'

def get_list():
    global path_string
    
    os.chdir(path_string)
    
    tree = pathlib.Path("")

    a=tree.rglob("*")

    ltemp=list(a)

    listfiles=[]

    i=0
    for i in range(len(ltemp)):
        listfiles.append(str(ltemp[i]))

    return listfiles

def popolate_objects():

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="password",
      database="search"
    )

    mycursor = mydb.cursor()

    listfiles=get_list()

    mycursor.execute("DELETE FROM objects")

    mydb.commit()
    
    i=0
    for i in range(len(listfiles)):
        o=listfiles[i]
        s=o.split("\\")
        name=s[len(s)-1]

        if os.path.isdir(o):
            typefile=1
        elif ((o.endswith(".txt")) or (o.endswith(".html"))):
            typefile=2
        else:
            typefile=3

        child=i+1

        path=o

        size=os.stat(path).st_size/ (1024)

        dimensione=f"{size:.2f} KB"

        if size==0:
            dimensione=None
        
        q="INSERT INTO objects (id, full_path, name, type, size) VALUES (%s, %s, %s, %s, %s)"
        val = (child, path, name, typefile, dimensione)
        mycursor.execute(q, val)


    mydb.commit()



def popolate_content():

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="password",
      database="search"
    )

    mycursor = mydb.cursor()

    os.chdir(path_string)

    listfiles=get_list()

    mycursor.execute("DELETE FROM content")

    mydb.commit()
    
    i=0
    for i in range(len(listfiles)):
        o=listfiles[i]

        if not os.path.isdir(o):
            try:
                file=open(o,"r")
                testo=file.read()
                file.close()

                q="INSERT INTO content (id, text) VALUES (%s, %s)"
                val=(i+1,testo)
                mycursor.execute(q, val)
            except:
                pass

    mydb.commit()    


popolate_objects()
popolate_content()

    
