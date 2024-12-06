import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('Pack_car.db')
cursor = conexao.cursor()

# Perguntar ao utilizador o carro_id que deseja excluir
carro_id = int(input("Digite o carro_id do registro que deseja excluir da tabela CarroAno: "))

# Deletar o registro da tabela CarroAno
cursor.execute('DELETE FROM CarroAno WHERE carro_id = ?', (carro_id,))

# Confirmar as alterações
conexao.commit()

# Verificar se o registro foi excluído
if cursor.rowcount > 0:
    print(f"Registro com carro_id {carro_id} excluído com sucesso da tabela CarroAno.")
else:
    print(f"Nenhum registro encontrado com carro_id {carro_id} na tabela CarroAno.")

# Fechar a conexão
conexao.close()