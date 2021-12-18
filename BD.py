import cx_Oracle

#lib_dir=r"oracle.client"
try:
    cx_Oracle.init_oracle_client()
    conexion=cx_Oracle.connect(user="admin", password="Proyectoinacap2021.", dsn="localhost:1521/xe")

except:
    print("error")


