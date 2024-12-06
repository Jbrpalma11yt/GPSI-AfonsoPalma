import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('seu_banco_de_dados.db')
cursor = conexao.cursor()

# Exibir os registros inseridos
print("\nCarro inserido e informações relacionadas:")
cursor.execute('''
    SELECT P.*, CA.ano, M.*
    FROM Pack P
    LEFT JOIN CarroAno CA ON P.id = CA.carro_id
    LEFT JOIN Matricula M ON P.id = M.carro_id
    WHERE P.id = ?
''', (carro_id,)) # type: ignore
resultados = cursor.fetchall()

if not resultados:
    print("Nenhum carro encontrado com o ID especificado.")
else:
    for resultado in resultados:
        print(resultado)  # Imprime a linha completa para verificar a estrutura
        print(f"Carro: {resultado[:3]}")  # Exibe as primeiras 3 colunas do Pack
        print(f"Ano do carro: {resultado[3]}")  # Exibe a coluna do ano do CarroAno
        print(f"Matricula: {resultado[4:]}")  # Exibe as colunas da Matricula

# Fechar a conexão
conexao.close()