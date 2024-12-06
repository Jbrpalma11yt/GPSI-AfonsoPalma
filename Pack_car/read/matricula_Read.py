import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('Pack_car.db')
cursor = conexao.cursor()

# Confirmar a inserção
conexao.commit()

# Selecionar e exibir os dados inseridos
cursor.execute('SELECT * FROM Matricula')  # Se a tabela se chama Matriculas
resultados = cursor.fetchall()

print("\nDados inseridos na tabela:")
for matricula in resultados:
    print(matricula)
    # Fechar a conexão
conexao.close()