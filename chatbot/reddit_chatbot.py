import mysql.connector
import pandas as pd
import time

mydb = mysql.connector.connect(
  host="192.168.1.8",
  port=3306,
  user="ram",
  password="root"
)
from sqlalchemy import create_engine
db_connection_str = 'mysql+pymysql://ram:root@192.168.1.8/_02e028ca3b617d04'
db_connection = create_engine(db_connection_str)
print("#################",db_connection)
start = time.time()
df = pd.read_sql_query("SELECT * FROM `tabD110` where company='PACIFICA HOTELS INDIA PRIVATE LIMITED';",db_connection)
print(time.time() - start)