import os
import sqlite3

def idlist(directory, all_cards):
    path = directory + "/EDOPro.exe"
    
    if not os.path.isfile(path):
        return []
    
    list = []

    path = directory + "/expansions/cards.cdb"

    con = sqlite3.connect(path)
    cur = con.cursor()

    cur.execute("SELECT id FROM 'texts'")
    data = cur.fetchall()
    con.close()

    for row in data:
        list.append(row[0])

    if all_cards:
        path = directory + "/expansions/cards-rush.cdb"
        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute("SELECT id FROM 'texts'")
        data = cur.fetchall()
        con.close()

        for row in data:
            list.append(row[0])
        
        path = directory + "/expansions/cards-skills.cdb"
        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute("SELECT id FROM 'texts'")
        data = cur.fetchall()
        con.close()

        for row in data:
            list.append(row[0])

    return list