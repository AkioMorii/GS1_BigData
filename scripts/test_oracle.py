import oracledb

usuario = input("Usuário Oracle: ")
senha = input("Senha Oracle: ")

try:
    conn = oracledb.connect(
        user=usuario,
        password=senha,
        dsn="oracle.fiap.com.br:1521/ORCL"
    )

    print("✅ Conectado com sucesso!")

    conn.close()

except Exception as e:
    print("❌ Erro:")
    print(e)