# Add a product (p100, cd, 5) in Product and (p100, d2, 50) in Stock.

#import the libraries
import  sqlite3

#For isolation, isolation_level has been defined
#The isolation_level of the connection, controlling whether and how transactions are implicitly opened. 
#Can be "DEFERRED" (default), "EXCLUSIVE" or "IMMEDIATE"; or None to disable opening transactions implicitly

database_name = "TRIAL_2"
conn = sqlite3.connect(database_name, timeout=5.0, detect_types=0, 
isolation_level='DEFERRED', check_same_thread=True,
factory=sqlite3.Connection, cached_statements=128, uri=False)



#conn  =  sqlite3 . connect ( 'mydatabase2.db' )
cursor  =  conn . cursor ()


print("Start")

cur = conn.cursor()

'''
: SERIALIZABLE
conn.start_transaction(isolation_level = 'SERIALIZABLE')
conn.autocommit = False
'''

#create the PRODUCT table 
cursor.execute("CREATE TABLE PRODUCT(prodid char(30), name char(30), price decimal(7,2));")

# inserting data into the PRODUCT table 
try:
  cursor . execute ( """
  INSERT INTO PRODUCT('prodid','name', price )
  VALUES('p100','cd', 5)
  """)
except (Exception) as err:
    print(err)
    print("Transactions could not be completed so database will be rolled back before start of transactions")
    conn.rollback()
    
    
#create the STOCK table 
cursor.execute("CREATE TABLE STOCK(prodid char(30), deptid char(30), qty decimal(7,2));")

# inserting data into the STOCK table 
try:
  cursor . execute ( """
  INSERT INTO STOCK('prodid','deptid', qty )
  VALUES('p100', 'd2', 50)
  """)

except (Exception) as err:
    print(err)
    print("Transactions could not be completed so database will be rolled back before start of transactions")
    conn.rollback()

#print contents of Product
def get_posts_1():
    cur.execute("SELECT * FROM PRODUCT")
    print("PRODUCT")
    print(cur.fetchall())

get_posts_1()

#print contents of STOCK

def get_posts_2():
    cur.execute("SELECT * FROM STOCK")    
    print("STOCK")
    print(cur.fetchall())
get_posts_2()


if (conn):
  #For atomicity
  conn.commit() 
  conn.close    
  print("\nThe SQLite connection is closed.")

print("\nEND")
