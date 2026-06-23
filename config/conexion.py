import pymysql

def conectar():
    return pymysql.connect(
        host="bwzzc4ivpfvrmnb3g3qo-mysql.services.clever-cloud.com",
        user="ucr379ul46b7eqsg",
        password="2uz9cVAR5DYRoYWqmZay",
        database="bwzzc4ivpfvrmnb3g3qo",
        port=3306
    )
        if conexion.is_connected():
            print("✅ Conexión establecida")
            return conexion
        else:
            print("❌ Conexión fallida (is_connected = False)")
            return None
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")
        return None
