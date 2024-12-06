import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('Pack_car.db')
cursor = conexao.cursor()

# Perguntar ao utilizador os dados do carro
nome_carro = input("Digite o nome do carro: ")
modelo_carro = input("Digite o modelo do carro: ")
ano_carro = input("Digite o ano do carro: ")  # Solicitar o ano do carro

# Inserir os dados do carro na tabela Pack
cursor.execute('INSERT INTO Pack (nome, modelo) VALUES (?, ?)', (nome_carro, modelo_carro))
# Obter o ID do carro recém-inserido
carro_id = cursor.lastrowid

# Inserir o ano do carro na tabela CarroAno
cursor.execute('INSERT INTO CarroAno (carro_id, ano) VALUES (?, ?)', (carro_id, ano_carro))

# Perguntar ao utilizador quantas matriculas de carros ele deseja associar a este carro
num_matricula = int(input("Quantas matriculas de carros você deseja associar a este carro? "))

# Loop para coletar os dados das matriculas de carros
for i in range(num_matricula):
    matricula = input(f"Digite o numero da matricula #{i + 1}: ")
    
    # Inserir a matricula na tabela Matricula, associando-a ao carro
    cursor.execute('INSERT INTO Matricula (carro_id, matricula) VALUES (?, ?)', (carro_id, matricula))

# Confirmar as inserções
conexao.commit()

# Exibir os registros inseridos
print("\nCarro inserido e informações relacionadas:")
cursor.execute('''
    SELECT P.*, CA.ano, M.*
    FROM Pack P
    LEFT JOIN CarroAno CA ON P.id = CA.carro_id
    LEFT JOIN Matricula M ON P.id = M.carro_id
    WHERE P.id = ?
''', (carro_id,))
resultados = cursor.fetchall()

for resultado in resultados:
    # resultado[0] até resultado[n] representam as colunas de Pack, CarroAno e Matricula
    print(f"Carro: {resultado[:3]}")  # Exibe as primeiras 3 colunas do Pack
    print(f"Ano do carro: {resultado[3]}")  # Exibe a coluna do ano do CarroAno
    print(f"Matricula: {resultado[4:]}")  # Exibe as colunas da Matricula

# Fechar a conexão
conexao.close()