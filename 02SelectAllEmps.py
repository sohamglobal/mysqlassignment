import pymysql

con=pymysql.connect(host='blkachwd7lci0izx4jnv-mysql.services.clever-cloud.com',user='ulswdsueqsnqhapm',password='rMRdjG8zb25twAVIF48e',database='blkachwd7lci0izx4jnv')
curs=con.cursor()

curs.execute("select * from emp")
data=curs.fetchall()
#data is returned in the form of tuple of tuples
print(data)
con.close()



