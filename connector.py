import mysql.connector as con
dbc = con.connect(host="localhost",user="root",passwd="root",database="Student_data")
cursor=dbc.cursor()

