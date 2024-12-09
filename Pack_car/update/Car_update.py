import sqlite3

def criar_tabelas():
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

def atualizar_Car(id_, novo_nome):
    # Conectar ao banco de dados
    conexao = sqlite3.connect('Pack_car.db')
    cursor = conexao.cursor()

    # Executar o comando UPDATE
    cursor.execute('''
        UPDATE Pack
        SET nome = ?
        WHERE id = ?
    ''', (novo_nome, id_aluno))

    # Confirmar as alterações
    conexao.commit()

    # Fechar a conexão
    conexao.close()

# Criar as tabelas
criar_tabelas()

# Exemplo de uso da função de atualização
id_aluno = 4796  # ID do aluno que você deseja atualizar
novo_nome = "Maria Silva"  # Novo nome que você deseja definir
atualizar_nome_aluno(id_aluno, novo_nome)