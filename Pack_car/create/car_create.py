import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('Pack_car.db')
cursor = conexao.cursor()

# Excluir as tabelas se já existirem
cursor.execute('DROP TABLE IF EXISTS Pack')
cursor.execute('DROP TABLE IF EXISTS Matricula')
cursor.execute('DROP TABLE IF EXISTS CarroAno')

# Criar tabela Pack, sem a coluna ano
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pack (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    modelo TEXT NOT NULL
)
''')

# Criar tabela Matricula, se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS Matricula (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    carro_id INTEGER,
    matricula TEXT NOT NULL,
    FOREIGN KEY (carro_id) REFERENCES Pack (id)
)
''')

# Criar tabela CarroAno, que armazena o ano do carro
cursor.execute('''
CREATE TABLE IF NOT EXISTS CarroAno (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    carro_id INTEGER,
    ano INTEGER NOT NULL,
    FOREIGN KEY (carro_id) REFERENCES Pack (id)
)
''')

# Confirmar as alterações
conexao.commit()

# Fechar a conexão
conexao.close()