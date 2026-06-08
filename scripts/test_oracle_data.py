import oracledb

conn = oracledb.connect(
    user="rm98067",
    password="020205",
    dsn="oracle.fiap.com.br:1521/ORCL"
)

cursor = conn.cursor()

cursor.execute("""
SELECT COUNT(*)
FROM ASTEROIDS
""")

resultado = cursor.fetchone()

print("Total de registros:", resultado[0])

conn.close()