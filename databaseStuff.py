import sqlite3




# c.execute("DROP TABLE UserInfo")
# c.execute("""CREATE TABLE UserInfo(
#             first text,
#             last text,
#             email text,
#             password text
#             )""")
# conn.commit
def lookForUser(username, password):
    conn = sqlite3.connect('Users.db')

    c = conn.cursor()
    val = c.execute("SELECT * FROM UserInfo WHERE email=?",(username,))
    
   
    dataholder = c.fetchall()
    print(dataholder)
    if dataholder is None:
        print("no data")
        return

    if dataholder[0][3] == password:
        print("this is an account")
    else:
        print("this is not an account")
    conn.commit()  
    conn.close()


def addToDataBase(user):
    conn = sqlite3.connect('Users.db')

    c = conn.cursor()
    c.execute("INSERT INTO UserInfo VALUES (?,?,?,?)",(user.first, user.last, user.email, user.password))
    conn.commit
    c.execute("SELECT * FROM UserInfo")
    print(c.fetchall())
    conn.commit()  
    conn.close()

# c.execute("INSERT INTO UserInfo VALUES('thiago', 'abreu', 'thiago@gmail.com', '67766')")


# c.execute("""CREATE TABLE employee(
#             first text,
#             last text,
#             pay inetger

#             )""")

#c.execute("INSERT INTO employee VALUES ('Aaron', 'Crawford', '50000')")



# c.execute("INSERT INTO employee VALUES(?, ?, ?)", (emp_2.first,emp_2.last, emp_2.pay))
# conn.commit()




