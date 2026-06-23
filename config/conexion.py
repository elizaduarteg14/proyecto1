import pymysql

def conectar():
    return pymysql.connect(
        host="bwzzc4ivpfvrmnb3g3qo-mysql.services.clever-cloud.com",
        user="ucr379ul46b7eqsg",
        password="2uz9cVAR5DYRoYWqmZay",
        database="bwzzc4ivpfvrmnb3g3qo",
        port=3306
    )
