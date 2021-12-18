
import cx_Oracle

lib_dir = "D:\Trabajos Inacap\instantclient_21_3"
try:
    cx_Oracle.init_oracle_client(lib_dir=lib_dir)
    conexion= cx_Oracle.connect(user="admin", password="Proyectoinacap2021.", dsn="BDproyecto_high")


except Exception as ex:
    print(ex)