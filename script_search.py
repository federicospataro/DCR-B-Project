import pathlib
import os
import mysql.connector

def search():

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="password",
      database="search"
    )

    mycursor = mydb.cursor()

    string=input("Type the term to search for: ")

    print("\n===============================================================================")

    q="SELECT full_path,name,type,size FROM objects WHERE name LIKE '%%s%'"

    mycursor.execute(q.replace("%s",string))

    r = mycursor.fetchall()

    print("\n\nMatch in the file names: ("+str(len(r))+")\n")

    i=0
    for i in range(len(r)):
        o=r[i]

        if o[2]==1:
            tipo="Folder"
        elif o[2]==2:
            tipo="Readable File"
        else:
            tipo="Non Readable File"
   
        print("Full Path: "+o[0]+"\nName: "+o[1]+"\nType: "+tipo+"\nSize: "+str(o[3])+"\n\n")

    print("===============================================================================")

    q="""select a.id, full_path,cont from 
         (select id,  ROUND((CHAR_LENGTH(text)- CHAR_LENGTH( REPLACE ( LOWER(text), %s, "") )) / CHAR_LENGTH(%s)) as cont from content) a
         join
         objects
         on objects.id=a.id
         where cont>0"""

    val=(string,string)

    mycursor.execute(q,val)

    r = mycursor.fetchall()

    print("\n\nMatch in the file contents: ("+str(len(r))+")\n")

    i=0
    for i in range(len(r)):
        o=r[i]
        print("Full Path: "+o[1]+"\nNumber of occurrences found: "+str(o[2])+"\n\n")

    print("===============================================================================")

            
search()



    
