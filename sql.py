import sqlite3
from sqltest import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employee(
#             first text,
#             last text,
#             pay inetger

#             )""")

#c.execute("INSERT INTO employee VALUES ('Aaron', 'Crawford', '50000')")



emp_1 = Employee('Jim','Dog','5000')
emp_2 = Employee('joe','nate','534000')
emp_3 = Employee('larry','narmath','100')

# c.execute("INSERT INTO employee VALUES(?, ?, ?)", (emp_2.first,emp_2.last, emp_2.pay))
# conn.commit()

c.execute("SELECT * FROM employee")
print(c.fetchall())


conn.commit()

conn.close()


