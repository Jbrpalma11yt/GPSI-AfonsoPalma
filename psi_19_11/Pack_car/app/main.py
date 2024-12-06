import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('Pack_car.db')
cursor = conexao.cursor()

# Criar a tabela, se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pack (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    modelo INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Matricula (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    carro_id INTEGER,
    matricula TEXT NOT NULL,
    FOREIGN KEY (carro_id) REFERENCES Pack (id)
)
''')

# Perguntar ao utilizador os dados do carro
nome_carro = input("Digite o nome do carro: ")
modelo_carro = input("Digite o modelo do carro: ")

# Inserir os dados do carro na tabela
cursor.execute('INSERT INTO Pack (nome, modelo) VALUES (?, ?)', (nome_carro, modelo_carro))
# Obter o ID do carro recém-inserido
carro_id = cursor.lastrowid

# Perguntar ao utilizador quantas marcas de carros ele deseja associar a este carro
num_marcas = int(input("Quantas marcas de carros você deseja associar a este carro? "))

# Loop para coletar os dados das marcas de carros
for i in range(num_marcas):
    marca = input(f"Digite o nome da marca #{i + 1}: ")
    
    # Aqui você pode querer armazenar a marca de alguma forma.
    # Se você quiser associar as marcas a um carro, você precisaria de outra tabela.
    # Para este exemplo, vamos apenas imprimir as marcas.
    print(f"Marca #{i + 1} associada ao carro '{nome_carro}' (ID: {carro_id}): {marca}")

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