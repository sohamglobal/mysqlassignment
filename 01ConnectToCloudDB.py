#pip install pymysql

import pymysql

con=pymysql.connect(host='blkachwd7lci0izx4jnv-mysql.services.clever-cloud.com',user='ulswdsueqsnqhapm',password='rMRdjG8zb25twAVIF48e',database='blkachwd7lci0izx4jnv')
print('successfully connected to cloud database')
con.close()