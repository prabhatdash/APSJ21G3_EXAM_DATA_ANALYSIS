import mysql.connector as mc
dbc = mc.connect(host="localhost",user="root",passwd="Abhi@mysql1234",database="Student_data")
cursor=dbc.cursor()

