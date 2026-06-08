import pandas as pd
import oracledb

df = pd.read_csv("data/processed/asteroids_processed.csv")

conn = oracledb.connect(
    user="rm98067",
    password="020205",
    dsn="oracle.fiap.com.br:1521/ORCL"
)

cursor = conn.cursor()

# Limpa dados antigos para evitar duplicações
try:
    cursor.execute("DELETE FROM ASTEROIDS")
    conn.commit()
except:
    pass

for _, row in df.iterrows():

    cursor.execute("""
        INSERT INTO ASTEROIDS (
            ID,
            NAME,
            ABSOLUTE_MAGNITUDE_H,
            IS_POTENTIALLY_HAZARDOUS
        )
        VALUES (:1, :2, :3, :4)
    """,
    (
        str(row["id"]),
        str(row["name"]),
        float(row["absolute_magnitude_h"]),
        str(row["is_potentially_hazardous"])
    ))

conn.commit()

print(f"{len(df)} registros carregados no Oracle!")

conn.close()