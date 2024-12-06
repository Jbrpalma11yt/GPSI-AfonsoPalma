import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('Pack_car.db')
cursor = conexao.cursor()

# Confirmar a inserção
conexao.commit()

# Selecionar e exibir os dados inseridos
cursor.execute('SELECT * FROM Pack')
resultados = cursor.fetchall()

print("\nDados inseridos na tabela:")
for pack in resultados:
    print(pack)
    # Fechar a conexão
conexao.close()